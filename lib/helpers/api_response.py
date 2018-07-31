import json
from dateutil import parser, tz
from .debug_helper import DebugHelper

class APIResponse(object):
  """docstring for APIResponse"""
  def __init__(self, raw, debug=False):
    super(APIResponse, self).__init__()
    if raw is 'ok':
      self.body = self.ok_body
      self.code = 200
    else:
      self.raw = raw
      self.code = self.raw.status_code
      self.debug = debug
      self.debug_helper = DebugHelper()
      self.body = self.json_body

  def time(self):
    date = self.raw.headers['Date']
    utc = parser.parse(date)
    local = tz.gettz('Asia/Shanghai')
    return utc.astimezone(local).__str__()

  def items(self):
    return self.body().items()

  def json_body(self):
    if self.raw and self.raw.text:
      _response = json.loads(self.raw.text)
    else:
      _response = self.raw.text
    if self.debug:
      self.debug_helper.output('response', _response, True)
    return _response

  def data(self):
    _body = self.body()
    if 'data' in _body.keys():
      return _body['data']
    else:
      return {}

  def result(self, _filter=None):
    if self.data() and 'result' in self.data().keys():
      _result = self.data()['result']
      if filter:
        return list(filter(_filter, _result))
      else:
        return _result
    else:
      return []

  def ok_body(self):
    return { 'code': 0, 'message': 'Success' }
