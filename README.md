# README

## Run test

```bash
pytest -s
```

## Install

```bash
pip install -r requirements.txt
```

## Structure

```bash
.
├── bin/
│   ├── console*
│   └── console.py
├── lib/
│   ├── helpers/
│   │   ├── api_base.py
│   │   ├── api_response.py
│   │   ├── concurrent.py
│   │   ├── debug_helper.py
│   │   └── eth.py
│   ├── __init__.py
│   └── wallet.py # Wallet的API描述，继承APIBase
├── tests/
│   ├── config/
│   │   ├── config.yml # 服务器配置文件
│   │   ├── environment.py
│   │   └── spreadsheet.py
│   ├── factory/
│   ├── spreadsheets/ # 描述API测试的csv文件
│   │   ├── threads/ # 描述并发API测试的csv文件
│   │   │   └── wallet.csv
│   │   └── wallet.csv
│   ├── __init__.py
│   ├── conftest.py # 公共测试数据
│   ├── test_concurrent.py
│   └── test_wallet.py # Wallet的API测试用例
├── README.md
└── requirements.txt
```

## tests/test_wallet.py

### fixture测试数据
```python
@pytest.fixture(scope='module')
def wallet_csv(env):
  return Speadsheet('tests/spreadsheets/wallet.csv')

@pytest.fixture(scope='module')
def csv(env):
  return env.glob('tests/spreadsheets/threads/*.csv')
```

### 根据csv文件执行API测试
```python
def test_all(wallet_csv, wallet):
  wallet_csv.test({ 'wallet': wallet })
```
- wallet_csv定义在上面的fixture测试数据里
- wallet是定义在tests/conftest.py里公共测试数据，这个变量是替换wallet_csv里Instance列里的'wallet'

### 根据多个csv文件并发执行API测试
```python
def test_concurrency(csv, thread, wallet):
  ...
```
- csv定义在上面的fixture测试数据里，返回tests/spreadsheets/threads下面的所有csv文件
