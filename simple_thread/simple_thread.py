from threading import Thread


class SimpleThread(Thread):
    """Creates and starts a thread with the given function and parameter"""

    def __init__(self, function, parameters=()):
        if not isinstance(parameters, tuple):
            parameters = (parameters,)
        Thread.__init__(self, target=function, args=parameters)
        self._return = None
        self.start()

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return
