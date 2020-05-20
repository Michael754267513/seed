#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'content-type': 'application/json;charset=utf8',
    'Accept': 'application/json'
}

# url = 'http://10.148.181.214:8888/kubernetes/init/svc'
# message_params = {"env":"bfenv001","owner":"srp","project":"bfintech"}


url = 'http://10.148.181.214:8888/kubernetes/update/deployment'
# #message_params = {"coreCreates":["harbor.com.cn/srp-bfintech/hpayFintechConnService:0.0.1-SNAPSHOT-24f36448e1a7a20d7921fca2a502abd517b222da-2019-06-21_14.57.34","harbor.handpay.com.cn/srp-bfintech/hpayaaaa:0.0.1-SNAPSHOT-24f36448e1a7a20d7921fca2a502abd517b222da-2019-06-21_14.57.34"],"coreUpdates":["harbor.handpay.com.cn/srp-bfintech/hpayFintechUI:0.0.1-SNAPSHOT-24f36448e1a7a20d7921fca2a502abd517b222da-2019-06-21_14.57.34"],"deletes":["harbor.handpay.com.cn/srp-bfintech/hpayFintechUI:0.0.1-SNAPSHOT-24f36448e1a7a20d7921fca2a502abd517b222da-2019-06-21_14.57.34","harbor.handpay.com.cn/srp-bfintech/hpayFintechUI:0.0.1-SNAPSHOT-24f36448e1a7a20d7921fca2a502abd517b222da-2019-06-21_14.57.34"],"env":"bfenv001","owner":"srp","project":"bfintech","uiCreates":["harbor.handpay.com.cn/srp-bfintech/hpayFintechUI:0.0.1-SNAPSHOT-24f36448e1a7a20d7921fca2a502abd517b222da-2019-06-21_14.57.34"],"uiUpdates":["harbor.handpay.com.cn/srp-bfintech/hpayFintechUI:0.0.1-SNAPSHOT-24f36448e1a7a20d7921fca2a502abd517b222da-2019-06-21_14.57.34"]}
# message_params ={
# 	"coreCreates": [],
# 	"coreUpdates": [],
# 	"deletes": ["harbor.com.cn/srp-bfintech/uiCreates:0.98.1-SNAPSHOT-24f36448e1a7a20d7921fca2a502abd517b222da-2019-06-21_14.57.34"],
# 	"env": "bfenv001",
# 	"owner": "srp",
# 	"project": "bfintech",
# 	"uiCreates": [],
# 	"uiUpdates": []
# }
#
message_params ={u'uiUpdates': [], u'coreUpdates': [], u'uiCreates': [], u'coreCreates': [u'harbor.com.cn/srp-bfintech/hpayfintechassistservice:0.0.1-SNAPSHOT-b65464d33717e2748116648a2c3e660c002d9611-2019-08-14_17.12.06', u'harbor.handpay.com.cn/srp-bfintech/hpayfintechconnservice:0.0.1-SNAPSHOT-0e70a26be4bcc3304ce3e4df8dbd42f8ad28130b-2019-08-14_17.12.06', u'harbor.handpay.com.cn/srp-bfintech/hpayfintechcoreservice:0.0.1-SNAPSHOT-c2c4a2b85099a1ea479548734cc8176dc1fb8253-2019-08-14_17.12.06', u'harbor.handpay.com.cn/srp-bfintech/hpayfintechuserservice:0.0.1-SNAPSHOT-341f33bbcb7ec21c1e74d1965c1600b32d4b2049-2019-08-14_17.12.06'], u'project': u'bfintech', u'env': u'bfienv003', u'owner': u'lfjiang', u'deletes': []}
#服务初始化
# url = "http://10.148.181.214:8888/kubernetes/init/svc"
# message_params = {"env":"bfenv001","owner":"srp","project":"bfintech"}


# # 删除环境
# url = "http://10.148.181.214:8888/kubernetes/delete/ns"
# message_params = {"env":"bfienv003"}

response = requests.post(url, json=message_params, headers=headers,)
print(response.content)
