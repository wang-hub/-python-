# -*- coding: utf-8 -*-
"""
Created on Mon May 25 16:06:52 2020

@author: wangwei
"""

import os
import file_util
import browser_util
from bs4 import BeautifulSoup

HTML_FILE_NAME = 'brid_show.html'

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
<html><head><meta charset="utf-8"><title>Paixiaoxing</title><style>%s</style></head><body></body></html>
""" % CSS

def brid_to_html(sql_text,name_table):
    table_list=sql_text
    
    soup = BeautifulSoup(HTML, 'lxml')
    #添加表名
    table1 = soup.new_tag(name='table')
    # 标题行
    tr_head = soup.new_tag(name='tr')
    td_head = soup.new_tag(name='th', colspan="3")
    td_head.append( '(' + name_table + ')')
    tr_head.append(td_head)
    table1.append(tr_head)
    # field行
    for field in table_list:
        tr_field = soup.new_tag(name='tr')
        for i in field:
            td=soup.new_tag(name='td')
            td.append(i)
            tr_field.append(td)
        table1.append(tr_field)
    soup.body.append(table1)
    #result_html = soup.prettify()
    #print(result_html)
    #file_util.write_file_content(HTML_FILE_NAME, result_html)
    #不知道为什么调用不了自己的浏览器
    #full_path = os.path.join(os.getcwd(), HTML_FILE_NAME)
    #browser_util.open_with_default_browser(full_path)
    return table1