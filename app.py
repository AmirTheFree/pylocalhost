# In the name of Allah

from flask import Flask, abort, render_template, request, jsonify, redirect, json
import os
import tools

info_fp = open('info.json')
home = json.load(info_fp)['home']
info_fp.close()

app = Flask(__name__)


@app.route('/about/', methods=['GET'])
def about():
    return 'about us page will be here ...'  # TODO make about page


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
        return abort(404)  # TODO render a custom 404 error page instead
