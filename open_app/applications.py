from AppOpener import open, close

def open_app(*args):
    for apps in args:
        open(apps)

def close_app(*args):
    for apps in args:
        close(apps)