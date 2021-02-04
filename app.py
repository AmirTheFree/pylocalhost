# In the name of Allah

from flask import Flask, abort, render_template, request, jsonify, redirect, session,g
from datetime import timedelta
import os
import forms
import mwxpy
import subprocess
import hashlib
import utils

home = mwxpy.rwjson('info.json')['home']
python = mwxpy.rwjson('info.json')['python']
password = mwxpy.rwjson('info.json')['password']
h = hashlib.sha256()
h.update(password.encode('utf-8'))
notebooks = []
dangerous_ips = []

app = Flask(__name__)
app.config['SECRET_KEY'] = mwxpy.rwjson('info.json')['secret']


@app.before_request
def security_check():
    if request.environ.get('HTTP_X_FORWARDED_FOR') in [None,'']:
        g.ip = request.remote_addr
    else:
        g.ip = request.environ['HTTP_X_FORWARDED_FOR']

    ips = mwxpy.rwjson('info.json')['ips']
    if g.ip in ips:
        abort(403)

    host = mwxpy.rwjson('info.json')['host']
    if not host:
        if session.get('id', False) != h.hexdigest():
            abort(403)


@app.before_request
def information_setup():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=3650)


@app.route('/about/', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/help/', methods=['GET'])
def guid():
    if request.args.get('fa') == 'true':
        return render_template('komak.html')
    return render_template('help.html')


@app.route('/config/', methods=['GET', 'POST'])
@utils.secure_api
def settings():
    inf = mwxpy.rwjson('info.json')
    if request.method == 'POST':
        form = forms.SettingsForm(request.form)
        if not form.validate_on_submit():
            abort(400)
        inf['host'] = True if form.host.data == '1' else False
        inf['show_hidden_files'] = True if form.show_hidden_files.data == '1' else False
        inf['theme'] = form.theme.data
        mwxpy.rwjson('info.json', inf)
        return redirect(f'http://{request.host}')

    form = forms.SettingsForm()
    data = {'host': '1' if inf['host'] else '0', 'show_hidden_files':
            '1' if inf['show_hidden_files'] else '0', 'theme': inf['theme']}
    return render_template('settings.html', form=form, data=data)


@app.route('/stopjupyter/', methods=['GET'])
@utils.secure_api
def kill():
    for n in notebooks:
        env = dict(os.environ)
        env['DISPLAY'] = ":0"
        subprocess.Popen(
            f'pkill -P {n.pid} && kill -9 {n.pid} && killall jupyter', env=env, shell=True)
    return 'Done!', 200


@app.route('/', defaults={'p': ''})
@app.route('/<path:p>/', methods=['GET'])
def explorer(p):
    root = os.path.join(home, 'Pylocalhost')
    path = os.path.join(root, p)
    show_hidden_files = mwxpy.rwjson('info.json')['show_hidden_files']
    jupyter_installed = '1' if mwxpy.rwjson(
        'info.json')['jupyter_installed'] else '0'
    if request.args.get('dl') == 'true':
        return redirect(f'http://{request.host}/d/' + p)
    if request.args.get('run') == 'true':
        if session.get('id', False) != h.hexdigest():
            abort(403)
        if p.lower().endswith('.py'):
            try:
                return '<span style="font-weight:bold;color:green;">Python script ran successsfully here is the output:</span><br><br>' + os.popen(f'{python} {home}/Pylocalhost/{p}').read(), 200
            except:
                return '<span style="font-weight:bold;color:red;">Could not run script successfully!</span>', 500
        elif p.lower().endswith('.js'):
            if not os.popen('which node').read().startswith('/'):
                return '<span style="font-weight:bold;color:red;">You don\'t have NodeJS installed on your system!</span>'
            try:
                return '<span style="font-weight:bold;color:green;">Javascript ran successfully here is the output:</span><br><br>' + os.popen(f'node {home}/Pylocalhost/{p}').read(), 200
            except:
                return '<span style="font-weight:bold;color:red;">Could not run script successfully!</span>', 500
        else:
            return '<span style="font-weight:bold;color: red;">PyLocalHost is only able to run Javascript or Python scripts</span>', 400

    if request.args.get('sysopen') == 'true':
        if session.get('id', False) != h.hexdigest():
            abort(403)
        try:
            env = dict(os.environ)
            env['DISPLAY'] = ":0"
            subprocess.Popen(f'xdg-open {path}', env=env, shell=True)
            return 'Requesting from system was successful', 200
        except:
            return 'Requesting from system was not successful', 500
    if request.args.get('rm') == 'true':
        if session.get('id', False) != h.hexdigest():
            abort(403)
        try:
            os.popen(f'rm -rf {path}')
            return redirect(f'http://{request.host}/' + p + '/../')
        except:
            return 'Requesting from system was not successful', 500
    if os.path.isdir(path) or os.path.ismount(path):
        if request.args.get('notebook') == 'true':
            if session.get('id', False) != h.hexdigest():
                abort(403)
            try:
                env = dict(os.environ)
                env['DISPLAY'] = ":0"
                x = subprocess.Popen(
                    f'cd {path} && /etc/pylocalhost/.venv/bin/jupyter notebook', env=env, shell=True)
                notebooks.append(x)
                return 'Requesting from system was successfull', 200
            except:
                return 'Requesting from system was not successfull!', 500
        if request.args.get('srvdir') == 'true':
            return redirect(f'http://{request.host}/s/' + p)
        ls = mwxpy.browse(path, show_hidden_files)
        return jsonify(ls) if request.args.get('api') == 'true' else render_template('explorer.html', ls=ls, p=p, rp=f'http://{request.host}', jupyter=jupyter_installed)
    elif os.path.isfile(path) or os.path.islink(path):
        return redirect(f'http://{request.host}/s/' + p)
    else:
        return render_template('404.html', p=p), 404


@app.route('/editor/', methods=['GET', 'POST'])
@utils.secure_api
def editor():
    if not isinstance(request.args.get('path', False), str):
        abort(400)
    form = forms.FileForm()
    if request.args.get('file', False):
        form = forms.FileForm()
        form.name.data = request.args['file']
        form.content.data = mwxpy.rwfile(os.path.join(
            home, 'Pylocalhost', request.args['path'], request.args['file']))
    if request.method == 'POST':
        form = forms.FileForm(request.form)
        if not form.validate_on_submit():
            abort(400)
        try:
            mwxpy.rwfile(os.path.join(
                home, 'Pylocalhost', request.args['path'], form.name.data), form.content.data)
            return redirect(f'http://{request.host}/' + request.args['path'])
        except:
            return '<span style="font-weight:bold;color:red;">An Error occurred while saving file!</span>'
    inf = mwxpy.rwjson('info.json')
    return render_template('editor.html', form=form, theme=inf['theme'])


@app.route('/newfolder/', methods=['GET'])
@utils.secure_api
def new_folder():
    if not isinstance(request.args.get('path', False), str) or not request.args.get('name', False):
        abort(400)
    try:
        os.mkdir(os.path.join(home, 'Pylocalhost',
                              request.args['path'], request.args['name']))
        return redirect(f'http://{request.host}/' + request.args['path'])
    except:
        return '<span style="font-weight:bold;color:red;">An Error occurred while creating folder!</span>'


@app.route('/rename/', methods=['GET'])
@utils.secure_api
def rename():
    if not isinstance(request.args.get('path', False), str) or not request.args.get('name', False) or not request.args.get('new', False):
        abort(400)
    try:
        os.rename(os.path.join(home, 'Pylocalhost', request.args['path'], request.args['name']), os.path.join(
            home, 'Pylocalhost', request.args['path'], request.args['new']))
        return redirect(f'http://{request.host}/' + request.args['path'])
    except:
        return '<span style="font-weight:bold;color:red;">An Error occurred while renaming item</span>'


@app.route('/login/', methods=['GET'])
def login():
    if session.get('id', False) != h.hexdigest():
        if request.args.get('pw', False):
            if str(request.args['pw']) == password:
                for i in dangerous_ips:
                    if i.address == g.ip:
                        dangerous_ips.remove(i)
                H = hashlib.sha256()
                H.update(str(request.args['pw']).encode('utf-8'))
                session['id'] = H.hexdigest()
                return '<head><meta http-equiv="refresh" content="3;url=http://pylh/"></head><body><h1 style="color:green;">Login Successful! Redirecting ...</h1></body>'
            else:
                for i in dangerous_ips:
                    if i.address == g.ip:
                        if i.register_attemp():
                            dangerous_ips.remove(i)
                        abort(401)
                dangerous_ips.append(utils.DangerousIP(g.ip))
                abort(401)
        else:
            return render_template('login.html')
    else:
        return 'You are already logged in <a href="http://pylh">Back to home</a>'