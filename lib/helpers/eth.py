import six, json
from decimal import *
from web3 import Web3, HTTPProvider
from eth_account.messages import defunct_hash_message
from .debug_helper import DebugHelper

class ETH(object):
  """docstring for ETH"""
  def __init__(self, params=None):
    super(ETH, self).__init__()
    self.debug_helper = DebugHelper()
    params = params or { 'network': 'kovan' }
    for key, value in params.items():
      if key == 'network':
        if (isinstance(value, six.string_types) and
            value in self.__networks()):
          network = self.__networks()[value]
        else:
          network = value
        self.web3 = Web3(HTTPProvider(
          network['uri'], request_kwargs=network['request_kwargs']))
        self.eth = self.web3.eth
      elif key == 'contract':
        address = value['address']
        self.abi = json.load(open(value['file'], 'r'))
        Contract = self.eth.contract(abi=self.abi)
        self.contract = Contract(address=address)
    self.account = None

  def __networks(self):
    return { 'kovan': { 'uri': 'https://kovan.infura.io:443',
                        'request_kwargs': { 'timeout': 30 } } }

  def balance(self, address):
    return self.eth.getBalance(address)

  def to_hex(self, value):
    return Web3.toHex(value)

  def to_wei(self, _wei, value):
    return int(value*10**int(_wei))

  def sign_hash(self, key, types, values):
    sha3 = Web3.soliditySha3(types, values)
    signed = self.eth.account.signHash(defunct_hash_message(sha3), key)
    _hash = { 'hash': self.to_hex(sha3) }
    for e in ['r', 's', 'v']:
      _hash[e] = self.to_hex(signed[e])
    return _hash

  def create_account(self, key):
    self._account = self.eth.account.privateKeyToAccount(key)
    self.account = {
      'address': self._account._key_obj.public_key.to_checksum_address(),
      'public_key': ''
    }
    return self.account

  def account_public_key(self):
    return str(self.account._key_obj.public_key)[2:-1]
