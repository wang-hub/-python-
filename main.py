# -*- coding: utf-8 -*-
"""
Created on Sun May 24 12:38:34 2020

@author: wangwei
"""

import crawler
from database import database
import com_wea
from brid_to_html import brid_to_html
from gra_to_html import graph_to_html
from plt_to_html import plt_to_html
from all_to_html import all_to_html
from form_to_html import form_to_html
from bs4 import Tag
from bs4 import BeautifulSoup as soup
import jcVSjc
import jcVSmp
import mpVSmp

url = 'https://gp.qq.com/zlkdatasys/data_zlk_hpjywqzlk.json'
db='hpjy'
#武器表
#存放武器
table1='武器总表'
attr1=['名字','特点','优点','缺点','图片']
table2='武器数据表'
attr2=['名字','威力', '射程', '射速', '子弹', '稳定']
table3='武器满配数据表'
attr3=['名字','威力_满配', '射程_满配', '射速_满配', '子弹_满配', '稳定_满配']
table4='武器配件表'
attr4=['名字','配件1','配件2','配件3','配件4','配件5']
table=[table1,table2,table3,table4]
attr=[attr1,attr2,attr3,attr4]
    
def cra_and_db():
    #爬取武器并存入数据库指定表
    html = crawler.get_html_text(url)
    wea=crawler.parse_wuqi_page(html)
    wea=crawler.get_weapon_img(wea)
    #连接数据库
    d=database(db)
    #建表
    for i in range(len(table)):
        attr_type=[]
        if i==0 :
            #默认20个char，可能存不下图片路径或者文字描述
            [attr_type.append('char(200)') for j in range(len(attr[i]))]
        print(attr_type)
        d.ex_cre_table(table=table[i],attr=attr[i],attr_type=attr_type,pri='名字')
    #插入
    for i in wea:
        for a in range(len(attr)-1):  #插入表,配件表单独处理
            data=[]
            data.append(i)
            for j in attr[a][1:]:   #除了名字属性
                #print(j)
                if j=='图片':
                    #图片存原始图片路径
                    data.append(wea[i][j]['原始'])
                else:
                    if(len(wea[i][j])>0):
                        data.append(wea[i][j])
                    else:
                        data.append('暂无')
            print(data)
            d.ex_ins(data,table[a])
        #处理配件表
        data=[]
        data.append(i)
        pei=wea[i]['图片']['配件']
        num=len(pei)
        for n in pei:
            data.append(n)
        for n in range(5-num):
            data.append('暂无')
        #print(data)
        d.ex_ins(data,table[3])
    del d

def jc_vs_mp(w='AKM'):
    d=database(db)
    lis=[]
    mc=d.ex_sel(['名字'],table1)
    _f=form_to_html(mc,1,'jcvsmp')
    lis.append(_f)
    res_jc=d.ex_sel(attr2,table2,w)
    res_mp=d.ex_sel(attr3,table3,w)
    if len(res_jc)!=0 and len(res_mp)!=0:
        p=com_wea.wea_com((res_jc[0],res_mp[0]),w,w)
        lis.append(plt_to_html(p))
    #把配件图片添加进html
    res=d.ex_sel(['图片'],table1,w)
    for img in res:
        img_dir=img[0]+'/../../配件'
        #print(img_dir)
        lis.append(graph_to_html(img_dir))
    h=jcVSmp.all_to_html(lis)
    #print(h)
    del d
    return h

def jc_vs_jc(w1='AKM',w2='M416'):
    lis=[]
    d=database(db)
    mc=d.ex_sel(['名字'],table1)
    _f=form_to_html(mc,2,'/jcvsjc')
    lis.append(_f)
    res=d.ex_sel(w1=w1,w2=w2,att=attr2,table=table2)
    if len(res)>1:
        p=com_wea.wea_com(res,w1,w2)
        lis.append(plt_to_html(p))
    #输出两者原始图片
    res=d.ex_sel(['图片'],table1,w1,w2)
    for img in res:
        img_dir=img[0]+'/..'
        lis.append(graph_to_html(img_dir))
    res=jcVSjc.all_to_html(lis)
    del d
    return res

def mp_vs_mp(w1='AKM',w2='M416'):
    lis=[]
    d=database(db)
    mc=d.ex_sel(['名字'],table1)
    _f=form_to_html(mc,2,'/mpvsmp')
    lis.append(_f)
    res=d.ex_sel(w1=w1,w2=w2,att=attr3,table=table3)
    if len(res)>1:
        p=com_wea.wea_com(res,w1,w2)
        lis.append(plt_to_html(p))
    #输出两者皮肤图片
    res=d.ex_sel(['图片'],table1,w1,w2)
    for img in res:
        img_dir=img[0]+'/../../皮肤'
        lis.append(graph_to_html(img_dir))
    res=mpVSmp.all_to_html(lis)
    #print(res)
    del d
    return res
    
