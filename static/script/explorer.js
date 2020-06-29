// In the name of Allah

document.getElementById('menu').style = 'display: none;';

document.addEventListener('click',function (e){
    document.getElementById('menu').style = 'display: none;';
},false);

function sysopen(path) {
    var ajax = new XMLHttpRequest();
    ajax.open('GET', path + '?sysopen=true', true);
    ajax.send();
};

function rightclick(element, event) {
    var menu = document.getElementById('menu');
    document.getElementById('titr').innerText = element.firstElementChild.innerText;
    document.getElementById('del').setAttribute('href',cp + element.firstElementChild.getAttribute('href') + '?rm=true');
    document.getElementById('run').setAttribute('href',cp + element.firstElementChild.getAttribute('href') + '?run=true');
    document.getElementById('dl').setAttribute('href',rp + 'd' + element.firstElementChild.getAttribute('href').slice(0,-1));
    function systemredirector(e){
        this.setAttribute('disabled','disabled');       
        sysopen(cp + element.firstElementChild.getAttribute('href'));
    };
    var old_oos = document.getElementById('oos');
    var new_oos = old_oos.cloneNode(true);
    old_oos.parentNode.replaceChild(new_oos,old_oos);
    old_oos.remove();
    document.getElementById('oos').addEventListener('click',systemredirector);
    document.getElementById('oos').removeAttribute('disabled');
    menu.setAttribute('class','menu')
    menu.style = 'top: ' + event.pageY + 'px;left: ' + event.pageX + 'px;';
};

var cls = ['a', 'b', 'c', 'd', 'e', 'f', 'g'];
var index = 0;

var items = document.getElementsByClassName('col');

for (let i = 0; i < items.length; i++) {
    items[i].classList.add(cls[index]);
    items[i].addEventListener('contextmenu', function (e) {
        rightclick(items[i], e);
        e.preventDefault()
    },false);
    (index == 6) ? index = 0 : index += 1;
};
