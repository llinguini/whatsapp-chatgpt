from wa_automate_socket_client import SocketClient
from decouple import config
import openai

print('Iniciando')
NUMBER_ADMIN = config('NUMBER')
client = SocketClient(config('CLIENT_URL'), config('CLIENT_PASS'))
openai.api_key = config('OPENAI_TOKEN')
model_engine = "text-davinci-003"
host_number = client.getHostNumber()
client.setPresence(True)


def print_response(message):
    tipo = message['data']['type']
    mensaje = message['data']['body']
    from_wa = message['data']['from']
    to_wa = message['data']['to']
    new = message['data']['isNewMsg']
    id_mensaje = message['data']['id']
    client.simulateTyping(from_wa, True)

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=mensaje,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0,
    )

    print("ChatGPT Online")
    response = completion.choices[0].text
    client.sendReplyWithMentions(from_wa, response)

    res = f"{from_wa}-{tipo}-{mensaje}"
    print("PREGUNTA", res)
    client.simulateTyping(from_wa, False)
    client.setPresence(False)
    client.sendSeen(from_wa)


client.sendText(NUMBER_ADMIN, f'BotWhatsAPP Encendido. {host_number}')
client.onMessage(print_response)
print(client.__dir__())