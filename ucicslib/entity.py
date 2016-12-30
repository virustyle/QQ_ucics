#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-14

@author: ヽoo悾絔℅o。

@email: 892768447@qq.com

@description: 
'''
from ucicslib.skylark import Model, Field


class Groups(Model):
    name = Field()

class Users(Model):
    id = Field()
    gid = Field()
    level = Field()
    nick = Field()
    name = Field()
    ip = Field()
    mood = Field()
    head = Field()
    time = Field()
