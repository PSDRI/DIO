import boto3
import json

def lambda_handler(event, context):
    pedido_id = event['pedido_id']
    
    # Atualiza o status para "Entregue" no DynamoDB
    dynamodb = boto3.resource('dynamodb')
    tabela_pedidos = dynamodb.Table('Pedidos')
    tabela_pedidos.update_item(
        Key={'pedido_id': pedido_id},
        UpdateExpression="set #st = :s",
        ExpressionAttributeNames={'#st': 'status'},
        ExpressionAttributeValues={':s': 'Entregue'}
    )
    
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:REGION:ACCOUNT_ID:notifyClientTopic',
        Message=f'Seu pedido {pedido_id} foi entregue!'
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Status Atualizado para Entregue'),
        'pedido_id': pedido_id
    }
