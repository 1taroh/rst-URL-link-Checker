import os

def list_rst_files(directory):
    rst_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".rst"):
                rst_files.append(os.path.join(root, file))
    return rst_files

directory_path = ".\\rstfiles\\source"  # 検索したいディレクトリのパスを指定
rst_files = list_rst_files(directory_path)

for rst_file in rst_files:
    print(rst_file)