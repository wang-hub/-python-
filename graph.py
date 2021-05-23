# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:03:06 2020

@author: wangwei
"""
import matplotlib.pyplot as plt
import numpy as np
def gra_zhizu(attr=[],val=[],nam=[]):
    #attr对比属性，传入形式attr[(name,max),('a',100),('b',100)]
    '''
    schema = [ 
    #("名称", 100),
    ("威力", 100),
    ("射程", 100),
    ("射速", 100),
    ("子弹数", 100), 
    ("稳定性", 100)
    ]
    '''
    #v1 = [[48, 60, 60, 30, 34]]
    #v2 = [[41, 55, 57, 30, 32]]
    
    
    # 拆分attr到标签labs与总分full_marks
    labs = []
    full_marks = []
    for value in attr:
        labs.append(value[0])
        full_marks.append(value[1])
    
    
    # v1,v2进行归一处里
    Y = np.vstack((val))
    val=[list(map(int,Y[i])) for i in range(len(Y))] 
    Y = np.vstack((val))   
    
    #print('labs = {}'.format(labs))
    #print('Y = {}'.format(Y))
    
    
    # 获取 r 与 theta
    N = len(labs)
    #r = np.arange(N) 
    theta = np.linspace(0, 360, N, endpoint=False) 
    #print("theta:",theta)
    
    # 调整角度使得正中在垂直线上
    #adj_angle = theta[-1] + 90 - 360
    adj_angle=90-theta[1]
    theta += adj_angle
    
    # 将角度转化为单位弧度
    X_ticks = np.radians(theta) # x轴标签所在的位置
    
    # 首尾相连
    X = np.append(X_ticks,X_ticks[0])
    Y = np.hstack((Y, Y[:,0].reshape(2,1)))
    
    #print('theta = {}, \nX = {}, \nY={}'.format(theta, X.round(4), Y.round(2)))
    
    fig, ax = plt.subplots(figsize=(5, 5),
                           subplot_kw=dict(projection='polar'))
    #print('ax:',ax)
    #print('fig',fig)
    
    # 画图
    ax.plot(X, Y[0], marker='.',color='b',linewidth=0.5)
    for i in range(len(X)):
        plt.text(X[i], Y[0][i], Y[0][i], color='b',size = 10, alpha = 0.5)
    ax.plot(X, Y[1], marker='.',color='r',linewidth=0.5)
    for i in range(len(X)):
        plt.text(X[i], Y[1][i], Y[1][i], color='r',size = 10)
    ax.set_xticks(X)
    
    # 设置背景坐标系
    ax.set_xticklabels(labs, fontproperties = 'SimHei', fontsize = 'large') # 设置标签
    ax.set_yticklabels([]) 
    ax.spines['polar'].set_visible(False) # 将轴隐藏
    ax.grid(axis='y') # 只有y轴设置grid
    
    
    # 设置X轴的grid
    n_grids = np.linspace(0,100, 6, endpoint=True) # grid的网格数
    #print('n_grids',n_grids)
    grids = [[i] * (len(X)) for i in n_grids] #grids的半径
    
    for i, grid in enumerate(grids): # 给grid 填充间隔色
        #print(i,grid)
        ax.plot(X, grid, color='grey', linewidth=0.5)
        if (i>0) & (i % 2 == 0):
            ax.fill_between(X, grids[i], grids[i-1], color='grey', alpha=0.1) 
    
    plt.text(100,120,nam[0],color='b',fontproperties = 'SimHei')
    plt.text(100,130,nam[1],color='r',fontproperties = 'SimHei')
    #plt.show()
    return plt
    
    
