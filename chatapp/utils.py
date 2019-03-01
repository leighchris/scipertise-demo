from django.conf import settings
from twilio.rest import Client

def get_client():
    return Client(settings.TWILIO_ACCT_SID, settings.TWILIO_AUTH_TOKEN)