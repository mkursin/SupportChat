# -*- coding: utf-8 -*-
import pusher
import json


APP_ID = '76012',
APP_KEY = 'd38cb75bae481304ff34',
APP_SECRET = '797bc8d8afb11ccd4d0f'

p = pusher.Pusher(app_id=APP_ID, key=APP_KEY, secret=APP_SECRET)
p['private-channel'].trigger('private-event', {'message': 'data'}, socket_id)

from django.core.serializers.json import DjangoJSONEncoder

p = pusher.Pusher(app_id=APP_ID, encoder=DjangoJSONEncoder)

channel_data = {
    "channel": String,
    "auth": String,
    "channel_data": Object
}

data = json.dumps(channel_data)

return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')







