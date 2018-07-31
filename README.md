# README

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