def html_first():
    lis=[]
    d=database(db)
    #输出所有表信息
    for i in range(len(attr)):
        res=d.ex_sel(attr[i],table[i])
        tex=[tuple(attr[i])]
        for r in res:
            tex.append(r)
        #res.append((attr[i]))
        #print(tex)
        lis.append(brid_to_html(tex,table[i]))
    res=all_to_html(lis)
    del d
    return res

if __name__=='__main__':
   cra_and_db()
   #jc_vs_jc('AKM','野牛冲锋枪')
   #jc_vs_mp('AWM')
   #mp_vs_mp('M416','M416')
   html_first()
   pass

'''
class get_html:
    url = 'https://gp.qq.com/zlkdatasys/data_zlk_hpjywqzlk.json'
    db='hpjy'
    #武器表
    #存放武器
    table1='武器总表'
    attr1=['名字','特点','优点','缺点','图片']
    table2='武器数据表'
    attr2=['名字','威力', '射程', '射速', '子弹', '稳定']
    table3='武器满配数据表'
    attr3=['名字','威力_满配', '射程_满配', '射速_满配', '子弹_满配', '稳定_满配']
    table4='武器配件表'
    attr4=['名字','配件1','配件2','配件3','配件4','配件5']
    table=[table1,table2,table3,table4]
    attr=[attr1,attr2,attr3,attr4]
    
    def cra_and_db(self):
        #爬取武器并存入数据库指定表
        html = crawler.get_html_text(self.url)
        wea=crawler.parse_wuqi_page(html)
        wea=crawler.get_weapon_img(wea)
        #连接数据库
        d=database(db)
        #建表
        for i in range(len(self.table)):
            attr_type=[]
            if i==0 :
                #默认20个char，可能存不下图片路径或者文字描述
                [attr_type.append('char(200)') for j in range(len(self.attr[i]))]
            print(attr_type)
            d.ex_cre_table(table=self.table[i],attr=self.attr[i],attr_type=attr_type,pri='名字')
        #插入
        for i in wea:
            for a in range(len(self.attr)-1):  #插入表,配件表单独处理
                data=[]
                data.append(i)
                for j in self.attr[a][1:]:   #除了名字属性
                    #print(j)
                    if j=='图片':
                        #图片存原始图片路径
                        data.append(wea[i][j]['原始'])
                    else:
                        if(len(wea[i][j])>0):
                            data.append(wea[i][j])
                        else:
                            data.append('暂无')
                print(data)
                d.ex_ins(data,self.table[a])
            #处理配件表
            data=[]
            data.append(i)
            pei=wea[i]['图片']['配件']
            num=len(pei)
            for n in pei:
                data.append(n)
            for n in range(5-num):
                data.append('暂无')
            print(data)
            d.ex_ins(data,self.table[3])
        del d

def jc_vs_mp(self,w):
    d=database(self.db)
    lis=[]
    res_jc=d.ex_sel(self.attr2,self.table2,w)
    res_mp=d.ex_sel(self.att3,self.table3,w)
    p=com_wea.wea_com((res_jc[0],res_mp[0]),w,w)
    lis.append(plt_to_html(p))
    #把配件图片添加进html
    res=d.ex_sel(['图片'],self.table1,w)
    for img in res:
        img_dir=img[0]+'/../../配件'
        #print(img_dir)
        lis.append(graph_to_html(img_dir))
    h=jcVSmp.all_to_html(lis)
    del d
    return h

def jc_vs_jc(self,w1,w2):
    lis=[]
    d=database(self.db)
    res=d.ex_sel(w1=w1,w2=w2,att=self.attr2,table=self.table2)
    p=com_wea.wea_com(res,w1,w2)
    lis.append(plt_to_html(p))
    #输出两者原始图片
    res=d.ex_sel(['图片'],self.table1,w1,w2)
    for img in res:
        img_dir=img[0]+'/..'
        lis.append(graph_to_html(img_dir))
    res=jcVSjc.all_to_html(lis)
    del d
    return res

def mp_vs_mp(self,w1,w2):
    lis=[]
    d=database(self.db)
    res=d.ex_sel(w1=w1,w2=w2,att=self.attr3,table=self.table3)
    p=com_wea.wea_com(res,w1,w2)
    lis.append(plt_to_html(p))
    #输出两者皮肤图片
    res=d.ex_sel(['图片'],self.table1,w1,w2)
    for img in res:
        img_dir=img[0]+'/../../皮肤'
        lis.append(graph_to_html(img_dir))
    res=mpVSmp.all_to_html(lis)
    del d
    return res
   
def html_first(self):
    lis=[]
    d=database(self.db)
    #输出所有表信息
    for i in range(len(self.attr)):
        res=d.ex_sel(self.attr[i],self.table[i])
        lis.append(brid_to_html(res,self.table[i]))
    
    #输出所有枪的皮肤
    #res=d.ex_sel(['图片'],table1)
    #for img in res:
        #原始图片文件的父文件夹下含有皮肤图片文件夹
     #   img_dir=img[0]+'/../../皮肤'
        #print(img_dir)
     #   lis.append(graph_to_html(img_dir))
    res=all_to_html(lis)
    del d
    return res
'''

