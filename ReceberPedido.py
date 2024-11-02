import boto3
import json

def lambda_handler(event, context):
    # Simulando o recebimento do pedido
    pedido_id = event.get('pedido_id')
    cliente = event.get('cliente')
    itens = event.get('itens')
    
    # Salva o pedido inicial no DynamoDB
    dynamodb = boto3.resource('dynamodb')
    tabela_pedidos = dynamodb.Table('Pedidos')
    tabela_pedidos.put_item(Item={
        'pedido_id': pedido_id,
        'cliente': cliente,
        'itens': itens,
        'status': 'Pedido Recebido'
    })
    
    return {
        'statusCode': 200,
        'body': json.dumps('Pedido Recebido e Salvo no DynamoDB'),
        'pedido_id': pedido_id
    }
