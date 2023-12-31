import re

def extract_embedded_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()

    link_pattern = re.compile(r'`([^`]+) <([^`]+)>`_')

    embedded_links = []

    for line_number, line in enumerate(content, start=1):
        matches = link_pattern.finditer(line)
        for match in matches:
            link_text = match.group(1)
            link_url = match.group(2)
            embedded_links.append([file_path, link_text, link_url, line_number])

    return embedded_links

rst_file_path = 'rstfiles/source/index.rst'
embedded_links = extract_embedded_links(rst_file_path)

print(embedded_links)
#->[['rstfiles/source/index.rst', 'CNN', 'http://cnn.com', 13], ['rstfiles/source/index.rst', 'google', 'http://google.com', 15]]

# for link_text, link_url, line_number in embedded_links:
#     print(f"Link Text: {link_text}")
#     print(f"Link URL: {link_url}")
#     print(f"Line Number: {line_number}")
#     print("-" * 20)
