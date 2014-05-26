# -*- coding: utf-8 -*-
# import MySQLdb
#
# dbHost = '127.0.0.1'
# dbPort = 3306
# dbName = 'support_chat'
# dbUser = 'root'
# dbPass = ''
#
#
# def db_connect():
#     try:
#         db = MySQLdb.connect(host=dbHost, port=dbPort, user=dbUser, passwd=dbPass)
#     except MySQLdb.MySQLError, err:
#         print 'Cannot connect to database. MySQL error:' + str(err)
#
# def db_in():
#     if len(message)>0:
#         r = Message.objects.order_by('-date')[:20]
#         res = []
#         for