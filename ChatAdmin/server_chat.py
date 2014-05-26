# coding: utf-8
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor


class ChatProtocol(LineReceiver):
    def __init__(self, factory):
        self.factory = factory
        self.name = None
        self.state = "REGISTER"

    def connectionMade(self):  # создание подключения
        print 'Соединение установлено'
        self.sendLine("Введите имя")

    def connectionLost(self, reason):  # разрыв соединения
        if self.name in self.factory.users:
            del self.factory.users[self.name]
            self.broadcastMessage("%s покинул чат." % (self.name,))

    def lineReceived(self, line):
        if self.state == "REGISTER":
            self.handle_REGISTER(line)
        else:
            self.handle_CHAT(line)

    def handle_REGISTER(self, name):
        if name in self.factory.users:
            self.sendLine("Такой пользователь уже есть.")
            return
        self.sendLine("Здравствуй, %s!" % (name,))
        self.broadcastMessage("%s В чат зашел." % (name,))
        self.name = name
        self.factory.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        message = "<%s> %s" % (self.name, message)
        self.broadcastMessage(message)

    def broadcastMessage(self, message):
        for name, protocol in self.factory.users.iteritems():
            if protocol != self:
                protocol.sendLine(message)


class ChatFactory(Factory):
    def __init__(self):
        self.users = {}

    def buildProtocol(self, addr):
        return ChatProtocol(self)


reactor.listenTCP(8123, ChatFactory())
reactor.run()