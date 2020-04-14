import hashlib
from functools import wraps


def hash_md5(info):
    m = hashlib.md5()
    m.update(info.encode('utf-8'))
    m.update('因为相信所以看见'.encode('utf-8'))
    return m.hexdigest()



def is_none(*args):
    return all(args)



def auth(role):
    from core.current_user import current_user
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if current_user and current_user['role'] == role:
                res = func(*args, **kwargs)
                return res
            else:
                print('您未登录或没有该功能的使用权限')
        return inner
    return wrapper



def select_item(info_list):
    while 1:
        for index, school in enumerate(info_list, 1):
            print(index, school)
        choice = input('请输入选择的编号(Q退出)：').strip().lower()
        if choice == 'q':
            return False, '返回'
        if not choice.isdigit() or int(choice) not in range(1, len(info_list) + 1):
            print('您输入的编号不存在')
            continue
        else:
            return True, info_list[int(choice) - 1]