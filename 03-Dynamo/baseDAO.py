import boto3
from boto3.dynamodb.conditions import Key


class BaseDAO:
    def __init__(self, table_name):
        self.__table = boto3.resource('dynamodb').Table(table_name)


    def put_item(self, item):
        return self.__table.put_item(
            Item=item,
            ReturnConsumedCapacity='TOTAL'
        )


    def scan_table_eq(self, filter_key=None, filter_value=None):
        if filter_key and filter_value:
            filtering_exp = Key(filter_key).eq(filter_value)
            response = self.__table.scan(FilterExpression=filtering_exp)
        else:
            response = self.__table.scan()

        return response
    

    def scan_table_gt(self, filter_key=None, filter_value=None):
        if filter_key and filter_value:
            filtering_exp = Key(filter_key).gt(filter_value)
            response = self.__table.scan(FilterExpression=filtering_exp)
        else:
            response = self.__table.scan()

        return response
    

    def scan_table_between(self, filter_key, filter_value1,filter_value2):

        filtering_exp = Key(filter_key).between(filter_value1,filter_value2)
        response = self.__table.scan(FilterExpression=filtering_exp)

        return response

    def query_table_key_between_range_key(self, partition_key,partition_key_value,range_key, range_key_value1,range_key_value2):
    
        filtering_exp = Key(partition_key).eq(partition_key_value) & Key(range_key).between(range_key_value1,range_key_value2)
        response = self.__table.query(
            KeyConditionExpression=filtering_exp
        )
        return response
    
    def query_table_key_between_range_key_on_secondaryIndex(self, partition_key,partition_key_value,range_key, range_key_value1,range_key_value2,indexName):
        
        filtering_exp = Key(partition_key).eq(partition_key_value) & Key(range_key).between(range_key_value1,range_key_value2)
        response = self.__table.query(
            IndexName=indexName,
            KeyConditionExpression=filtering_exp
        )
        return response

    def query_table_key_and_range_key(self, partition_key,partition_key_value,range_key, range_key_value):
        
        filtering_exp = Key(partition_key).eq(partition_key_value) & Key(range_key).eq(range_key_value)
        response = self.__table.query(
            KeyConditionExpression=filtering_exp
        )
        return response
    def query_table_key_and_range_key_on_secondaryIndex(self, partition_key,partition_key_value,range_key, range_key_value,indexName):
        
        filtering_exp = Key(partition_key).eq(partition_key_value) & Key(range_key).eq(range_key_value)
        response = self.__table.query(
            IndexName=indexName,
            KeyConditionExpression=filtering_exp
        )
        return response
    def scan_table_allpages(self, filter_key=None, filter_value=None):
        if filter_key and filter_value:
            filtering_exp = Key(filter_key).eq(filter_value)
            response = self.__table.scan(FilterExpression=filtering_exp)
        else:
            response = self.__table.scan()

        items = response['Items']
        while True:
            print(len(response['Items']))
            if response.get('LastEvaluatedKey'):
                response = self.__table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                items += response['Items']
            else:
                break

        return items

    def delete_item(self, mapkey):
        return self.__table.delete_item(
            Key=mapkey,
            ReturnConsumedCapacity='TOTAL'
        )

    def query(self, expression):
        return self.__table.query(
            KeyConditionExpression=expression,
            ReturnConsumedCapacity='TOTAL'
        )

    def query_index(self, expression, index):
        return self.__table.query(
            IndexName=index,
            KeyConditionExpression=expression,
            ReturnConsumedCapacity='TOTAL'
        )
