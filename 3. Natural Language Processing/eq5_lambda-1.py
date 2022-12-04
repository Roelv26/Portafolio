import json

#Equipo 5

#Se hizo esta función lambda en respuesta al ordenar un alambre de costilla.

def lambda_handler(event, context):

    intent_name = event['interpretations'][0]['intent']['name']
    slots = event['interpretations'][0]['intent']['slots']
    selection = slots['Alambres']['value']['interpretedValue']
    message = "Se ha agregado tu pedido de alambre de " + selection + ". Esta respuesta viene desde una función lambda."

    response = {
       'sessionState' : {
            'dialogAction' : {
                'type' : 'Close'
            },
            'intent' : {
                'name' : intent_name,
                'state' : 'Fulfilled'
            }
       },
        'messages': [
             {
                'contentType' : 'PlainText',
                'content' : message
             }
        ]
    }

    return response