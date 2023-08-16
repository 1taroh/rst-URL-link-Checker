import re
import os
import requests
import pandas as pd
import time
import pprint

def get_http_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException as e:
        return f"Error: {e}"
    

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
            url_http_status = get_http_status(link_url)
            embedded_links.append([file_path, link_text, line_number, link_url, url_http_status])

    return embedded_links


def list_rst_files(directory):
    rst_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".rst"):
                rst_files.append(os.path.join(root, file))
    return rst_files


# main -----------------------------------

# directory_path = input()
directory_path = "./test/rstfiles/source/"
rst_file_paths = list_rst_files(directory_path)

print("\nrst files are ..")
print("--------------------------------------------------------------------------")
pprint.pprint(rst_file_paths)
print("--------------------------------------------------------------------------")


embedded_links = []
for rst_file_path in rst_file_paths:
    embedded_links.extend(extract_embedded_links(rst_file_path))

df = pd.DataFrame(embedded_links)
df.columns = ["rst file", "text", "line", "URL", "http status"]

print("The dataframe is ..")
print("--------------------------------------------------------------------------")
print(df)
print("--------------------------------------------------------------------------")

print("Do you want to save this list? y/n")
if(input()=="y"):
    name = time.strftime('%Y%m%d_%H%M%S')
    df.to_csv(name+".csv")