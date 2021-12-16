# In the name of Allah

from functools import wraps
from flask import session,abort
import mwx
import hashlib

h = hashlib.sha256()
h.update(str(mwx.rwjson('info.json')['password']).encode('utf-8'))

def secure_api(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        if str(session.get('id',False)) != h.hexdigest():
             abort(403)
        return func(*args,**kwargs)
    return decorator

class DangerousIP:
    def __init__(self,address):
        self.address = address
        self.chances = 4
    def register_attemp(self):
        if self.chances == 0:
            data = mwx.rwjson('info.json')
            data['ips'].append(self.address)
            mwx.rwjson('info.json',data)
            return True
        self.chances -= 1
        return False


