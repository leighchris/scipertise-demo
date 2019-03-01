from django.shortcuts import render

 #Create your views here.
from users.models import CustomUser
from .models import Channel

from faker import Factory
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

from twilio.rest import Client
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import (
    SyncGrant,
    ChatGrant
)

from chatapp.utils import get_client

@login_required
def create_channel(request, to_user_id):
    to_user = get_user_model().objects.get(pk=to_user_id)
    try:
        channel = Channel.objects.get(users=request.user, users__id=to_user_id)
    except Channel.DoesNotExist:
        channel = Channel.objects.create(
            channel_name='{from_user}-{to_user}'.format(from_user=request.user.username, to_user=to_user)
        )
        channel.users.add(request.user)
        channel.users.add(to_user)
        client = get_client()
        service = client.chat.services(settings.TWILIO_CHAT_SID)
        twilio_channel = service.channels.create(channel.channel_name)
        
        channel.twilio_chat_id = twilio_channel.sid
        
        twilio_channel.members.create(identity=request.user.get_twilio_user_id())
        twilio_channel.members.create(identity=to_user.get_twilio_user_id())
        channel.save()
        
    return HttpResponseRedirect(reverse('twilio', kwargs={'pk': channel.pk}))
        
    
@login_required
def app(request, pk):
    channel = Channel.objects.get(pk=pk)
    return render(request, 'twilio/index.html', {'channel': channel})

@login_required
def token(request):
    identity = request.user.get_twilio_user_id() #called to verify they have a twilio user account, they should on channel create already
        
    return generateToken(identity)

def generateToken(identity):
    # Get credentials from environment variables
    account_sid      = settings.TWILIO_ACCT_SID
    chat_service_sid = settings.TWILIO_CHAT_SID
    sync_service_sid = settings.TWILIO_SYNC_SID
    api_sid          = settings.TWILIO_API_SID
    api_secret       = settings.TWILIO_API_SECRET

    # Create access token with credentials
    token = AccessToken(account_sid, api_sid, api_secret, identity=identity)

    # Create a Sync grant and add to token
    if sync_service_sid:
        sync_grant = SyncGrant(service_sid=sync_service_sid)
        token.add_grant(sync_grant)

    # Create a Chat grant and add to token
    if chat_service_sid:
        chat_grant = ChatGrant(service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    # Return token info as JSON
    return JsonResponse({'identity':identity,'token':token.to_jwt().decode('utf-8')})
