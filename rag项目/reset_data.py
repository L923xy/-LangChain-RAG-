
import os
import shutil
import config_data as config

def reset_database():
    # 1. 清空 Chroma 向量数据库
    if os.path.exists(config.persist_directory):
        shutil.rmtree(config.persist_directory)
        print("已清空 Chroma 向量数据库")

    # 2. 清空 MD5 去重记录
    if os.path.exists(config.md5_path):
        os.remove(config.md5_path)
        print("已清空 MD5 记录")

    # 3. 清空聊天历史
    history_path = "./chat_history"
    if os.path.exists(history_path):
        shutil.rmtree(history_path)
        print("已清空聊天历史")

    print("\n数据清理完成！")

if __name__ == "__main__":
    confirm = input("确定清空所有知识库和聊天记录吗？(yes/no): ")

    if confirm.lower() == "yes":
        reset_database()
    else:
        print("已取消操作")
