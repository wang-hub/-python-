# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:40:56 2020

@author: wangwei
"""
#import database
import graph

def wea_com(res,w1='',w2=''):
    attr=['名称', '威力', '射程', '射速', '子弹数', '稳定性']
    
    
    #res=d.ex_sel(attr[1::],table,w1,w2)
    #print(res)
    att=[(i,100) for i in attr][1::]
    nam=[res[0][0],res[1][0]]
    res=[res[i][1::] for i in range(len(res))]
    #print(res)
    p=graph.gra_zhizu(att,res,nam)
    return p