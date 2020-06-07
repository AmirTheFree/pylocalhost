# In the name of Allah

import os
import json
from flask import request,abort
from functools import wraps


def browser(path):
    result = {'drives': [], 'folders': [],
              'files': [], 'links': [], 'unknowns': []}
    # first list will include drives & the second one will include folders & the third one will include files & the fourth one will include links & the fifth one will include unknowns
    if not os.path.isdir(path):
        return False
    for i in sorted(os.listdir(path), key=str.lower):
        if os.path.ismount(os.path.join(path, i)):
            result['drives'].append({'name': i, 'type': 'drive'})
        elif os.path.islink(os.path.join(path, i)):
            result['links'].append({'name': i, 'type': 'link'})
        elif os.path.isdir(os.path.join(path, i)):
            result['folders'].append({'name': i, 'type': 'folder'})
        elif os.path.isfile(os.path.join(path, i)):
            extentions_json_file = open('extentions.json')
            extentions = json.load(extentions_json_file)
            for e in extentions:
                for s in extentions[e]:
                    if i.lower().endswith(s):
                        result['files'].append({'name': i, 'type': e})
            recongnized = False
            for f in result['files']:
                if i == f['name']:
                    recongnized = True
                    break
            if not recongnized:
                result['files'].append({'name': i, 'type': 'file'})
        else:
            result['unknowns'].append({'name': i, 'type': 'unknown'})
    return result

