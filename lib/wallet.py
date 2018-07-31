from .helpers.api_base import APIBase, APIResponse

class Wallet(APIBase):
  """docstring for Wallet"""
  def create(self, params):
    return self.post('/wallets', params, ['name', 'requestPubKey'])

  def read(self, params):
    return self.get("/wallets/%s"%params['id'], params, ['id'])

  def update(self, params):
    return self.patch("/wallets/%s"%params['id'],
      params, ['id'], ['name', 'assets'])
