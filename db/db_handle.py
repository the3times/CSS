import os, pickle
from conf.settings import DB_USER_DIR


def get_all_obj(cls_name):
    obj_list = []
    cls_dir = os.path.join(DB_USER_DIR, cls_name)
    if os.path.exists(cls_dir):
        file_list = os.listdir(cls_dir)
        for file_name in file_list:
            file_path = os.path.join(DB_USER_DIR, cls_name, file_name)
            with open(file_path, 'rb') as f:
                obj_list.append(pickle.load(f))

        return obj_list



def get_obj(obj_name, obj_type):
    file_path = os.path.join(DB_USER_DIR, obj_type, f'{obj_name}.pkl')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)
