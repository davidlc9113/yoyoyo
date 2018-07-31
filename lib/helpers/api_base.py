import requests, six
from .debug_helper import DebugHelper
from .api_response import APIResponse

class APIBase(object):
  """docstring for APIBase"""
  def __init__(self, params):
    super(APIBase, self).__init__()
    self.debug_helper = DebugHelper()
    attr = ['server', 'debug']
    for e in attr:
      setattr(self, e, params[e])
    self.lang = 'en'

  def full_url(self, path):
    _full_url = self.server + path
    return _full_url

  def full_headers(self, headers):
    if not headers:
      headers = {}
    if 'user-agent' not in headers:
      headers['user-agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '\
        'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1 '\
        'Safari/605.1.15'
    return headers

  def filter_params(self, params, required, optional):
    _params = {}
    for k in params.keys():
      if k in self.show_params('params', None, required, optional):
        _params[k] = params[k]
    return _params

  def dict_params(self, params):
    dict_list = list(map(lambda e: e if isinstance(e, dict) else { e: 'str' },
      params))
    _dict = {}
    for e in dict_list:
      _dict.update(e)
    return _dict

  def show_params(self, tag, path=None, required=None, optional=None):
    if tag is 'path':
      return path
    elif tag is 'required':
      return self.dict_params(required)
    elif tag is 'params':
      if not optional:
        optional = []
      return self.dict_params(required+optional)
    else:
      return ['path', 'required', 'params']

  def get(self, path, params, required, optional=None, headers=None):
    if (isinstance(params, six.string_types) and
        params in self.show_params('tags')):
      return self.show_params(params, path, required, optional)
    _url = self.full_url(path)
    _headers = self.full_headers(headers)
    _params = self.filter_params(params, required, optional)
    if self.debug:
      self.debug_helper.output('get', _url)
      self.debug_helper.output('params', _params)
    response = requests.get(_url, params=_params, headers=_headers)
    return APIResponse(response, self.debug)

  def post(self, path, params, required, optional=None, headers=None):
    if isinstance(params, six.string_types):
      return self.show_params(params, path, required, optional)
    _url = self.full_url(path)
    _headers = self.full_headers(headers)
    _params = self.filter_params(params, required, optional)
    if self.debug:
      self.debug_helper.output('post', _url)
      self.debug_helper.output('payload', _params)
    response = requests.post(_url, data=_params, headers=_headers)
    return APIResponse(response, self.debug)

  def patch(self, path, params, required, optional=None, headers=None):
    if isinstance(params, six.string_types):
      return self.show_params(params, path, required, optional)
    _url = self.full_url(path)
    _headers = self.full_headers(headers)
    _params = self.filter_params(params, required, optional)
    if self.debug:
      self.debug_helper.output('patch', _url)
      self.debug_helper.output('payload', _params)
    response = requests.patch(_url, data=_params, headers=_headers)
    return APIResponse(response, self.debug)
