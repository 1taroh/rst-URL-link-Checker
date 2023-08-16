import re

def extract_embedded_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 正規表現パターンを定義
    link_pattern = re.compile(r'`([^`]+) <([^`]+)>`_')

    # マッチする全てのリンクを抽出
    matches = link_pattern.findall(content)

    return matches

rst_file_path = 'rstfiles/source/index.rst'
embedded_links = extract_embedded_links(rst_file_path)

for link_text, link_url in embedded_links:
    print(f"Link Text: {link_text}")
    print(f"Link URL: {link_url}")
    print("-" * 20)
