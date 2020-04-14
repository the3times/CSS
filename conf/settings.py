import os
from lib.tools import hash_md5

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


#数据库文件夹
DB_USER_DIR = os.path.join(BASE_DIR, 'db')

# 用户初始密码
INIT_PWD = hash_md5('123456')
