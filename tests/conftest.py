import pytest
from tests.config.environment import Environment
from lib.wallet import Wallet, APIResponse

@pytest.fixture(scope='session')
def env():
  return Environment()

@pytest.fixture(scope='session')
def wallet(env):
  return Wallet(env.config)

@pytest.fixture(scope='session')
def ok():
  return APIResponse('ok')

@pytest.fixture(scope='session')
def users(env):
    return env.users()

@pytest.fixture(scope='session')
def user(users):
    return users[0]
