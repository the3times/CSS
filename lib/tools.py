import hashlib


class ToolsMixin:
    def is_none(self, *args):
        """
        存在空字符串，就返回True
        :param args:
        :return:
        """
        return False if all(args) else True

    def hash_md5(self, info):
        m = hashlib.md5()
        m.update(info.encode('utf-8'))
        m.update('因为相信所以看见'.encode('utf-8'))
        return m.hexdigest()

    def select_item(self, info_list):
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

    def edit_pwd(self, your_interface):
        while 1:
            old_pwd = input('请输入旧密码：').strip()
            new_pwd = input('请设置新密码：').strip()
            re_pwd = input('请确认新密码：').strip()
            if new_pwd != re_pwd:
                print('两次密码输入不一致')
                continue
            flag, msg = your_interface(self.hash_md5(old_pwd), self.hash_md5(new_pwd), self.name, self.role)
            print(msg)
            break
