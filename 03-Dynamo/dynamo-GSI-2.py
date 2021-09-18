import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime
import json

dao = BaseDAO('sell_gsi')

items = dao.scan_table_eq('user','rafael')
print(len(items['Items']))

items = dao.query_table_key_between_range_key_on_secondaryIndex('store','shop4','datetime', 
    '2021-05-05 17:12:53.286678','2021-05-05 17:12:55.458917','store-datetime-index')
print(len(items['Items']))
print(json.dumps(items['Items']))




