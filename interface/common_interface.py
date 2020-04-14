import os
from conf import settings


def get_all_school_list():
    """
    获取所有学校的校名
    :return: 校名列表
    """
    school_folder = os.path.join(settings.DB_USER_DIR, 'School')
    return os.listdir(school_folder)


