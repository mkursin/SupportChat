# -*- coding: utf-8 -*-
import pusher
import json
import requests
import webapp2
from django.shortcuts import render_to_response
from django.conf import settings
from django.http import HttpResponse
from django.template import RequestContext
# from django.core.serializers.json import DjangoJSONEncoder
from ChatAdmin.models import PeopleModelForm


pusher.app_id = settings.PUSHER_APP_ID
pusher.key = settings.PUSHER_KEY
pusher.secret = settings.PUSHER_SECRET

p = pusher.Pusher()


def home(request):
    if not request.session.get('user'):
        request.session['user'] = 'user-%s' % request.session.session_key
    return render_to_response('pusher_index.html', {
        'PUSHER_KEY': settings.PUSHER_KEY,
    }, RequestContext(request))


def message(request):
    if request.session.get('user') and request.POST.get('name') and request.POST.get('message') \
            and request.POST.get('email'):
        p['chat'].trigger('message', {
            'user': request.session['user'],
            'name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'message': request.POST.get('message'),
        })
    return HttpResponse('')


class AuthHandler(webapp2.RequestHandler):
    def post(self):
        channel_name = self.request.get('chat')
        socket_id = self.request.get('socket_id')
        p = pusher.Pusher(app_id=pusher.app_id, key=pusher.key, secret=pusher.secret)

        auth = p[channel_name].authenticate(socket_id)
        json_data = json.dumps(auth)
        self.response.out.write(json_data)


def main():
    application = webapp2.WSGIApplication([('/pusher/auth', AuthHandler)])







