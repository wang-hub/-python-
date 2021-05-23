ng# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:35:58 2020

@author: wangwei
"""

from tornado.web import Application,RequestHandler,url
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import json
import main
import jcVSjc
import jcVSmp
import mpVSmp
import tornado.options
import tornado.websocket
import os


'''
#定义变量，这些也可以写入配置文件
tornado.options.define(
        name='port',
        default=9876,
        type=int,
        help='this is help',  #选项变量的提示信息
        )
tornado.options.define(name='port',type=int,default=9876)
'''
#定义处理类型
class IndexHandler(RequestHandler):
    #添加一个get请求方式的方法
    #g=main.gethtml()
    def get(self):
        
        h=main.html_first()
        tab=h.new_tag(name='table')
        tr_head = h.new_tag(name='tr')
        td_head = h.new_tag(name='th', colspan="3")
        td_head.append( '功能展示')
        tr_head.append(td_head)
        tab.append(tr_head)
        
        tr=h.new_tag(name='tr')
        td=h.new_tag(name='td')
        a=h.new_tag('a',href=self.reverse_url("jcvsjc"))
        a.append("武器VS武器")
        td.append(a)
        tr.append(td)
        tab.append(tr)
        #tab.append('<br>')
        tr=h.new_tag(name='tr')
        td=h.new_tag(name='td')
        a=h.new_tag('a',href=self.reverse_url("jcvsmp"))
        a.append("裸装VS满配")
        td.append(a)
        tr.append(td)
        tab.append(tr)
        #tab.append('<br>')
        tr=h.new_tag(name='tr')
        td=h.new_tag(name='td')
        a=h.new_tag('a',href=self.reverse_url("mpvsmp"))
        a.append("满配VS满配")
        td.append(a)
        tr.append(td)
        tab.append(tr)
        h.append(tab)
        self.write(str(h))
        #self.render('show.html')
        #print (self.request)
        
        #json_str={"username":"admin","password":"123123"}
        #self.write(json.dumps(json_str))
        #self.write("<a href='"+self.reverse_url("login")+"'>用户登陆</a>")
    '''
    def post(self,*args,**kwargs):
        username=self.get_argument('username')
        password=self.get_argument('password')
        print(username,password)
        self.write('提交成功')
        self.write(str(main.m(username,password)))
    '''    
        
class jvjHandler(RequestHandler):
        
    def get(self):
        #self.write('欢迎使用武器对比功能')
        #h=jcVSjc.all_to_html([])
        h=main.jc_vs_jc()
        a=h.new_tag('a',href=self.reverse_url("first"))
        a.append("返回数据页")
        h.append(a)
        self.write(str(h))
    def post(self,*args,**kwargs):
        username=self.get_argument('username')
        password=self.get_argument('password')
        print(username,password)
        h=main.jc_vs_jc(username,password)
        a=h.new_tag('a',href=self.reverse_url("first"))
        a.append("返回数据页")
        h.append(a)
        self.write(str(h))
        
class jvmHandler(RequestHandler):
    def get(self):
        #self.write('欢迎使用武器配件展示')
        #h=jcVSmp.all_to_html('M762')
        h=main.jc_vs_mp()
        a=h.new_tag('a',href=self.reverse_url("first"))
        a.append("返回数据页")
        h.append(a)
        self.write(str(h))
    def post(self,*args,**kwargs):
        username=self.get_argument('username')
        print(username)
        h=main.jc_vs_mp(username)
        a=h.new_tag('a',href=self.reverse_url("first"))
        a.append("返回数据页")
        h.append(a)
        self.write(str(h))

class mvmHandler(RequestHandler):
    def get(self):
        #self.write('欢迎使用武器满配对比功能')
        #h=mpVSmp.all_to_html('AUG','M416')
        h=main.mp_vs_mp()
        a=h.new_tag('a',href=self.reverse_url("first"))
        a.append("返回数据页")
        h.append(a)
        self.write(str(h))
    def post(self,*args,**kwargs):
        username=self.get_argument('username')
        password=self.get_argument('password')
        print(username,password)
        h=main.mp_vs_mp(username,password)
        a=h.new_tag('a',href=self.reverse_url("first"))
        a.append("返回数据页")
        h.append(a)
        self.write(str(h))
   
if __name__=='__main__':
    #创建一个应用对象
    app=tornado.web.Application(
            [
                url(r'/',IndexHandler,name="first"),
                url(r'/jcvsjc',jvjHandler,name="jcvsjc"),
                url(r"/jcvsmp",jvmHandler,name="jcvsmp"),
                url(r"/mpvsmp",mvmHandler,name="mpvsmp")
            ],
            #static_path=os.path.join(os.path.dirname(__file__),"static")
            static_path=os.path.join(os.path.dirname(__file__),"jingying_weapon_img")
            )
    tornado.options.parse_command_line()
    #实例化http服务对象
    http_server=tornado.httpserver.HTTPServer(app) 
    #绑定一个监听端口
    http_server.bind(9876)
    #启动进程
    http_server.start(1)  #不写默认一个进程
    #启动web程序，开始监听端口连接
    tornado.ioloop.IOLoop.current().start()