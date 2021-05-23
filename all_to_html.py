# -*- coding: utf-8 -*-
"""
Created on Mon May 25 20:05:31 2020

@author: wangwei
"""

import os
import file_util
import browser_util
from bs4 import BeautifulSoup

HTML_FILE_NAME = 'show.html'

CSS = '''
    th {
        background-color: rgb(81, 130, 187);
        color: #fff;
        border-bottom-width: 0;
    }
    td {
        color: rgb(255,0,0);
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
<html><head><meta charset="utf-8"><title>派小星的武器仓库</title><style>%s</style></head><body>
</body></html>
""" % CSS

def all_to_html(lis):
    soup = BeautifulSoup(HTML, 'lxml')
    for i in lis:
        soup.body.append(i)
    return soup
    #result_html = soup.prettify()
    #full_path = os.path.join(os.getcwd(), HTML_FILE_NAME)
    #file_util.write_file_content(HTML_FILE_NAME, result_html)
    #browser_util.open_with_default_browser(full_path)
    #return result_html