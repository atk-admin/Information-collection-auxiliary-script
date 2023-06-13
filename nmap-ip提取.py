import re


# 打开文件并读取文本内容
with open('酒店C段.txt', 'r') as file:
    text = file.read()

def extract_ip_addresses(text):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = re.findall(ip_pattern, text)
    return ip_addresses


# 提取IP地址
ip_addresses = extract_ip_addresses(text)

# 打印提取到的IP地址
for ip in ip_addresses:
    print(ip)
    
with open('ip_addresses.txt', 'w') as file:
    for ip in ip_addresses:
        file.write(ip + '\n')
