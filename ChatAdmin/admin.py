from django.contrib import admin
from ChatAdmin.models import People, Message, Room


class UserSupportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'ip', 'email', 'is_block', 'started', 'date',)


admin.site.register(People, UserSupportAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'sent', 'name',)


admin.site.register(Message, MessageAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_key', 'date', 'hash_key')


admin.site.register(Room, RoomAdmin)
