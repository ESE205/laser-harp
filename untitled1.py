#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 21:27:30 2019

@author: 39387
"""

import requests

# record sounrd

# write sounds


with open('hi.wav', 'rb') as f:
    requests.post('http://3.211.80.203:3000/upload/0452.wav', files={'0452.wav': f})