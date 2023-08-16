import requests

def get_http_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException as e:
        return f"Error: {e}"

# url_to_check = "https://google.com"  # 調べたいURLをここに設定
# url_to_check = "https://mikamika.io"  # 調べたいURLをここに設定
url_to_check = "https://github.com/1taroh/rst-URL-link-Checkeraaaa"  # 調べたいURLをここに設定

http_status = get_http_status(url_to_check)

print(f"HTTP Status Code for {url_to_check}: {http_status}")