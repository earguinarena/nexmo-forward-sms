from flask import Flask
from flask import  request
from vonage import vonage
import boto3

app = Flask(__name__)
ssm = boto3.client('ssm')


VONAGE_API_KEY = (ssm.get_parameter(Name='/vonage/api_key', WithDecryption=True))['Parameter']['Value']
VONAGE_API_SECRET = (ssm.get_parameter(Name='/vonage/api_secret', WithDecryption=True))['Parameter']['Value']
VIRTUAL_NUMBER = (ssm.get_parameter(Name='/vonage/virtual_number', WithDecryption=True))['Parameter']['Value']
DESTINATION_NUMBER = (ssm.get_parameter(Name='/vonage/destination_number', WithDecryption=True))['Parameter']['Value']

client = vonage.Client(key=VONAGE_API_KEY, secret=VONAGE_API_SECRET)
sms = vonage.Sms(client)


@app.route('/')
def test_simple_message():
    send_sms_message(DESTINATION_NUMBER, "Nexmo Forward SMS")
    return "OK", 200


@app.route('/webhooks/inbound-sms', methods=['POST'])
def inbound_sms():
    if request.is_json:
        print(request.get_json())
        sms_text = request.json.get('text')

        send_sms_message(DESTINATION_NUMBER, sms_text)

    else:
        return '', 404

    return '', 204


def send_sms_message(to_number, sms_text):
    response_data = sms.send_message(
        {
            "from": VIRTUAL_NUMBER,
            "to": to_number,
            "text": sms_text,
        }
    )

    if response_data["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {response_data['messages'][0]['error-text']}")
