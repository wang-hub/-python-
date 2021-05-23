# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:09:52 2020

@author: wangwei
"""

from bs4 import Tag
from bs4 import BeautifulSoup 

def form_to_html(mc,is_one,s='/jcvsjc'):
    soup = BeautifulSoup()  
    _f=soup.new_tag('form',
                   #action="/jcvsjc",
                   action=s,
                   method="post",
                   enctype="multipart/form-data",
                   id="form1")
    sel = Tag(#builder=soup.builder, 
               name='select', 
               attrs={'name':'username'})
    #sel=res.newag('select',name='username')  
    for i in mc:
        print(i[0])
        op=soup.new_tag('option',value=str(i[0]))
        op.append(str(i[0]))
        sel.append(op)
    _f.append(sel)
    if is_one!=1:
        sel = Tag(#builder=soup.builder, 
                name='select', 
                attrs={'name':'password'})
        #sel=res.newag('select',name='username')
        for i in mc:
            op=soup.new_tag('option',value=str(i[0]))
            op.append(str(i[0]))
            sel.append(op)
    inpu=soup.new_tag('input',type='submit',value='提交')
    _f.append(sel)
    _f.append(inpu)
    #print(_f)
    return _f

if __name__=='__main__':
    pass
    #form_to_html([1],2)