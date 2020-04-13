import os

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 用户数据库路径
DB_USER_DIR = os.path.join(BASE_DIR, 'db')

INIT_PWD = '123456'