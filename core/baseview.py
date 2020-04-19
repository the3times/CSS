from functools import wraps


class BaseViewer:

    name = None
    role = None
    func_list = []

    def __init__(self):
        self.auto_get_func_menu()

    def auto_get_func_menu(self):
        """
        自动调用功能函数触发装饰器的执行，将功能函数添加到类属性 func_list中
        :return:
        """
        not_this = ['auto_get_func_menu', 'my_func', 'start']
        all_funcs = {k: v for k, v in self.__class__.__dict__.items()
                     if callable(v) and not k.startswith('__') and k not in not_this}
        for func in all_funcs.values():
            func()

    def start(self):
        """
        开始函数，功能菜单显示，供管理员选择
        :return:
        """
        while 1:
            for index, func_name in enumerate(self.func_list, 1):
                print('\t\t\t\t\t\t', index, func_name[0], sep='\t')

            choice = input('>>>(Q退出)：').strip().lower()
            if choice == 'q':
                self.func_list.clear()
                break
            if not choice.isdigit() or int(choice) not in range(1, len(self.func_list) +1):
                print('编号不存在， 请重新输入')
                continue
            func = self.func_list[int(choice) - 1][1]
            func(self)

    @staticmethod
    def my_func(desc):
        """
        装饰器，实现功能函数自动添加到类的func_list中
        :return:
        """
        def wrapper(func):
            @wraps(func)
            def inner(*args, **kwargs):
                BaseViewer.func_list.append((desc, func))
            return inner
        return wrapper

    @staticmethod
    def auth(role):
        """
        装饰器，登录校验
        :return:
        """
        def wrapper(func):
            @wraps(func)
            def inner(*args, **kwargs):
                if BaseViewer.name and BaseViewer.role == role:
                    res = func(*args, **kwargs)
                    return res
                else:
                    print('您未登录或没有该功能的使用权限')
            return inner
        return wrapper

    def login(self, role_interface):
        while 1:
            print('老师登录页面'.center(50, '-'))
            name = input('请输入用户名(Q退出)：').strip().lower()
            if name == 'q':
                break
            pwd = input('请输入密码：').strip()
            if self.is_none(name, pwd):
                print('用户名或密码不能为空')
                continue
            flag, msg = role_interface.login_interface(name, self.hash_md5(pwd))
            print(msg)
            if flag:
                self.name = name
                break