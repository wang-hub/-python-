# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:46:11 2020

@author: wangwei
"""

import requests
import os
import json
import re
from file_util import write_file_content

def get_html_text(url):
    """
    获取页面json数据
    :param url:
    :return:
    """
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    parmas = {
        'callback': 'dealCallBack',
        '_': 1566815094736
    }
    try:
        r = requests.get(url, headers=headers, params=parmas, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        result = r.text
        result = result.replace('dealCallBack(', '').replace(')', '')  # 只留下"dealCallBack(……)"中间……这一部分
        result = json.loads(result)
        return result
    except:
        return ''

def parse_page(ilt, html):
    """
    使用re模块，利用正则表达式分析json数据，ilt列表中存储需要的数据
    :param ilt: 
    :param html: 
    :return: 
    """
    try:
        # 将数据转成字符串
        html = str(html)
        # 找到所有的武器名称
        name = []
        namelt = re.findall(r"'mc_94': '.*?'", html)
        for i in range(len(namelt)):
            name_temp = namelt[i].split(': ')[1].strip("'")
            if len(name) < 43 and name_temp not in ['突击步枪', '射手步枪', '狙击枪', '冲锋枪', '霰弹枪', '机枪', '手枪', '近战武器', '其他']:
                if name_temp not in name:
                    name.append(name_temp)
        # 找到武器对应的属性
        lt = re.findall(r"'ldtw_f2': \[.*?\]", html)
        lt = str(lt)
        weililt = re.findall(r"'wl_45': '\d+'", lt)
        shechenglt = re.findall(r"'sc_54': '\d+'", lt)
        shesult = re.findall(r"'ss_d0': '\d+'", lt)
        zidanlt = re.findall(r"'zds_62': '\d+'", lt)
        wendinglt = re.findall(r"'wdx_a7': '\d+'", lt)
        imagelt = re.findall(r"'tp_93': '//.*?'", html)
        # 获取武器的属性值和图片的url
        for i in range(len(name)):
            weili = eval(weililt[i].split(':')[1])
            shecheng = eval(shechenglt[i].split(':')[1])
            shesu = eval(shesult[i].split(':')[1])
            zidan = eval(zidanlt[i].split(':')[1])
            wending = eval(wendinglt[i].split(':')[1])
            image = 'http://' + imagelt[i].split('//')[1].replace("'", "")
            ilt.append([name[i], weili, shecheng, shesu, zidan, wending, image])
    except:
        print('')

'''
def parse_all_page(ilt,html):
    """
    使用re模块，利用正则表达式分析json数据，ilt列表中存储需要的数据
    :param ilt: 
    :param html: 
    :return: 
    """
    try:
        # 将数据转成字符串
        html = str(html)
        # 找到所有的武器名称
        name = []
        namelt = re.findall(r"'mc_94': '.*?'", html)
        for i in range(len(namelt)):
            name_temp = namelt[i].split(': ')[1].strip("'")
            if len(name)<43 and name_temp not in ['突击步枪', '射手步枪', '狙击枪', '冲锋枪', '霰弹枪', '机枪', '手枪', '近战武器', '其他']:
                if name_temp not in name:
                    name.append(name_temp)
        # 找到武器对应的属性
        lt = re.findall(r"'ldtw_f2': \[.*?\]", html)
        lt = str(lt)
        weililt = re.findall(r"'wl_45': '\d+'", lt)
        shechenglt = re.findall(r"'sc_54': '\d+'", lt)
        shesult = re.findall(r"'ss_d0': '\d+'", lt)
        zidanlt = re.findall(r"'zds_62': '\d+'", lt)
        wendinglt = re.findall(r"'wdx_a7': '\d+'", lt)
        imagelt = re.findall(r"'tp_93': '//.*?'", html)
        # 获取武器的属性值和图片的url
        for i in range(len(name)):
            weili = eval(weililt[i].split(':')[1])
            shecheng = eval(shechenglt[i].split(':')[1])
            shesu = eval(shesult[i].split(':')[1])
            zidan = eval(zidanlt[i].split(':')[1])
            wending = eval(wendinglt[i].split(':')[1])
            image = 'http://' + imagelt[i].split('//')[1].replace("'", "")
            ilt.append([name[i], weili, shecheng, shesu, zidan, wending, image])
    except:
        print('')
'''
def parse_wuqi_page(html):
    # try:
        # 将数据转成字符串
        html = str(html)
        # 找到所有的武器名称
        name = []
        namelt = re.findall(r"'mc_94': '.*?'", html)
        for i in range(len(namelt)):
            name_temp = namelt[i].split(': ')[1].strip("'")
            if len(name)<43 and name_temp not in ['突击步枪', '射手步枪', '狙击枪', '冲锋枪', '霰弹枪', '机枪', '手枪', '近战武器', '其他']:
                if name_temp not in name:
                    name.append(name_temp)
        
        
        # 找到武器对应的基础属性
        lt = re.findall(r"'ldtw_f2': \[.*?\]", html)
        lt = str(lt)
        weililt = re.findall(r"'wl_45': '\d+'", lt)
        shechenglt = re.findall(r"'sc_54': '\d+'", lt)
        shesult = re.findall(r"'ss_d0': '\d+'", lt)
        zidanlt = re.findall(r"'zds_62': '\d+'", lt)
        wendinglt = re.findall(r"'wdx_a7': '\d+'", lt)
        
        #找到武器的满配属性
        mp = re.findall(r"'ldt_79': \[.*?\]", html)
        mp = str(mp)
        weilimp = re.findall(r"'wl_45': '\d+'", mp)
        shechengmp = re.findall(r"'sc_54': '\d+'", mp)
        shesump = re.findall(r"'ss_d0': '\d+'", mp)
        zidanmp = re.findall(r"'zds_62': '\d+'", mp)
        wendingmp = re.findall(r"'wdx_a7': '\d+'", mp)
        
        #找到武器的特点
        td = re.findall(r"'jb_f0': '(.*?)'", html)
        
        #找到武器的优点
        yd = re.findall(r"'yd_c6': '(.*?)'", html)
        
        #找到武器的缺点
        qd = re.findall(r"'qd_00': '(.*?)'", html)
        
        
        #找到武器所有原始图片
        imagemp = re.findall(r"'tp_93': '//.*?'", html)
        #找到所有配件图片
        pj = re.findall(r"'pjzh_7a': (.*?)]", html)
        #print(len(pj))
        #print(pj)
        #皮肤
        pf = re.findall(r"'qpfzh_b1': (.*?)]", html)
        #获取武器的属性值和图片的url
        #字典保存
        wea={}
        for i in range(len(name)):
            #基础数据
            w={}
            weili = eval(weililt[i].split(':')[1])
            shecheng = eval(shechenglt[i].split(':')[1])
            shesu = eval(shesult[i].split(':')[1])
            zidan = eval(zidanlt[i].split(':')[1])
            wending = eval(wendinglt[i].split(':')[1])
            w['威力']=weili
            w['射程']=shecheng
            w['射速']=shesu
            w['子弹']=zidan
            w['稳定']=wending
            #满配数据
            weili_mp = eval(weilimp[i].split(':')[1])
            shecheng_mp = eval(shechengmp[i].split(':')[1])
            shesu_mp = eval(shesump[i].split(':')[1])
            zidan_mp = eval(zidanmp[i].split(':')[1])
            wending_mp = eval(wendingmp[i].split(':')[1])
            w['威力_满配']=weili_mp
            w['射程_满配']=shecheng_mp
            w['射速_满配']=shesu_mp
            w['子弹_满配']=zidan_mp
            w['稳定_满配']=wending_mp
            #特点
            w['特点']=td[i]
            #优点
            w['优点']=yd[i]
            #缺点
            w['缺点']=qd[i]
            img={}
            #原始
            img['原始']='http://' + imagemp[i].split('//')[1].replace("'", "")
            #配件
            pj_pic={}
            pj_mc=re.findall(r"'pjmc_2a': '(.*?)'", pj[i])
            pj_tp=re.findall(r"'pjtp_ea': '(.*?)'}", pj[i])
            for j in range(len(pj_mc)):
                pj_pic[pj_mc[j]]='http:' + pj_tp[j]
            img['配件']=pj_pic
            #皮肤
            pf_pic={}
            pf_mc=re.findall(r"'qpfm_f5': '(.*?)'", pf[i])
            pf_tp=re.findall(r"'qpfdt_74': '(.*?)',", pf[i])
            for j in range(len(pf_mc)):
                pf_pic[pf_mc[j]]='http:' + pf_tp[j]
            img['皮肤']=pf_pic
            w['图片']=img
            wea[name[i]]=w
        return wea
            #图片先不处理
            #wea[name[i]]['']='http://' + imagelt[i].split('//')[1].replace("'", "")
            #image = 'http://' + imagelt[i].split('//')[1].replace("'", "")
            #ilt.append([name[i], weili, shecheng, shesu, zidan, wending, image])
     #except Exception as e:
     #   print(e)

    

def parse_peijian_page(ilt, html):
    """
    使用re模块，利用正则表达式分析json数据，ilt列表中存储需要的数据
    :param ilt: 
    :param html: 
    :return: 
    """
    try:
        # 将数据转成字符串
        html = str(html)
        # 找到所有的武器名称
        name = []
        namelt = re.findall(r"'mc_94': '.*?'", html)
        for i in range(len(namelt)):
            name_temp = namelt[i].split(': ')[1].strip("'")
            if len(name) < 43 and name_temp not in ['突击步枪', '射手步枪', '狙击枪', '冲锋枪', '霰弹枪', '机枪', '手枪', '近战武器', '其他']:
                if name_temp not in name:
                    name.append(name_temp)
        # 找到武器对应的属性
        lt = re.findall(r"'ldtw_f2': \[.*?\]", html)
        lt = str(lt)
        weililt = re.findall(r"'wl_45': '\d+'", lt)
        shechenglt = re.findall(r"'sc_54': '\d+'", lt)
        shesult = re.findall(r"'ss_d0': '\d+'", lt)
        zidanlt = re.findall(r"'zds_62': '\d+'", lt)
        wendinglt = re.findall(r"'wdx_a7': '\d+'", lt)
        imagelt = re.findall(r"'tp_93': '//.*?'", html)
        # 获取武器的属性值和图片的url
        for i in range(len(name)):
            weili = eval(weililt[i].split(':')[1])
            shecheng = eval(shechenglt[i].split(':')[1])
            shesu = eval(shesult[i].split(':')[1])
            zidan = eval(zidanlt[i].split(':')[1])
            wending = eval(wendinglt[i].split(':')[1])
            image = 'http://' + imagelt[i].split('//')[1].replace("'", "")
            ilt.append([name[i], weili, shecheng, shesu, zidan, wending, image])
    except:
        print('')

def get_image(ilt):
    """
    下载所有武器的图片
    :param ilt: 
    :return: 
    """
 
    save_dir='./jingying_img'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for lt in ilt:
        name = lt[0]
        url_img = lt[-1]
        r = requests.get(url_img)
        f = open('jingying_img/' + name + '.jpg', 'wb')
        f.write(r.content)
        f.close()

def get_weapon_img(wea):
    w=wea
    #总文件夹
    save_dir='./jingying_weapon_img'  
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    for n in w:
        #枪名文件夹
        save_dir_2=save_dir+'/'+n
        if not os.path.exists(save_dir_2):
            os.mkdir(save_dir_2)
        for p in w[n]['图片']:
            #图片类型文件夹
            save_dir_3=save_dir_2+'/'+p
            if not os.path.exists(save_dir_3):
                os.mkdir(save_dir_3)
            #写入图片，并更改字典路径
            if p=='原始':
                name = p
                url_img =w[n]['图片'][p] 
                r = requests.get(url_img)
                path=save_dir_3 +'/'+ name + '.jpg'
                f = open(path, 'wb')
                w[n]['图片'][p]=path
                f.write(r.content)
                f.close()
            else:
                for pp in w[n]['图片'][p]:
                    name=pp
                    url_img =w[n]['图片'][p][pp] 
                    r = requests.get(url_img)
                    path=save_dir_3+'/'+ name + '.jpg'
                    f = open(path, 'wb')
                    w[n]['图片'][p][pp]=path
                    f.write(r.content)
                    f.close()
    return w

def print_weapon_list(ilt):
    tplt = '{:^12}\t{:5}\t{:5}\t{:5}\t{:5}\t{:5}\t{:5}'
    print(tplt.format('名称', '威力', '射程', '射速', '子弹数', '稳定性', '图片'))
    for i in range(len(ilt)):
        lt = ilt[i]
        print(tplt.format(lt[0], lt[1], lt[2], lt[3], lt[4], lt[5], lt[6]))

if __name__=='__main__':
    pass
    #url = 'https://gp.qq.com/zlkdatasys/data_zlk_hpjywqzlk.json'
    #html = get_html_text(url)
    #write_file_content('hpjy1.html',str(html))
    #lis = []
    #namelt = re.findall(r"'mc_94': '.*?'", str(html))
    #print(namelt)
    #wea=parse_wuqi_page(html)
    #get_weapon_img(wea)
    

