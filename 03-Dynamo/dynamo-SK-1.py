import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime

dao = BaseDAO('sell')

users = ['rafael','pedro','teresa','natalia', 'eduardo']
books = ['book1','book2','book3','book4','book5','book6']
peeker = random.SystemRandom()

for i in range(100):
    dao.put_item({'sell_id': peeker.choice(users), 
        'datetime':str(datetime.now()),'book':peeker.choice(books)})

