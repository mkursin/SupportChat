# -*- coding: utf-8 -*-
import json
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, Http404, HttpResponse
from django.shortcuts import render_to_response
from ChatAdmin.models import People, PeopleModelForm, Message, MessageModelForm, Room


list_comments = People.objects.all().order_by('-date')
error = 'error'


def add_question_by_db(request):
    if request.method == 'GET':
        form = PeopleModelForm(request.GET)
        form.fields['name'].required = True
        form.fields['email'].required = True
        # form.fields['message'].required = True

        if form.is_valid():
            form.save()
            return render_to_response('index.html', {'list_comments': list_comments})

    else:
        form = PeopleModelForm()
    return render_to_response('index.html', {'form': form})


def list_question_by_db(request):
    list_comment_context = {'list_comments': list_comments}
    return render_to_response('index.html', list_comment_context)
#
#
# def add_messages_by_db(request):
#     list_messages = Message.objects.all()
#     if request.method == 'GET':
#         form2 = MessageModelForm(request.GET)
#         form2.fields['message'].required = True
#         if form2.is_valid():
#             form2.save()
#             return render_to_response('index.html', {'list_messages': list_messages})
#
#     else:
#         form2 = MessageModelForm()
#     return render_to_response('index.html', {'form': form2})




