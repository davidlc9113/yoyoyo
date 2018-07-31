import readline, rlcompleter, code, pprint, six, json

class DebugHelper(object):
  """docstring for DebugHelper"""
  def __init__(self):
    super(DebugHelper, self).__init__()
    self.pp = pprint.pprint

  def on(self, _globals, _locals):
    context = _globals.copy()
    context.update(_locals)
    readline.set_completer(rlcompleter.Completer(context).complete)
    readline.parse_and_bind("tab: complete")
    shell = code.InteractiveConsole(context)
    shell.interact()

  def output(self, title, text, newline=False):
    print('')
    if (isinstance(title, six.string_types)):
      print(title.upper())
    else:
      print(title)
    if isinstance(text, dict) or isinstance(text, list):
      print(json.dumps(text, indent=2, sort_keys=True))
    else:
      print(text)
    if newline:
      print('')
