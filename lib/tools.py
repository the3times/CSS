import hashlib
from functools import wraps


def auth(func):
    import core.login_user

    @wraps(func)
    def inner(*args, **kwargs):
        if core.login_user.login_user:
            res = func(*args, **kwargs)
            return res
        else:
            print('请您先登陆好吧')
    return inner



def hash_md5(info):
    m = hashlib.md5()
    m.update(info.encode('utf-8'))
    m.update('因为相信所以看见'.encode('utf-8'))
    return m.hexdigest()


