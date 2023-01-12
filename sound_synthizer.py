import synthizer

buffer_cache = {}


class sound_synthizer:
    def __init__(self, filename, context, hrtf=True, source_type="3d"):
        self.filename = filename
        self.context = context
        self.hrtf = hrtf
        self.source_type = source_type
        if hrtf == True:

            self.context.default_panner_strategy.value = synthizer.PannerStrategy.HRTF
        elif hrtf == False:
            self.context.default_panner_strategy.value = synthizer.PannerStrategy.STEREO
        else:
            raise ValueError

        if filename in buffer_cache:
            self.buffer = buffer_cache[filename]
        else:
            self.buffer = synthizer.Buffer.from_file(filename)
            buffer_cache[filename] = self.buffer
        self.generator = synthizer.BufferGenerator(context)
        self.generator.buffer.value = self.buffer

        self.source = synthizer.Source3D(context)
        self.source.add_generator(self.generator)
        self.source.pause()
        self.generator.playback_position.value = 0

    def play(self):
        self.source.play()

    def pause(self):
        self.source.pause()

    def stop(self):
        self.generator.playback_position = 0
        self.source.pause()

    def set_pitch(self, pitch):
        self.generator.pitch_bend.value = pitch

    def position(self, x, y=0, z=0):
        self.source.position.value = (x, y, z)

    def seek(self, position):
        self.generator.playback_position.value = position

    def gain(self, volume):
        gain = 10**(volume/20)
        self.source.gain.value = gain

    def loop(self, value):
        self.generator.looping.value = value

    def __del__(self):
        self.source.dec_ref()
        self.generator.dec_ref()



