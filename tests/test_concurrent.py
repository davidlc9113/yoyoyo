import pytest, time

def sleep(arg):
  print(arg, time.time())
  time.sleep(3)
  print('done')

def test_sleep(thread):
  print()
  thread.start(sleep, [1,2,3,4,5])
