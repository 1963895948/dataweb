from django.db import models

# Create your models here.
from mongoengine import *
import pymongo

connect("city58",host="127.0.0.1",port=27017)

class Employee(Document):
    name = StringField(max_length=5)
    age = IntField()
    address=StringField(max_length=50)
    meta = {'collection': "bjzufang_detail"}
