import hashlib
from functools import wraps


def hash_md5(info):
    m = hashlib.md5()
    m.update(info.encode('utf-8'))
    m.update('因为相信所以看见'.encode('utf-8'))
    return m.hexdigest()


def is_none(*args):
    """
    存在空字符串，就返回True
    :param args:
    :return:
    """
    return False if all(args) else True



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
    """
    枚举展示数据列表，并支持用户数据编号返回编号对应的数据，支持编号合法校验
    :param info_list:
    :return:
    """
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


def menu_display(menu_dict):
    """
    展示功能字典，然用户选择使用
    :param menu_dict:
    :return:
    """
    while 1:
        for k, v in menu_dict.items():
            print(f'({k}) {v[0]}', end='\t')

        func_choice = input('\n请输入选择的功能编号(Q退出)：').strip().lower()
        if func_choice == 'q':
            break
        if func_choice not in menu_dict:
            continue
        func = menu_dict.get(func_choice)[1]
        func()


def edit_pwd(your_interface, current_user):
    while 1:
        old_pwd = input('请输入旧密码：').strip()
        new_pwd = input('请设置新密码：').strip()
        re_pwd = input('请确认新密码：').strip()
        if new_pwd != re_pwd:
            print('两次密码输入不一致')
            continue
        flag, msg = your_interface(
            hash_md5(old_pwd), hash_md5(new_pwd), current_user['name'], current_user['role'])
        print(msg)
        if flag:
            break