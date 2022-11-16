
class sound_synthizer:
    def __init__(self, filename, context):
        self.filename = filename
        self.context = context
        self.context.default_panner_strategy.value = synthizer.PannerStrategy.HRTF
        self.buffer = synthizer.Buffer.from_file(filename)
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

    def position(self, x, y=0, z=0):
        self.source.position.value = (x, y, z)

    def seek(self, position):
        self.generator.playback_position.value = position

    def gain(self, volume):
        gain = 10**(volume/20)
        self.source.gain.value = gain

    def __del__(self):
        self.source.dec_ref()
        self.generator.dec_ref()
        self.buffer.dec_ref()
