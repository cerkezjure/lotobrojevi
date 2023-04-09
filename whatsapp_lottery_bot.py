import random
from twilio.rest import Client
import schedule
import time

# Twilio credentials
account_sid = 'AC34c00e8f6ded6525d724ff4ec2550b71'
import random
from twilio.rest import Client
import schedule
import time

# Twilio credentials
account_sid = 'AC34c00e8f6ded6525d724ff4ec2550b71'
auth_token = '1aba653c18148988e14414bfc1402ae4'
client = Client(account_sid, auth_token)

# Your dad's phone number and your Twilio phone number
dad_phone_number = 'whatsapp:+385998167000'
twilio_phone_number = 'whatsapp:+14155238886'


def generate_lottery_numbers():
    main_numbers = sorted(random.sample(range(1, 51), 5))
    extra_numbers = sorted(random.sample(range(1, 11), 2))
    return main_numbers + extra_numbers


def send_whatsapp_message():
    lottery_numbers = generate_lottery_numbers()
    message_body = f"Danasnji brojevi su: {', '.join(map(str, lottery_numbers))}"

    message = client.messages.create(
        body=message_body,
        from_=twilio_phone_number,
        to=dad_phone_number
    )

    print(f"Message sent: {message.sid}")


send_whatsapp_message()

# # Schedule the bot to send messages every Tuesday and Friday at 1 pm
schedule.every().tuesday.at("09:00").do(send_whatsapp_message)
schedule.every().friday.at("09:00").do(send_whatsapp_message)

# # Keep the script running
while True:
    schedule.run_pending()
    print('looping')
    time.sleep(60)
