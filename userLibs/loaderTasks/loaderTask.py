from locust.exception import LocustError


class LoaderTask(object):

    def __init__(self):
        raise LocustError("__init__ of super() called. Please implement an init method for your class %s") % self.__class__.__name__

    def on_start(self, args=None, kwargs=None):
        raise LocustError("on_start method not defined for %s, super() called. Please implement an on_start() method") % self.__class__.__name__

    def run(self, args=None, kwargs=None):
        # Extend this class and call on_start() here
        raise LocustError("run method not defined for %s, super() called. Please implement an run() method") % self.__class__.__name__
        # Call finalize() here

    def finalize(self, args=None, kwargs=None):
        raise LocustError("finalize method not defined for %s, super() called. Please implement a finalize() method") % self.__class__.__name__


