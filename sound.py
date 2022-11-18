from sound_lib import output, stream


def urlsound(urlname):
    handle = stream.URLStream(url=urlname)
    return handle


def sound(filename):
    handle = stream.FileStream(file=filename)
    return handle
