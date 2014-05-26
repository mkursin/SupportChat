# -*- coding: utf-8 -*-
import factory
from models import People, Message, Room


class PeopleFactory(factory.Factory):
    FACTORY_FOR = People

    name = 'Thomas'
    ip = '127.0.0.1'
    email = 'Thomas@test.com'
    is_block = 1
    sign_in = '2014-05-16 10:48:24.0',
    date = '2014-05-16 10:48:24.0'


class MessageFactory(factory.Factory):
    FACTORY_FOR = Message

    name = factory.lazy_attribute(lambda a: PeopleFactory())
    text = 'test text'
    date = '2014-05-16 10:48:24.0'
    people_id = 1
    room_id = None


class RoomFactory(factory.Factory):
    FACTORY_FOR = Room

    title = 'test_room'
    user_key = 11







