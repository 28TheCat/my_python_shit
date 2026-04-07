import datetime
import os
from webbrowser import Chrome
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
import config
from langchain_text_splitters import RecursiveCharacterTextSplitter
from zipp.glob import separate

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
        # 如果文件夹不存在就创建，否则就跳过
        os.makedirs(config.persist_directory, exist_ok=True)
        self.spliter = None
        self.chroma = Chrome(
            collection_name=config.collection_name,
            embedding_function=DashScopeEmbeddings(
                model="text-embedding-v4"
            ),
            persist_directory=config.persist_directory,
        )
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.chunk_size,
            chunk_overlap=config.chunk_overlap,
            length_function=len,
        )  # 文本分割器的对象

    def upload_by_str(self, data: str, filename: str):
        md5_hex = get_string_md5(data)

        # 去重
        if check_md5(md5_hex):
            return "【跳过】内容已经在知识库中"

        # 切分
        if len(data) > config.max_split_char_number:
            knowledge_chunks: list[str] = self.splitter.split_text(data)
        else:
            knowledge_chunks: list[str] = [data]

        # 构造 metadata
        metadata = {
            "source": filename,
            "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "operator": "mmm"
        }

        self.chroma.add_texts(
            texts=knowledge_chunks,
            metadatas=[metadata for _ in range(len(knowledge_chunks))]
        )


        self.chroma.persist()

        # 记录 md5
        save_md5(md5_hex)

        return f"✅ 已入库，共 {len(knowledge_chunks)} 条"


if __name__ == '__main__':
    service=KnowledgeBaseService()
    service.upload_by_str("heildlsjf","testfile")
