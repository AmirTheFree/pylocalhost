// In the name of Allah

document.getElementById('menu').style = 'display: none;';

document.addEventListener('click',function (e){
    document.getElementById('menu').style = 'display: none;';
},false);

function startNoteBook(path) {
    if (jupyter == '0'){
        alert('Jupyter is not installed');
        return 'Jupyter is not installed';
    };
    var ajax = new XMLHttpRequest();
    ajax.open('GET',path + '?notebook=true',true);
    ajax.send();
};

function stopNoteBook() {
     if (jupyter == '0'){
        alert('Jupyter is not installed');
        return 'Jupyter is not installed';
    };
    var ajax = new XMLHttpRequest();
    ajax.open('GET',rp + 'stopjupyter/',true);
    ajax.send();
}

function sysopen(path) {
    var ajax = new XMLHttpRequest();
    ajax.open('GET', path + '?sysopen=true', true);
    ajax.send();
};

function createFolder() {
    var folder_name = prompt('Enter a name for new folder:');
    if (folder_name){
        location.href = rp + '/newfolder/?path=' + p + '&name=' + folder_name;
    };
};

document.getElementById('del').addEventListener('click',function (e){
    result = confirm('Are you sure?');
    if (!result){
        e.preventDefault();
        return false;
    };
});

function rightclick(element, event) {
    var menu = document.getElementById('menu');
    document.getElementById('titr').innerText = element.firstElementChild.innerText;
    document.getElementById('del').setAttribute('href',rp + element.firstElementChild.getAttribute('href') + '?rm=true');
    document.getElementById('run').setAttribute('href',rp + element.firstElementChild.getAttribute('href') + '?run=true');
    document.getElementById('dl').setAttribute('href',rp + '/d' + element.firstElementChild.getAttribute('href').slice(0,-1));
    document.getElementById('src').setAttribute('href',rp + '/t' + element.firstElementChild.getAttribute('href').slice(0,-1));
    document.getElementById('edit').setAttribute('href',rp + '/editor?path=' + p + '&file=' + element.firstElementChild.innerText)
    // Button functions
    function systemredirector(e){
        this.setAttribute('disabled','disabled');       
        sysopen(rp + element.firstElementChild.getAttribute('href'));
    };
    function renamer(e) {
        this.setAttribute('disabled','disabled');
        newName = prompt('Enter a new name:',element.firstElementChild.innerText);
        if (newName) {
            location.href = rp + '/rename/?path=' + p + '&name=' + element.firstElementChild.innerText + '&new=' + newName;
        };
    };
    // Rebuild oss button
    var old_oos = document.getElementById('oos');
    var new_oos = old_oos.cloneNode(true);
    old_oos.parentNode.replaceChild(new_oos,old_oos);
    old_oos.remove();
    document.getElementById('oos').addEventListener('click',systemredirector);
    document.getElementById('oos').removeAttribute('disabled');
    // Rebuild rename button
    var old_rename = document.getElementById('rename');
    var new_rename = old_rename.cloneNode(true);
    old_rename.parentNode.replaceChild(new_rename, old_rename);
    old_rename.remove();
    document.getElementById('rename').addEventListener('click',renamer);
    document.getElementById('rename').removeAttribute('disabled');
    menu.setAttribute('class','menu');
    menu.style = 'top: ' + event.pageY + 'px;left: ' + event.pageX + 'px;';
};

var cls = ['a', 'b', 'c', 'd', 'e', 'f'];
var index = 0;

var items = document.getElementsByClassName('col');

for (let i = 0; i < items.length; i++) {
    items[i].classList.add(cls[index]);
    items[i].addEventListener('contextmenu', function (e) {
        rightclick(items[i], e);
        e.preventDefault()
    },false);
    (index == 5) ? index = 0 : index += 1;
};
