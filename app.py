# In the name of Allah

from flask import Flask, abort, render_template, request, jsonify, redirect
import os
import forms
import mwxpy
import subprocess

home = mwxpy.rwjson('info.json')['home']
python = mwxpy.rwjson('info.json')['python']
notebooks = []

app = Flask(__name__)
app.config['SECRET_KEY'] = mwxpy.rwjson('info.json')['secret']

@app.before_request
def check_host():
    host = mwxpy.rwjson('info.json')['host']

    if not host:
        if not ((request.host == 'localhost' and request.url.split('/')[2]) == 'localhost' or (request.host == '127.0.0.1' and request.url.split('/')[2] == '127.0.0.1')):
            abort(403)


@app.route('/about/', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/help/', methods=['GET'])
def guid():
    if request.args.get('fa') == 'true':
        return render_template('komak.html')
    return render_template('help.html')


@app.route('/config/', methods=['GET','POST'])
def settings():
    if not ((request.host == 'localhost' and request.url.split('/')[2]) == 'localhost' or (request.host == '127.0.0.1' and request.url.split('/')[2] == '127.0.0.1')):
            abort(403)
    inf = mwxpy.rwjson('info.json')
    if request.method == 'POST':
        form = forms.SettingsForm(request.form)
        if not form.validate_on_submit():
            abort(400)
        inf['host'] = True if form.host.data == '1' else False
        inf['show_hidden_files'] = True if form.show_hidden_files.data == '1' else False
        mwxpy.rwjson('info.json',inf)
        
    form = forms.SettingsForm()
    data = {'host':'1' if inf['host'] else '0','show_hidden_files': '1' if inf['show_hidden_files'] else '0'}
    return render_template('settings.html',form=form,data = data)

@app.route('/stopjupyter/', methods =['GET'])
def kill():
    if not ((request.host == 'localhost' and request.url.split('/')[2]) == 'localhost' or (request.host == '127.0.0.1' and request.url.split('/')[2] == '127.0.0.1')):
        abort(403)
    for n in notebooks:
        env = dict(os.environ)
        env['DISPLAY'] = ":0"
        subprocess.Popen(f'pkill -P {n.pid} && kill -9 {n.pid} && killall jupyter',env=env,shell=True)
    return 'Done!',200

@app.route('/', defaults={'p': ''})
@app.route('/<path:p>/', methods=['GET'])
def explorer(p):
    root = os.path.join(home, 'Pylocalhost')
    path = os.path.join(root, p)
    show_hidden_files = mwxpy.rwjson('info.json')['show_hidden_files']
    if request.args.get('dl') == 'true':
        return redirect(f'http://{request.host}/d/' + p)
    if request.args.get('run') == 'true':
        if not ((request.host == 'localhost' and request.url.split('/')[2]) == 'localhost' or (request.host == '127.0.0.1' and request.url.split('/')[2] == '127.0.0.1')):
            abort(403)
        if p.lower().endswith('.py'):
            try:
                return '<span style="color:green;">Python script ran successsfully here is the output:</span><br><br>' + os.popen(f'{python} {home}/Pylocalhost/{p}').read(),200
            except:
                return '<span style="color:red;">Could not run script successfully!</span>',500
        elif p.lower().endswith('.js'):
            if not os.popen('which node').read().startswith('/'):
                return '<span style="color:red;">You don\'t have NodeJS installed on your system!</span>'
            try:
                return '<span style="color:green;">Javascript ran successfully here is the output:</span><br><br>' + os.popen(f'node {home}/Pylocalhost/{p}').read(),200
            except:
                return '<span style="color:red;">Could not run script successfully!</span>',500
        else:
            return '<span style="color: red;">PyLocalHost is only able to run Javascript or Python scripts</span>',400
        
    if request.args.get('sysopen') == 'true':
        if not ((request.host == 'localhost' and request.url.split('/')[2]) == 'localhost' or (request.host == '127.0.0.1' and request.url.split('/')[2] == '127.0.0.1')):
            abort(403)
        try:
            env = dict(os.environ)
            env['DISPLAY'] = ":0"
            subprocess.Popen(f'xdg-open {path}',env=env,shell=True)
            return 'Requesting from system was successful',200
        except:
            return 'Requesting from system was not successful',500
    if request.args.get('rm') == 'true':
        if not ((request.host == 'localhost' and request.url.split('/')[2]) == 'localhost' or (request.host == '127.0.0.1' and request.url.split('/')[2] == '127.0.0.1')):
            abort(403)
        try:
            os.popen(f'rm -rf {path}')
            return redirect(f'http://{request.host}/' + p + '/../')
        except:
            return 'Requesting from system was not successful',500
    if os.path.isdir(path) or os.path.ismount(path):
        if request.args.get('notebook') == 'true':
            if not ((request.host == 'localhost' and request.url.split('/')[2]) == 'localhost' or (request.host == '127.0.0.1' and request.url.split('/')[2] == '127.0.0.1')):
                abort(403)
            try:
                env = dict(os.environ)
                env['DISPLAY'] = ":0"
                x = subprocess.Popen(f'cd {path} && /etc/pylocalhost/.venv/bin/jupyter notebook',env=env,shell=True)
                notebooks.append(x)
                return 'Requesting from system was successfull',200
            except:
                return 'Requesting from system was not successfull!',500
        if request.args.get('srvdir') == 'true':
            return redirect(f'http://{request.host}/s/' + p)
        ls = mwxpy.browse(path,show_hidden_files)
        return jsonify(ls) if request.args.get('api') == 'true' else render_template('explorer.html', ls=ls, p=p, rp = f'http://{request.host}' )
    elif os.path.isfile(path) or os.path.islink(path):
        return redirect(f'http://{request.host}/s/' + p)
    else:
        return render_template('404.html',p=p),404

@app.route('/editor/', methods = ['GET', 'POST'])
def editor():
    if not ((request.host == 'localhost' and request.url.split('/')[2]) == 'localhost' or (request.host == '127.0.0.1' and request.url.split('/')[2] == '127.0.0.1')):
            abort(403)
    if not isinstance(request.args.get('path',False),str):
        abort(400)
    form = forms.FileForm()
    if request.args.get('file',False):
        form = forms.FileForm()
        form.name.data = request.args['file']
        form.content.data = mwxpy.rwfile(os.path.join(home,'Pylocalhost',request.args['path'],request.args['file']))
    if request.method == 'POST':
        form = forms.FileForm(request.form)
        if not form.validate_on_submit():
            abort(400)
        try:
            mwxpy.rwfile(os.path.join(home,'Pylocalhost',request.args['path'],form.name.data),form.content.data)
            return redirect(f'http://{request.host}/' + request.args['path'])
        except:
            return '<span style="font-weight:bold;color:red;">An Error occurred while saving file!</span>'

    return render_template('editor.html',form = form)