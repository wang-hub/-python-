# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:21:26 2020

@author: wangwei
"""

import os


def open_with_chrome(file_path):
    chrome_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    cmd = "%s %s" % (chrome_path, file_path)
    os.system(cmd)


def open_with_default_browser(file_path):
    cmd = "explorer %s" % (file_path)
    os.system(cmd)