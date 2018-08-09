from threading import Thread
from queue import Queue

class Concurrent(object):
  """docstring for Concurrent"""
  def __init__(self):
    super(Concurrent, self).__init__()
    self.queue = Queue()

  def add(self):
    arg = self.queue.get()
    self.method(arg)
    self.queue.task_done()

  def start(self, method, args):
    num = len(args)
    self.method = method
    self.threads = [Thread(target=self.add) for _ in range(num)]
    [self.queue.put(arg) for arg in args]
    [thread.start() for thread in self.threads]
    self.queue.join()
