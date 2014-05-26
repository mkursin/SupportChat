# coding: utf-8
import json
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, Http404, HttpResponse
from ChatAdmin.models import PeopleModelForm, MessageModelForm, People, Message, Room
from django.shortcuts import render_to_response


# list_comments = People.objects.all().order_by('-date')
# error = 'error'
#
#
# def add_question_by_db(request):
# if request.method == 'GET':
# form = PeopleModelForm(request.GET)
#         form.fields['name'].required = True
#         form.fields['email'].required = True
#         # form.fields['message'].required = True
#
#         if form.is_valid():
#             form.save()
#             return render_to_response('index.html', {'list_comments': list_comments})
#     else:
#         form = PeopleModelForm()
#     return render_to_response('index.html', {'form': form})
#
#
# def list_question_by_db(request):
#     list_comment_context = {'list_comments': list_comments}
#     return render_to_response('index.html', list_comment_context)


# def add_messages_by_db(request):
#
# list_messages = Message.objects.all()
#     if request.method == 'GET':
#             form = MessageModelForm(request.GET)
#             form.fields['message'].required = True
#             if form.is_valid():
#                 form.save()
#                 return render_to_response('index.html', {'list_messages': list_messages})
#
#     else:
#         form = MessageModelForm()
#     return render_to_response('index.html', {'form': form})
#
#
#
# HOST = ''
# PORT = 50007
#
# name = PeopleModelForm.GET['name']
# email = PeopleModelForm.GET['email']
# message = PeopleModelForm.GET['message']
# block = People.is_block
#
#
# def start_connect():
#     if len(name) > 0 | len(email) | len(message) | block != 0:
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.bind((HOST, PORT))
#         s.send(raw_input)
#         data = s.recv(2048)
#
#
# def end_chat(request):
#     chat = get_object_or_404(People)
#     message = Message()
#     name = request.People.name
#     message.message = '%s Покинул чат. Этот чат закончился' % name
#     chat.messages.add(message)
#     if request.POST.get('end_chat') == 'true':
#         chat.end()
#     return HttpResponseRedirect(request.META['HTTP_REFERER'])
#
#
# def user_connect(request):
#     if request.method != 'POST':
#         raise Http404
#     post = request.POST
#
#     if not post.get('id', None):
#         raise Http404
#     r = People.objects.get(id=post['id'])
#     lmid = r.last_message_id()
#     return HttpResponse(jsonify({'last_message_id': lmid}))
#
#
# def receive(request):
#     if request.method == 'GET':
#         raise Http404
#     get = request.metho.GET


def people_connect(request):
    name = request.GET.get('name')
    email = request.Get.get('email')
    message = request.GET.get('message')
    is_block = People.objects.filter(name).filter(is_block=1)

    if request.method == 'GET':
        user_key = Room.objects.copy_to_model(Room)
        form = PeopleModelForm(request.GET)
        form.fields['name'].required = True
        form.fields['email'].required = True
        form.fields['message'].required = True

        if form.is_valid():
            form.save()
            return render_to_response('index.html', {'list_comments': list_comments})

    else:
        form = PeopleModelForm()
        return render_to_response('index.html', {'form': form})

    if len(name) < 0 or len(email) < 0 or len(message) < 0 or not is_block == 1:
        return HttpResponse('Пожалуйста, заполните все поля')

    if len(message) > 255:
        HttpResponse('Сообщение превышает оганичение')

        # room = Room.objects.filter(user_key)


people_comments = People.objects.all()
message_comments = Message.objects.all()

list_comments = list(people_comments) + list(message_comments)


def add_question_by_db(request):
    if request.method == 'GET':
        form = PeopleModelForm(request.GET)
        form.fields['name'].required = True
        form.fields['email'].required = True
        #
        # form2 = MessageModelForm(request.GET)

        if form.is_valid():
            form.save()
            # form2.save()
            return render_to_response('index.html', {'list_comments': list_comments})

    else:
        form = PeopleModelForm()
    return render_to_response('index.html', {'form': form})


def list_question_by_db(request):
    list_comment_context = {'list_comments': list_comments}
    return render_to_response('index.html', list_comment_context)
















