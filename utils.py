# In the name of Allah

from functools import wraps
from flask import session,abort
import mwxpy
import hashlib

h = hashlib.sha256()
h.update(str(mwxpy.rwjson('info.json')['password']).encode('utf-8'))

def secure_api(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        if str(session.get('id',False)) != h.hexdigest():
             abort(403)
        return func(*args,**kwargs)
    return decorator

