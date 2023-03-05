from canvas import root, frame


def clear_screen():
    frame.delete('all')


def clear_all(el):
    el.destroy()