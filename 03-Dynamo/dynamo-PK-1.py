import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime

dao = BaseDAO('book')


dao.put_item({'book_id':'111', 'name': 'teste1'})
dao.put_item({'book_id':'111', 'name': 'teste1'})
dao.put_item({'book_id':'111', 'name': 'teste1', 'year': 1999})
