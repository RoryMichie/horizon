import synthizer

buffer_cache = {}


class sound_synthizer:
    def __init__(self, filename, context, hrtf=True, source_type="3d"):
        self.filename = filename
        self.context = context
        self.hrtf = hrtf
        self.source_type = source_type
        if hrtf is True:
            self.context.default_panner_strategy.value = synthizer.PannerStrategy.HRTF
        elif hrtf is False:
            self.context.default_panner_strategy.value = synthizer.PannerStrategy.STEREO
        else:
            raise TypeError(
                "expected True/False value for hrtf, but got " + str(type(hrtf))
            )
        if filename in buffer_cache:
            self.buffer = buffer_cache[filename]
        else:
            self.buffer = synthizer.Buffer.from_file(filename)
            buffer_cache[filename] = self.buffer
        self.generator = synthizer.BufferGenerator(context)
        self.generator.buffer.value = self.buffer

        if source_type == "3d":
            self.source = synthizer.Source3D(context)
        elif source_type == "scalar":
            self.source = synthizer.ScalarPannedSource(context)
        elif source_type == "direct":
            self.source = synthizer.DirectSource(context)
        elif source_type == "angular":
            self.source = synthizer.AngularPannedSource(context)
        else:
            raise ValueError("must be scalar, 3d, angular, or direct")
        self.source.add_generator(self.generator)
        self.source.pause()
        self.generator.playback_position.value = 0

    def play(self):
        if (
            self.generator.playback_position.value
            >= self.buffer.get_length_in_seconds()
        ):
            self.generator.playback_position.value = 0
            self.source.pause()
        self.source.play()

    def resume(self):
        self.source.play()

    def pause(self):
        self.source.pause()

    def stop(self):
        self.generator.playback_position.value = 0
        self.source.pause()

    def set_pitch(self, pitch):
        self.generator.pitch_bend.value = pitch

    def position(self, x, y=0, z=0):
        if self.source_type == "3d":
            self.source.position.value = (x, y, z)

        elif self.source_type == "angular":
            self.source.azimuth.value = x
            self.source.elevation.value = y
        elif self.source_type == "scalar":
            self.source.panning_scalar.value = x

    def seek(self, position):
        self.generator.playback_position.value = position

    def gain(self, volume):
        gain = 10 ** (volume / 20)
        self.source.gain.value = gain

    def loop(self, value):
        self.generator.looping.value = value

    def set_reverb(
        self,
        gain: float = 1.0,
        lf_reference: float = 500,
        hf_reference: float = 200,
        lf_rolloff: float = 1.0,
        hf_rolloff: float = 0.5,
        delay: float = 0.01,
        defusion: float = 1.0,
        modulation_freqency: float = 0.5,
        modulation_depth: float = 0.01,
        mean_free_path: float = 0.02,
        t60: float = 0.3,
    ) -> synthizer.GlobalFdnReverb:
        reverb = synthizer.GlobalFdnReverb(self.context)
        reverb.gain.value = gain
        reverb.late_reflections_delay.value = delay
        reverb.late_reflections_diffusion.value = defusion
        reverb.late_reflections_hf_reference.value = hf_reference
        reverb.late_reflections_hf_rolloff.value = hf_rolloff
        reverb.late_reflections_lf_reference.value = lf_reference
        reverb.late_reflections_lf_rolloff.value = lf_rolloff
        reverb.late_reflections_modulation_depth.value = modulation_depth
        reverb.late_reflections_modulation_frequency.value = modulation_freqency
        reverb.mean_free_path.value = mean_free_path
        reverb.t60.value = t60
        self.context.config_route(self.source, reverb)
        return reverb

    def clear_reverb(self, reverb: synthizer.GlobalFdnReverb):
        self.context.remove_route(self.source, reverb)
        reverb.dec_ref()

    def destroy(self):
        self.__del__()  # wrapper for lua otherwise unnecessary. Nilling sound objects in lua does not destroy them in python, only unlinks it.

    def __del__(self):
        self.source.dec_ref()
        self.generator.dec_ref()
