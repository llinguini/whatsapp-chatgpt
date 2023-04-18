# WhatSapp + ChatGPT

This is a 1 file chatgpt based assistant.

## Installation

You can view more in mi [blog](https://linguini.ga/chat-de-whatsapp-con-chatgpt/) to extended configuration.

```bash
sudo docker run -p 8085:8085 openwa/wa-automate --socket -p 8085 -k "SomeSecret"
```

## Usage

```python
from wa_automate_socket_client import SocketClient

# send 'words'
client.sendReplyWithMentions(from_wa, "words")

# change opainai model
model_engine = "text-davinci-003"

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)