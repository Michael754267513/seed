#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

def returnRes(env,res):
  headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'content-type': 'application/json;charset=utf8',
        'Accept': 'application/json'
    }
  url = 'http://1.1.1.1/dmgr/env/%s/deploy/%s'%(env,str(res))

  response = requests.get(url=url, headers=headers)
  print response