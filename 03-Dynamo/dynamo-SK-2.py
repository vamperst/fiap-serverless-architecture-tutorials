import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime
import json

dao = BaseDAO('sell')


items = dao.scan_table_eq('sell_id', 'rafael')
print(len(items['Items']))
print(json.dumps(items))
print('>>>>>>>>>>>>>>>>')
items = dao.scan_table_eq('datetime', '2021-05-05 16:55:56.233241')
print(len(items['Items']))
print(json.dumps(items))
