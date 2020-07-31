# In the name of Allah

import os
import sys
import json

pylhinfo = {}

pylhinfo['user'] = os.getenv('USER')
pylhinfo['home'] = os.getenv('HOME')

fp = open('pylhinfo.json','w')
json.dump(pylhinfo,fp)

installer_download = os.popen('wget https://raw.githubusercontent.com/mwxgaf/pylocalhost/master/installer.py')
os.waitpid(installer_download._proc.pid,0)

if not os.path.isfile('installer.py'):
    print('Downloading installer was unsuccessful!')
    sys.exit(404)