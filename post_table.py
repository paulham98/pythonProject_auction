import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamo_client = boto3.client('dynamodb')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('post')


def get_item():
    return dynamo_client.scan(
        TableName='post'
    )


def select_all(self):
    r = self.table.scan()
    return r


def list_table():
    response = dynamo_client.list_tables()
    return response


'''
def insert_row(table_name, row):
    r = table.put_item(Item=row)
    print(r)
b = {
    'Arthur': 'paul ham',
    'Title': 'programming',
    'text': 'Hello'
}
insert_row('post', b)
'''



