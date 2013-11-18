# -*- coding: utf-8 -*-

import json
import mongoengine as models

class User(object):
    '''用户类'''
    __userId = 0            # 用户ID
    __userName = ''         # 用户名
    __email = ''            # 邮箱
    __passwd = ''           # 登录密码

    def __init__(self, userId, userName):
	self.__userId = userId
	self.__userName = userName

    def getUserId(self):
        return self.__userId

    def setUserId(self, userId):
        self.__userId = userId

    def getUserName(self):
        return self.__userName

    def setUserName(self, userName):
        self.__userName = userName

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getPasswd(self):
        return self.__passwd

    def setPasswd(self, passwd):
        self.__passwd = passwd

class A(object):
    def __init__(self):
        self.__private()
        self.ask()

    def __private(self):
        print 'A.__private()'

    def ask(self):
        print 'A.ask()'

class MongoJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if not isinstance(obj, models.Document):
            return super(MyJSONEncoder, self).default(obj)
        #return json.JSONEncoder.default(self, obj)
        _data = obj.__dict__['_data'] 
        return _data

class City1(object):
    id = 0
    cityid = 0
    provinceid = 0
    name = ''

    def __str__(self):
        return '{"cityid":%d, "provinceid":%d, "name":"%s"}'%(self.cityid, self.provinceid, self.name)

class City(models.Document):
    cityid = models.IntField()
    provinceid = models.IntField()
    name = models.StringField()

    # turn on inheritance by setting allow_inheritance to True in the meta
    meta = {'allow_inheritance': True}

class Municipality(City):
    level = models.IntField()

if __name__ == '__main__':
    city = City()
    city.cityid = 111
    city.provinceid = 2222
    city.name = 'yangxin'

    city1 = City()
    city1.cityid = 112
    city1.provinceid = 2223
    city1.name = 'huangshi'

    m = Municipality()
    m.cityid = 112
    m.provinceid = 2223
    m.name = 'chongqin'
    m.level = 3

    city_list = []
    city_list.append(city)
    city_list.append(city1)

    print type(city)
    print isinstance(city, models.Document)
    #print city
    #print city.__dict__
    #print MyJSONEncoder().encode(city)
    print json.dumps(city, cls=MongoJSONEncoder)
    print json.dumps(city_list, cls=MongoJSONEncoder)
    print json.dumps(m, cls=MongoJSONEncoder)
    #print json.dumps(city)
