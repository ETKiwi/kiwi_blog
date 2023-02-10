# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 09:29:03 2023

@author: Kiwi
"""
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np



# 建立資料
def data():
    x = np.random.randint(1, 50, 10) # 10 random data from 1 to 50
    y = np.random.randint(-20, 0, 10) # 10 random data from 1 to 50
    # y = np.random.randn(10) # standard normal distribution random data
    
    return x, y

# 檢視內鍵字體
def font_list():
    for f in font_manager.fontManager.ttflist:
        print(f.name)
        
# 繪圖
def plt_plot(x, y, title = '繪圖'):
    plt_chinese
    # plt.xkcd()
    
    plt.plot(
        x, y, # data
        'r', # color
        alpha = 0.5 # 透明度
        )
    # 圖說明
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()
    
    
def plt_chinese():
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # 顯示中文
    plt.rcParams['axes.unicode_minus'] = False # 顯示負號



x,y  = data()
plt_plot(x, y)















