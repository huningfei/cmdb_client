#!/usr/bin/python
# -*- coding:utf-8 -*-

result = {'status':True,'error':None,'data':None}
try:
    result['status'] = True
except Exception as e:
    pass

print(result)

class BaseResponse(object):
    def __init__(self):
        self.status = True
        self.error = None
        self.data = None

    @property
    def dict(self):
        return self.__dict__

result = BaseResponse()
try:
    result.status = False
except Exception as e:
    pass
print(result.dict)

