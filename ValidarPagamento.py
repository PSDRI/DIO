import json

def lambda_handler(event, context):
    # Simulação de validação de pagamento (integração com gateway real não inclusa)
    pagamento_confirmado = True  # Assumindo pagamento aprovado para exemplo
    
    if pagamento_confirmado:
        return {
            'statusCode': 200,
            'body': json.dumps('Pagamento Confirmado'),
            'pedido_id': event['pedido_id']
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('Pagamento Falhou'),
            'pedido_id': event['pedido_id']
        }
