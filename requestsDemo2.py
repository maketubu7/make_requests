#encoding=utf-8
import requests
import json
import exceptions
import urllib2


URL = 'http://api.github.com'
def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    return json.load(json_str)

def request_method():
    # response = requests.get(build_uri("user/emails"),auth=('maketubu7','xy818514'))
    response = requests.get(build_uri("users/maketubu7"))
    print response.json()

def params_request():
    response = requests.get(build_uri('users'),params={'since':11})
    print response.text
    print response.headers
    print response.url

def json_request():
    '''
    修改名称，增加email
    :return:
    '''
    # response = requests.patch(build_uri('user'),auth=('maketubu7','xy818514'),
    #                           json={'name':'maketubu77'})
    response = requests.post(build_uri('user/emails'),auth=('maketubu7','xy818514'),
                               json=['601176930@qq.com'])
    print  response.text
    print  response.request.headers
    print response.request.body
    print  response.status_code

def timeout_request():
    '''异常处理
        无法找到httperror timeout这两种异常
    '''
    try:
        response =requests.get(build_uri('user/emails'),auth=('maketubu7','xy818514'), timeout=2)
        response.raise_for_status()
    except urllib2.HTTPError as e:
        print e.message
    except requests.Timeout as e:
        print e.message
    else:
        print response.text
        print response.status_code

def hard_request():
    from requests import Request, Session
    s = Session()
    headers = {'User-Agent':'fake1.3.4'}
    req = Request('GET', build_uri('user/emails'), auth=('maketubu7','xy818514'),headers=headers)
    prepped = req.prepare()
    print prepped.body
    print prepped.headers
    resp = s.send(prepped,timeout=10)
    print resp.headers
    print resp.status_code
    print resp.text
    print resp.history   #访问历史
    print resp.elapsed
    print resp.content
    print resp.encoding   #编码
    email =  resp.json()
    print email
if __name__ == '__main__':
    # request_method()
    # params_request()
    # json_request()
    # timeout_request()
    hard_request()