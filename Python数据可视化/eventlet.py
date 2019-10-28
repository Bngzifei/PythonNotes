import eventlet

evt = eventlet.event.Event()


def baz(b):
    evt.send(b + 1)


_ = eventlet.spawn_n(baz, 3)
evt.wait()


# http://eventlet.net/doc/basic_usage.html
# EOF是一个计算机术语，为End Of File的缩写