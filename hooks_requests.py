#encoding=utf-8
import requests

def get_key_info(response, *agrs, **kwargs):
    '''回调函数,只获取我们响应时间的关键信息
    '''
    print response.headers['Content-Type']
def hooks_requests():
    '''
    事件钩子
    :return:
    '''
    # return text/html
    response1 = requests.get('https://www.baidu.com', hooks=dict(response1=get_key_info))
    # return application/json; charset = utf - 8
    #回调函数接受的参数为 response
    response = requests.get('https://api.github.com', hooks=dict(response=get_key_info))
if __name__ == '__main__':
    hooks_requests()