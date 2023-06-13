# 定义要分割的文件名和要保存的路径
input_file = 'success.txt'
output_dirs = ['C:\\Users\\admin\Desktop\\5-漏洞扫描\\1-Xray\\xray1\\', 'C:\\Users\\admin\Desktop\\5-漏洞扫描\\1-Xray\\xray2\\', 'C:\\Users\\admin\Desktop\\5-漏洞扫描\\1-Xray\\xray3\\', 'C:\\Users\\admin\Desktop\\5-漏洞扫描\\1-Xray\\xray4\\']

# 打开要分割的文本文件，并读取其内容
with open(input_file, 'r') as f:
    content = f.readlines()

# 计算每个文件的大小，将URL的数量分为4等份
urls_per_file = len(content) // 4

# 将内容分割成4个部分
parts = []
start = 0
for i in range(4):
    end = start + urls_per_file
    if i == 3:
        end = len(content)
    parts.append(content[start:end])
    start = end

# 创建4个文件并将相应的内容写入文件
for i, part in enumerate(parts):
    output_file = output_dirs[i] + 'urls_part{}.txt'.format(i+1)
    with open(output_file, 'w') as f:
        f.writelines(part)
