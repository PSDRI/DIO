import boto3
import json

def lambda_handler(event, context):
    pedido_id = event['pedido_id']
    
    # Atualizar o status do pedido no DynamoDB para "Em Preparo"
    dynamodb = boto3.resource('dynamodb')
    tabela_pedidos = dynamodb.Table('Pedidos')
    tabela_pedidos.update_item(
        Key={'pedido_id': pedido_id},
        UpdateExpression="set #st = :s",
        ExpressionAttributeNames={'#st': 'status'},
        ExpressionAttributeValues={':s': 'Em Preparo'}
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Status Atualizado para Em Preparo'),
        'pedido_id': pedido_id
    }
