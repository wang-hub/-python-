# -*- coding: utf-8 -*-
"""
Created on Mon May 25 18:41:42 2020

@author: wangwei
"""

import file_util
import browser_util
import base64
import os
from io import BytesIO
from bs4 import BeautifulSoup


HTML_FILE_NAME = 'plt_show.html'

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
   
def plt_to_html(plt):
    soup = BeautifulSoup(HTML, 'lxml')
    # figure 保存为二进制文件
    buffer = BytesIO()
    plt.savefig(buffer)  
    #plt.savefig('cmp.png')
    plot_data = buffer.getvalue()
     
    # 图像数据转化为 HTML 格式
    imb = base64.b64encode(plot_data)  
    ims = imb.decode()
    imd = "data:image/png;base64,"+ims
    img=soup.new_tag('img',src="{}".format(imd))    
    #soup.body.append(img)
    #result_html = soup.prettify()
    #print(result_html)
    #file_util.write_file_content(HTML_FILE_NAME, result_html)
    #不知道为什么调用不了自己的浏览器
    #full_path = os.path.join(os.getcwd(), HTML_FILE_NAME)
    #browser_util.open_with_default_browser(full_path)
    return img
    