// In the name of Allah

var langs = ['','xml','css','javascript','markdown','python','php']
var themes = ['monokai','isotope','cobalt','eclipse','neat']

var editor = CodeMirror.fromTextArea(document.getElementById('content'),{
    lineNumbers: true,
    theme: 'monokai',
    mode: langs[document.getElementById('type').options.selectedIndex],
    lineWrapping: true
});

editor.setSize('auto',330);

editor.setOption('keymap','sublime');

document.getElementById('type').addEventListener('change', function () {
    editor.setOption('mode', langs[document.getElementById('type').options.selectedIndex])
});

document.getElementById('theme').addEventListener('change', function () {
    editor.setOption('theme', themes[document.getElementById('theme').options.selectedIndex])
})

switch (document.getElementById('name').value.split('.').pop()) {
    case 'js':
        editor.setOption('mode','javascript');
        document.querySelector('option[value=javascript]').setAttribute('selected',null);
        break;
    case 'json':
        editor.setOption('mode','javascript');
        document.querySelector('option[value=javascript]').setAttribute('selected',null);
        break;
    case 'html':
        editor.setOption('mode','xml');
        document.getElementById('xml').setAttribute('selected',null)
        break;
    case 'htm':
        editor.setOption('mode','xml');
        document.querySelector('option[value=xml]').setAttribute('selected',null);
        break;
    case 'xml':
        editor.setOption('mode','xml');
        document.querySelector('option[value=xml]').setAttribute('selected',null);
        break;
    case 'css':
        editor.setOption('mode','css');
        document.querySelector('option[value=css]').setAttribute('selected',null);
        break;
    case 'sass':
        editor.setOption('mode','css');
        document.querySelector('option[value=css]').setAttribute('selected',null);
        break;
    case 'scss':
        editor.setOption('mode','css');
        document.querySelector('option[value=css]').setAttribute('selected',null);
        break;
    case 'less':
        editor.setOption('mode','css');
        document.querySelector('option[value=css]').setAttribute('selected',null);
        break;
    case 'md':
        editor.setOption('mode','markdown');
        document.querySelector('option[value=markdown]').setAttribute('selected',null);
        break;
    case 'py':
        editor.setOption('mode','python');
        document.querySelector('option[value=python]').setAttribute('selected',null);
        break;
    case 'php':
        editor.setOption('mode','php');
        document.querySelector('option[value=php]').setAttribute('selected',null);
        break;
    default:
        editor.setOption('mode','');
}