import re

url_regex = re.compile(r'(https?|ftp)://(-\.)?([^\s/?\.#]+\.?)+(/[^\s]*)?$')

try:
    with open('urls.txt', 'r') as f:
        urls = set()
        for line in f:
            url = line.strip()
            if url_regex.match(url):
                urls.add(url)
            else:
                print(f"Invalid URL: {url}")

    with open('unique_urls.txt', 'w') as f:
        f.writelines('\n'.join(urls))
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
