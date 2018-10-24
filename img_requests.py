#encoding=utf-8
import requests
from contextlib import closing
def download_img():
    '''下载图片demo'''
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=' \
          '1540372111840&di=75cd63f74ec67305fd42360c4544320a&imgtype=0&src=http%3A' \
          '%2F%2Fimg.mp.sohu.com%2Fupload%2F20180604%2F7bf1028b4a99491abb03eb077f6c1' \
          'c4b_th.jpg'
    response = requests.get(url, headers=headers,stream=True)
    # print response.headers
    # print response.status_code
    # print response.reason
    with open('github.jpg','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
    fd.close()
def download_img_improved():
    #伪造header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    #限定URL
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=' \
          '1540372111840&di=75cd63f74ec67305fd42360c4544320a&imgtype=0&src=http%3A' \
          '%2F%2Fimg.mp.sohu.com%2Fupload%2F20180604%2F7bf1028b4a99491abb03eb077f6c1' \
          'c4b_th.jpg'
    # 打开文件 创建连接  完成后关闭连接
    with closing(requests.get(url, headers=headers,stream=True)) as response:
        with open('github2.jpg', 'wb') as fd:
            #每128写一次
            for chunk in response.iter_content(128):
                fd.write(chunk)
if __name__ == '__main__':
    # download_img()
    download_img_improved()