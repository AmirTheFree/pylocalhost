# In the name of Allah

import os

def browser(path):
    result = {'drives':[],'folders':[],'files':[],'links':[],'unknowns':[]}
    # first list will include drives & the second one will include folders & the third one will include files & the fourth one will include links & the fifth one will include unknowns
    if not os.path.isdir(path):
        return False
    for i in sorted(os.listdir(path),key=str.lower):
        if os.path.ismount(os.path.join(path,i)):
            result['drives'].append({'name':i,'type':'drive'})
        elif os.path.islink(os.path.join(path,i)):
            result['links'].append({'name':i,'type':'link'})
        elif os.path.isdir(os.path.join(path,i)):
            result['folders'].append({'name':i,'type':'folder'})
        elif os.path.isfile(os.path.join(path,i)):
            for s in ['.css','.sass','.scss']:
                if i.lower().endswith(s):
                    result['files'].append({'name':i,'type':'css'})
            for s in ['.db','.sqlite3','.sqlite','.sql']:
                if i.lower().endswith(s):
                    result['files'].append({'name':i,'type':'database'})
            for s in ['.html','.htm']:
                if i.lower().endswith(s):
                    result['files'].append({'name':i,'type':'html'})
            for s in ['.png','.jpg','.jpeg','.svg','.bmp','.webp','.ico']:
                if i.lower().endswith(s):
                    result['files'].append({'name':i,'type':'image'})
            for s in ['.zip','.rar','.tar','.taz','.tar.xz']:
                if i.lower().endswith(s):
                    result['files'].append({'name':i,'type':'zip'})
            for s in ['.mp4','.avi','.wmv','.mkv','.gif','.ogg','.vob','.flv','webm','.ogv','.mov','.3gp','.m4v']:
                if i.lower().endswith(s):
                    result['files'].append({'name':i,'type':'video'})
            for s in ['.mp3','.wav','.m4a','.ogg','.wma','.mp4a']:
                if i.lower().endswith(s):
                    result['files'].append({'name':i,'type':'audio'})
            if i.lower().endswith('.py'):
                result['files'].append({'name':i,'type':'python'})
            if i.lower().endswith('.txt'):
                result['files'].append({'name':i,'type':'txt'})
            if i.lower().endswith('.js'):
                result['files'].append({'name':i,'type':'javascript'})
            if i.lower().endswith('.json'):
                result['files'].append({'name':i,'type':'json'})
            if i.lower().endswith('.php'):
                result['files'].append({'name':i,'type':'php'})
            if i.lower().endswith('.pdf'):
                result['files'].append({'name':i,'type':'pdf'})
            recongnized = False
            for f in result['files']:
                if i == f['name']:
                    recongnized = True
                    break
            if not recongnized:
                result['files'].append({'name':i,'type':'file'})
        else:
            result['unknowns'].append({'name':i,'type':'unknown'})
    return result


                