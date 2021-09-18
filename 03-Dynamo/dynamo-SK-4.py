import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime
import json

dao = BaseDAO('sell')


items = dao.query_table_key_between_range_key('sell_id','rafael','datetime', '2021-05-05 16:55:56.233241','2021-05-05 16:56:01.023557')
print(len(items['Items']))
print(json.dumps(items))

