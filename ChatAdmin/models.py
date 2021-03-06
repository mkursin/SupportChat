# coding: utf-8
from django.db import models
from django.forms import ModelForm
from uuid import uuid4


class People(models.Model):
    # message = models.ForeignKey('Message', db_column='message', related_name="%(class)s_related")
    id = models.AutoField(editable=False, primary_key=True)
    name = models.CharField(max_length=20, verbose_name=u'Имя', blank=True, unique=True)
    ip = models.IPAddressField(verbose_name=u'IP address')
    email = models.EmailField(blank=True)
    is_block = models.IntegerField(max_length=1, verbose_name=u'Block')
    start_date = models.DateTimeField(verbose_name=u'Дата входа', auto_now_add=True)
    date = models.DateTimeField(verbose_name=u'Дата сообщения', auto_now_add=True)

    class Meta:
        verbose_name = 'UserSupport'
        verbose_name_plural = 'UserSupport'
        db_table = 'people'

    def __unicode__(self):
        return '%s: %s' % (self.start_date, self.name)


class PeopleModelForm(ModelForm):
    """
    форма модели People
    """

    class Meta:
        model = People
        fields = ('name', 'email',)


class Room(models.Model):
    hash_key = models.CharField(unique=True, max_length=64, null=True, editable=False, blank=True, default=uuid4)
    user_key = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=20, verbose_name=u'Название комнаты')
    date = models.DateTimeField(verbose_name=u'Время сообщения', auto_now_add=True)

    class Meta:
        verbose_name = 'ChatRoom'
        verbose_name_plural = 'ChatRoom'
        db_table = 'room'

    def __unicode__(self):
        return self.title


class Message(models.Model):
    message = models.CharField(max_length=255,  verbose_name=u'Сообщение')
    sent = models.DateTimeField(auto_now_add=True)
    people_id = models.IntegerField()
    room_id = models.IntegerField()

    class Meta:
        verbose_name = 'ChatMessage'
        verbose_name_plural = 'ChatMessage'
        db_table = 'message'


    def __unicode__(self):
        return unicode(self.name)


class MessageModelForm(ModelForm):
    """
    форма модели Message
    """

    class Meta:
        model = Message
        fields = ('message',)
