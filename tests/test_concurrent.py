import pytest, time
from lib.helpers.concurrent import Concurrent

def sleep(arg):
  print(arg, time.time())
  time.sleep(3)
  print('done')

@pytest.fixture(scope='module')
def thread():
  return Concurrent(5)

def test_sleep(thread):
  print()
  thread.start(sleep, [1,2,3,4,5])
