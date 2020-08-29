// In the name of Allah

var langs = ['','html','css','javascript','markdown','python','php']

var editor = CodeMirror.fromTextArea(document.getElementById('content'),{
    lineNumbers: true,
    theme: 'monokai',
    mode: langs[document.getElementById('type').options.selectedIndex]
});

document.getElementById('type').addEventListener('change',function () {
    editor.setOption('mode',langs[document.getElementById('type').options.selectedIndex])
});