# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:52:13 2020

@author: wangwei
"""
import BeautifulSoup
import os
import sql_parser

HTML = "<html><head><title>PdmShow</title><style>%s</style></head><body></body></html>"% CSS

def sql_to_html(sql_text):
    table_list = sql_parser.get_tables(sql_text)
    soup = BeautifulSoup(HTML, 'lxml')
    # 遍历数据表
    for table in table_list:
        table1 = soup.new_tag(name='table')
        # 标题行
        tr_head = soup.new_tag(name='tr')
        td_head = soup.new_tag(name='th', colspan="3")
        td_head.append(table.name + '(' + table.comment + ')')
        tr_head.append(td_head)
        table1.append(tr_head)
        # field行
        for field in table.fields:
            tr_field = soup.new_tag(name='tr')
            td_name = soup.new_tag(name='td')
            td_name.append(field.name)
            td_type = soup.new_tag(name='td')
            td_type.append(field.type)
            td_comment = soup.new_tag(name='td')
            td_comment.append(field.comment)
            tr_field.append(td_name)
            tr_field.append(td_type)
            tr_field.append(td_comment)
            table1.append(tr_field)
        soup.body.append(table1)
    # 格式化生成
    result_html = soup.prettify()
    # 保存Html到当前文件夹
    file_util.write_file_content(HTML_FILE_NAME, result_html)
    full_path = os.path.join(os.getcwd(), HTML_FILE_NAME)
    # 用浏览器打开生成的Html文件
    system_util.open_with_default_browser(full_path)