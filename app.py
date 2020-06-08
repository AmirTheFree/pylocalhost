# In the name of Allah

from flask import Flask, abort, render_template, request, jsonify, redirect, json
import os
import tools
import forms


home = tools.info_file()['home']    

app = Flask(__name__)
app.config['SECRET_KEY'] = tools.info_file()['secret']

@app.before_request
def check_host():
    host = tools.info_file()['host']

    if not host:
        if not ((request.host == 'localhost' and request.url.split('/')[2]) == 'localhost' or (request.host == '127.0.0.1' and request.url.split('/')[2] == '127.0.0.1')):
            abort(403)


@app.route('/about/', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/help/', methods=['GET'])
def guid():
    print(request.url)
    return render_template('help.html')


@app.route('/settings/', methods=['GET','POST'])
def settings():
    if not ((request.host == 'localhost' and request.url.split('/')[2]) == 'localhost' or (request.host == '127.0.0.1' and request.url.split('/')[2] == '127.0.0.1')):
            abort(403)
    inf = tools.info_file()
    if request.method == 'POST':
        form = forms.SettingsForm(request.form)
        if not form.validate_on_submit():
            abort(400)
        inf['host'] = True if form.host.data == '1' else False
        tools.info_file(inf)
        
    form = forms.SettingsForm()
    data = {'host':'1' if inf['host'] else '0'}
    return render_template('settings.html',form=form,data = data)


@app.route('/', defaults={'p': ''})
@app.route('/<path:p>/', methods=['GET'])
def explorer(p):
    root = os.path.join(home, 'Pylocalhost')
    path = os.path.join(root, p)
    if os.path.isdir(path) or os.path.ismount(path):
        ls = tools.browser(path)
        return jsonify(ls) if request.args.get('api') == 'true' else render_template('explorer.html', ls=ls, title=os.path.basename(path), p=p)
    elif os.path.isfile(path) or os.path.islink(path):
        return redirect('http://localhost/s/' + p)
    else:
        return render_template('404.html',p=p)
