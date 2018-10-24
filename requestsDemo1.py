#encoding=utf-8
import requests

url_get = 'http://httpbin.org/get'
url_ip = 'http://httpbin.org/ip'

def use_simple_requests():
    response = requests.get(url_ip)
    print '>>>>>>>>header:'
    print response.headers
    print '>>>>>>>>body:'
    print response.text


def use_params_requests():
    # 构建参数请求
    params = {'param1':'hello','param2':'world'}
    #发送请求
    response = requests.get(url_get,params=params)
    # 处理相应打印相关信息
    print '>>>>>>>>header:'
    print response.headers
    print '>>>>>>>>status code'
    print response.status_code
    print response.reason
    print '>>>>>>>>body:'
    print response.json()
    print  response.text


if __name__ == '__main__':
    # print '>>>use simple requests'
    # use_simple_requests()
    print '>>>use_params_requests'
    use_params_requests()