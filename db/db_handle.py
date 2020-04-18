import os, pickle
from conf import settings


def get_obj(cls, obj_name):
    """
    获取对象
    :param cls: 类
    :param obj_name: 对象名字
    :return: 对象 or None
    """
    cls_name = cls.__name__
    file_path = os.path.join(settings.DB_USER_DIR, cls_name, obj_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)


def save_obj(obj):
    """
    保存对象（覆盖重写的方式）
    :param obj:
    :return:
    """
    cls_name = obj.__class__.__name__
    folder = os.path.join(settings.DB_USER_DIR, cls_name)
    if not os.path.exists(folder):
        os.mkdir(folder)
    file_path = os.path.join(folder, obj.name)
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)

