# coding: utf-8


from models import People, Message, Room
from ChatAdmin.factories import PeopleFactory, MessageFactory, RoomFactory
from django.test import TestCase


class PeopleTest(TestCase):
    def setUp(self):
        self.user = People.objects.create(name='Semen', ip='127.0.0.1', email='semen@test.com', is_block=1)

    def tearDown(self):
        self.user = None

    def test_people(self):
        self.assertEqual(str(self.user.name), 'Semen')
        self.assertEqual(str(self.user.ip), '127.0.0.1')
        self.assertEqual(str(self.user.email), 'semen@test.com')
        self.assertEqual(str(self.user.is_block), '1')


    def test_people_save(self):
        self.user.save()
        obj = People.objects.get(name='Semen', ip='127.0.0.1', email='semen@test.com', is_block=1)
        self.assertEqual(obj.name, 'Semen')
        self.assertEqual(obj.ip, '127.0.0.1')
        self.assertEqual(obj.email, 'semen@test.com')
        self.assertEqual(obj.is_block, 1)


    def test_delete_people(self):
        self.user.save()
        People.objects.filter(name='Semen').delete()
        People.objects.filter(ip='127.0.0.1').delete()
        People.objects.filter(email='semen@test.com').delete()
        People.objects.filter(is_block=1).delete()


class MessageTest(TestCase):
    def setUp(self):
        self.user_message = Message.objects.create(text='hello world', people_id=1, room_id=2)

    def tearDown(self):
        self.user_message = None

    def test_message(self):
        self.assertEqual(str(self.user_message.text), 'hello world')
        self.assertEqual(self.user_message.people_id, 1)
        self.assertEqual(self.user_message.room_id, 2)

    def test_message_save(self):
        self.user_message.save()

        obj = Message.objects.get(text='hello world', people_id=1, room_id=2)
        self.assertEqual(obj.message, 'hello world')
        self.assertEqual(obj.people_id, 1)
        self.assertEqual(obj.room_id, 2)

    def test_delete_message(self):
        self.user_message.save()
        Message.objects.filter(text='hello world').delete()
        Message.objects.filter(people_id=1).delete()
        Message.objects.filter(room_id=2).delete()


class RoomTest(TestCase):
    def setUp(self):
        self.user_room = Room.objects.create(title='test_room', user_key=1)

    def tearDown(self):
        self.user_room = None

    def test_room(self):
        self.assertEqual(str(self.user_room.title), 'test_room')
        self.assertEqual(self.user_room.user_key, 1)

    def test_room_save(self):
        self.user_room.save()

        obj = Room.objects.get(title='test_room', user_key=1)
        self.assertEqual(obj.title, 'test_room')
        self.assertEqual(obj.user_key, u'1')

    def test_delete_room(self):
        self.user_room.save()
        Room.objects.filter(title='test_room').delete()
        Room.objects.filter(user_key=1).delete()


class FactoryTestsCase(TestCase):
    def test_people_factory(self):
        people = PeopleFactory()
        self.assertTrue(isinstance(people, People))

    def test_room_factory(self):
        room = RoomFactory()
        self.assertTrue(isinstance(room, Room))

    def test_message_factory(self):
        message = MessageFactory()
        self.assertTrue(isinstance(message, Message))



















