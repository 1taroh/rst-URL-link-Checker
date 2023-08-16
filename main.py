import re
import os
import requests
import pandas as pd
import time

def get_http_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException as e:
        return f"Error: {e}"
    

def extract_embedded_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 正規表現パターンを定義
    link_pattern = re.compile(r'`([^`]+) <([^`]+)>`_')

    # マッチする全てのリンクを抽出
    matches = link_pattern.findall(content)

    return matches


def list_rst_files(directory):
    rst_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".rst"):
                rst_files.append(os.path.join(root, file))
    return rst_files

