import readline, rlcompleter, code, atexit, os
from tests.config.environment import Environment
from lib.helpers.debug_helper import DebugHelper
from lib.helpers.eth import ETH
from lib.helpers.api_base import APIBase
from lib.helpers.api_response import APIResponse

debug = DebugHelper()
env = Environment()
eth = ETH(env.config['eth'])
pp = debug.pp

history_file = os.path.expanduser("~/.python_history")

def save_history(file=history_file):
    readline.write_history_file(file)

if os.path.exists(history_file):
  readline.read_history_file(history_file)
atexit.register(save_history)
debug.on(globals(), locals())
