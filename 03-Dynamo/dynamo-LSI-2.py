import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime
import json

dao = BaseDAO('sell_lci')

items = dao.scan_table_eq('user','rafael')
print(len(items['Items']))

items = dao.query_table_key_and_range_key_on_secondaryIndex('user','rafael','store', 'store1','user-store-index')
print(len(items['Items']))
print(json.dumps(items['Items']))




