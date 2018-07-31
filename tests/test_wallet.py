import pytest, ast
from lib.wallet import Wallet, APIResponse
from tests.config.spreadsheet import Speadsheet

@pytest.fixture(scope='module')
def wallet_csv(env):
  return Speadsheet('tests/spreadsheets/wallet.csv')

def test_all(wallet_csv, wallet):
  wallet_csv.test({ 'wallet': wallet })
