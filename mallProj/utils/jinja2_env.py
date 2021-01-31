from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse


def jinja2_environment(**option):
    '''确保可以使用模板引擎中的static和url语句'''
    env = Environment(**option)

    # 通过django中的函数来实现相关功能
    env.globals.update({
        'static': staticfiles_storage.url,  # 文件相对路径转绝对路径
        'url': reverse,  # 命名空间转具体url
    })
    return env
