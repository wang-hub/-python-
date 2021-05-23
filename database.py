# -*- coding: utf-8 -*-
"""
Created on Sun May 24 11:30:37 2020

@author: wangwei
"""

import pymysql


class database:
    #连接数据库
    conn=''
    cur=''
    def __init__(self,db):
        self.db = db
        try:
            self.conn = pymysql.Connect(
                    host="127.0.0.1",
                    user="root",
                    password="123456",
                    db=db,
                    port=3306,
                    charset='utf8')
        except Exception as e:
            print("数据库连接失败！%s"%e)
            print("创建数据库："+db)
            try:
                conn = pymysql.Connect(
                        host="127.0.0.1",
                        user="root",
                        password="123456",
                        port=3306,
                        charset='utf8')
                cursor = conn.cursor()
                cursor.execute('create database %s'%db) 
                conn.commit()
                cursor.close()
                conn.close()
                self.conn = pymysql.Connect(
                        host="127.0.0.1",
                        user="root",
                        password="123456",
                        db=db,
                        port=3306,
                        charset='utf8')
                print("创建数据库成功!")
            except Exception as e:    
                print('创建数据库失败!%s'%e)
        else:
            self.cur = self.conn.cursor()
            print('连接数据库成功！')
    #提交并关闭连接
    def __del__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        print('数据库连接关闭')
    #执行sql语句    
    def ex_sql(self,sql):
        try:
            self.cur.execute(sql)
        except Exception as e:
            print('sql语句有问题,%s'%sql)
            print('problem:%s'%e)
        else:
            self.res=self.cur.fetchall()
            return self.res
    #执行创表语句
    def ex_cre_table(self,table='',attr=[],attr_type=[],pri=-1):
        #传入创建表的名字和属性
        if len(attr_type)==0:
            #没传入属性类型，全部char处理
            for i in range(len(attr)):
                attr_type.append('char(50)')
        sql="create table if not exists "+table
        for i in range(len(attr)):
            if i==0:
                sql=sql+"("+str(attr[i])+" "+str(attr_type[i])
            else:
                sql=sql+","+str(attr[i])+' '+str(attr_type[i])
            if i==pri:
                sql=sql+' primary key'
        sql=sql+')'+'default charset=utf8'
        try:
            #因为是不存在才创表，所以不会执行到except，用于调试改动
            self.cur.execute(sql)
            print(table,'创建成功')
        except Exception as e:
            c=input(table+'表已经存在,是否删除重建(y/n):')
            while(True):
                if(c=='y' or c=='Y'):
                    self.cur.execute('drop table '+table)
                    self.ex_cre_table(table,attr,attr_type,pri)
                    break
                elif(c=='n' or c=='N'):
                    break
                else:
                    c=input('输入有误，请检查')
            
    #执行插入语句
    def ex_ins(self,lis=[],table=''):
        #插入内容，表名
        sql = 'insert into '+table+' values '
        for i in range(len(lis)):
            if i==0:
                sql=sql+"('"+str(lis[i])
            else:
                sql=sql+"','"+str(lis[i])
        sql=sql+"')"
        try:                       
            self.cur.execute(sql)
            print("insert successfully!")
        except Exception as e:
            print("insert failed!%s"%e)
    #数据库查找操作        
    def ex_sel(self,att=[],table='',w1='',w2=''):
        sql='select '
        for i in range(len(att)):
            if i==0:
                sql=sql+att[i]
            else:
                sql=sql+','+att[i]
        sql=sql+' from '+table
        if(w1!=''):
            sql=sql+' where '+'名字'+"='"+w1+"'"
            if(w2!=''):
                sql=sql+" or "+'名字'+"='"+w2+"'"
        return self.ex_sql(sql)
'''
db='hpjydb'
table='weapon'
#attr=['名称', '威力', '射程', '射速', '子弹数', '稳定性']
attr=['name','power','gunshot','speed','clip','stability']
attr_type=['char(20)','char(20)','char(20)','char(20)','char(20)','char(20)']
d=database(db)
d.ex_cre_table(table=table,attr=attr,attr_type=attr_type)
'''
