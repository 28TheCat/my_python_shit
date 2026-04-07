import os

import config

import config_data as config
import hashlib


def check_md5(md5_str: str):
    if not os.path.exists(config.md5_path):
        print("MD5 file not exists")
        open(config.md5_path, 'w', encoding='utf-8').close()
        return False  # 表示这个md5没有处理过
    else:
        for line in open(config.md5_path, 'r', encoding='utf-8'):
            line = line.strip()  # 处理空格
            if line == md5_str:
                return True  # 表示这个行存在
        return False


def save_md5(md5_str: str):
    with open(config.md5_path, 'a', encoding='utf-8') as f:
        f.write(md5_str + '\n')


def get_string_md5(input_str: str, encoding='utf-8'):
    str_bytes = input_str.encode(encoding=encoding)
    md5_obj = hashlib.md5()  # 得到md5对象
    md5_obj.update(str_bytes)
    md5_str = md5_obj.hexdigest()  # 得到md5的十六进制字符串
    return md5_str


class KnowledgeBaseService(object):
    def __init__(self):
        self.spliter = None
        self.chroma = None

    # 将字符串向量化，存入向量数据库中
    def upload_by_str(self, data, filename):
        pass

if __name__ == '__main__':
    r1 = get_string_md5("data.encode('utf-8')")
    r2 = get_string_md5("data.encode('utf-8')")
    r3 = get_string_md5("data.encode('utf-8')11")
    print(r1)
    print(r2)
    print(r3)
