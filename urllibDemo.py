# encoding=utf-8
import  urllib
import urllib2

url_get = 'http://httpbin.org/get'
url_ip = 'http://httpbin.org/ip'

def use_simple_urllib2():
    response = urllib2.urlopen(url_ip)
    print '>>>>>>>>header:'
    print response.info()
    print '>>>>>>>>body:'
    print ''.join([line for line in response.readlines()])


def use_params_urllib2():

    # 构建参数请求
    params = urllib.urlencode({'param1': 'hello', 'param2': 'world'})
    print 'reuests params:'
    print params
    #发送请求
    response = urllib2.urlopen('?'.join([url_get,'%s'])%params)
    # 打印相关信息
    print '>>>>>>>>header:'
    print response.info()
    print '>>>>>>>>status code'
    print response.getcode()
    print '>>>>>>>>body:'
    print ''.join([line for line in response.readlines()])


if __name__ == '__main__':
    # print '>>>use simple urllib'
    # use_simple_urllib2()
    print '>>>use_params_urllib2'
    use_params_urllib2()