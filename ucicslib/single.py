#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015-1-16

@author: ヽoo悾絔℅o。

@email: 892768447@qq.com

@description: 单例
'''

# 单例模式
class Single(object):

    def __new__(self, *args, **kwargs):
        if not hasattr(self, "_instance"):
            _new = super(Single, self)
            self._instance = _new.__new__(self, *args, **kwargs)
        return self._instance

if __name__ == "__main__":
    a = Single()
    b = Single()

    print(a, id(a))
    print(b, id(b))
