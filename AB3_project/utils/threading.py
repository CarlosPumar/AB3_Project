import threading


def thread_is_active(name):
    list_thread = threading.enumerate()

    for thread in list_thread:
        if thread.name == name:
            return True

    return False
