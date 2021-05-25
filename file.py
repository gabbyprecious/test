import requests

data = {
  "to": {
    "type": "whatsapp",
    "number": "2348113660619"
  },
  "from": {
    "type": "whatsapp",
    "number": "14157386170"
  },
  "message": {
    "content": {
      "type": "text",
      "text": "Hello From Vonage!"
    }
  }
}
url = "https://messages-sandbox.nexmo.com/v0.1/messages"

resp = requests.post(url, data=data, auth=('user', 'pass'))