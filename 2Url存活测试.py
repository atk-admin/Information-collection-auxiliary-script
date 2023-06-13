import threading
import queue
import requests

# 读取 URL 文件，并存储到队列中
def read_urls(filename, url_queue):
    with open(filename, 'r',encoding='utf-8') as f:
        for line in f:
            url = line.strip()
            url_queue.put(url)

# 存活检测线程函数
def check_url(url_queue, success_file, failure_file):
    while True:
        try:
            url = url_queue.get(timeout=1)
        except queue.Empty:
            break

        try:
            response = requests.head(url, timeout=10)
            if response.status_code == 200:
                print(f"{url} is alive.")
                success_file.write(url + '\n')
            else:
                print(f"{url} returned status code {response.status_code}.")
                failure_file.write(url + '\n')
        except requests.exceptions.RequestException as e:
            print(f"{url} failed: {e}")
            failure_file.write(url + '\n')

# 主程序
def main():
    num_threads = 100
    url_queue = queue.Queue()

    # 打开输出文件
    with open('success.txt', 'w') as success_file, \
         open('failure.txt', 'w') as failure_file:

        # 读取 URL 文件，并存储到队列中
        read_urls('unique_urls.txt', url_queue)

        # 创建线程池，并启动检测线程
        threads = []
        for i in range(num_threads):
            t = threading.Thread(target=check_url,
                                 args=(url_queue, success_file, failure_file))
            threads.append(t)
            t.start()

        # 等待所有线程结束
        for t in threads:
            t.join()

if __name__ == '__main__':
    main()
