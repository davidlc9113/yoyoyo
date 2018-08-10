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
├── lib
│   ├── __init__.py
│   ├── helpers
│   │   ├── api_base.py # 实现get/post等等基础方法的母类
│   │   ├── api_response.py # get/post等等之后返回的响应，可以用body()查看响应内容
│   │   └── debug_helper.py # debug输出小工具
│   └── wallet.py # Wallet的API描述，继承APIBase
├── requirements.txt # 安装依赖 pip install -r requirements.txt
└── tests
    ├── __init__.py
    ├── config
    │   ├── config.yml # 服务器配置文件
    │   └── environment.py # 用来读取上面的config.yml
    ├── conftest.py # 公共测试数据，比如wallet、user等等
    ├── factory
    │   └── users.yml # 测试用户，改成自己用的测试用户
    └── test_wallet.py # wallet的测试用例
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

### 根据csv文件执行csvAPI测试
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
