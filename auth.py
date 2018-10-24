#encoding=utf-8

import requests


def construct_url(endpoint):
    return  '/'.join(['https://api.github.com',endpoint])

def oauth_demo():
    '''token 认证
    '''
    #token   通过GitHub获取  我们自己直接获取相关权限的token
    # 一般APP  会在请求资源请进行token的获取，然后用token获取资源
    headers = {'Authorization':'token d28eaf9304a0d1fc7808f5aecbf40b2c6333e7e5'}
    response = requests.get(construct_url('user/emails'),headers=headers)
    print response.request.headers
    print response.text
    print response.status_code


from requests.auth import AuthBase
# 创建一个auth信息，传给requests
class GithubAuth(AuthBase):

    def __init__(self,token):
        self.token = token
    def __call__(self, response):
        response.headers['Authorization'] = ' '.join(['token', self.token])
        return response

def oauth_advanced():
    auth = GithubAuth('d28eaf9304a0d1fc7808f5aecbf40b2c6333e7e5')
    response = requests.get(construct_url('user/emails'),auth=auth)

    print response.request.headers
    print response.text
    print response.status_code

# oauth_demo()
oauth_advanced()