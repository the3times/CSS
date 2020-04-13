import os, pickle
from conf.settings import DB_USER_DIR



def get_obj(cls, name):
    file_path = os.path.join(DB_USER_DIR, cls.__name__, name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)



def save_obj(obj):
    cls_name = obj.__class__.__name__
    file_dir = os.path.join(DB_USER_DIR, cls_name)
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    file_path = os.path.join(file_dir, obj.name)
    with open(file_path, 'wb') as f:
        pickle.dump(obj, f)
