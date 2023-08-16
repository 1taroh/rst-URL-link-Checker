import os

def list_rst_files(directory):
    rst_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".rst"):
                rst_files.append(os.path.join(root, file))
    return rst_files

directory_path = ".\\rstfiles\\source"  # 検索したいディレクトリのパスを指定
rst_file_paths = list_rst_files(directory_path)

for rst_file_path in rst_file_paths:
    print(rst_file_path)