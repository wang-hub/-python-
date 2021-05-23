# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:39:23 2020

@author: wangwei
"""

import file_util
import browser_util
import os
from bs4 import BeautifulSoup
import base64
import os
from io import BytesIO
import re
HTML_FILE_NAME = 'graph_show.html'

CSS = '''
th {
        background-color: rgb(81, 130, 187);
        color: #fff;
        border-bottom-width: 0;
    }
    td {
        color: #000;
    }
    tr, th {
        border-width: 1px;
        border-style: solid;
        border-color: rgb(81, 130, 187);
    }
    td, th {
        padding: 5px 10px;
        font-size: 12px;
        font-family: Verdana;
        font-weight: bold;
    }
    table {
        border-width: 1px;
        border-collapse: collapse;
        float: left;
        margin: 10px;
    }
'''

HTML = """
<html><head><meta charset="utf-8"><title>paixiaoxing</title><style>%s</style></head><body></body></html>
""" % CSS

def graph_to_html(grp_dir):
    #r=re.compile(r'.*?_img/(.*?).jpg') #提取名字
    #r=re.compile(r'.*?/(.*?).jpg') #提取名字
    img_list=file_util.get_suffixfiles_fulloppath(grp_dir,'.jpg')
    soup = BeautifulSoup(HTML, 'lxml')
    #添加表名
    table1 = soup.new_tag(name='table')
    # 标题行
    tr_head = soup.new_tag(name='tr')
    td_head = soup.new_tag(name='th', colspan="3")
    td_head.append( '图片')
    tr_head.append(td_head)
    table1.append(tr_head)
    # field行
    #i=1
    tr_field = soup.new_tag(name='tr')
    for field in img_list: 
        td=soup.new_tag(name='td')
        #s='/../'+field
        #print(s)
        with open(field,'rb') as f:
            data=f.read()
            imb = base64.b64encode(data)  
            ims = imb.decode()
            imd = "data:image/png;base64,"+ims
            img=soup.new_tag('img',src="{}".format(imd))
            #img=soup.new_tag('img',src=field)
            #td.append("<img src = '"+'../'+field+"'>")
            td.append(img)
        #print(field)
        tp=soup.new_tag(name='p')
        nu=0
        for i in range(1,len(field)+1):
            if field[-i]=='/':
                nu=-i
                break
        #print(nu,field[nu])
        fi=field[nu+1:-4:1]
        #print(fi)
        tp.append(fi)
        #tp.append(re.search(r,field).group(1))
        td.append(tp)
        tr_field.append(td)
        table1.append(tr_field)
        #if(i%5==0):
         #   table1.append(tr_field)
         #   tr_field = soup.new_tag(name='tr')
        #i+=1
    soup.body.append(table1)
    #result_html = soup.prettify()
    #print(result_html)
    #file_util.write_file_content(HTML_FILE_NAME, result_html)
    #不知道为什么调用不了自己的浏览器
    #full_path = os.path.join(os.getcwd(), HTML_FILE_NAME)
    #browser_util.open_with_default_browser(full_path)
    return table1