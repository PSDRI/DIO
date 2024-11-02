import boto3
import json

stepfunctions = boto3.client('stepfunctions')

# Definir o fluxo do Step Functions em JSON
definition = {
    "Comment": "Fluxo de Assistente de Delivery",
    "StartAt": "ReceberPedido",
    "States": {
        "ReceberPedido": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:ReceberPedidoFunction",
            "Next": "ValidarPagamento"
        },
        "ValidarPagamento": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:ValidarPagamentoFunction",
            "Next": "AtualizarStatus"
        },
        "AtualizarStatus": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:AtualizarStatusFunction",
            "Next": "RastrearEntrega"
        },
        "RastrearEntrega": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:RastrearEntregaFunction",
            "Next": "ConfirmarEntrega"
        },
        "ConfirmarEntrega": {
            "Type": "Task",
            "Resource": "arn:aws:lambda:REGION:ACCOUNT_ID:function:ConfirmarEntregaFunction",
            "End": True
        }
    }
}

# Criar o Step Function
response = stepfunctions.create_state_machine(
    name='AssistenteDeDelivery',
    definition=json.dumps(definition),
    roleArn='arn:aws:iam::ACCOUNT_ID:role/service-role/StepFunctionsRole'  # Ajuste o ARN da role conforme necessário
)

print("Step Function criada com sucesso:", response)
