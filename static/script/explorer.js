// In the name of Allah

var cls = ['a','b','c','d','e','f','g'];
var index = 0;

var items = document.getElementsByClassName('col');

for (let i = 0; i < items.length; i++) {
    items[i].classList.add(cls[index]);
    (index == 6) ? index = 0 : index += 1;   
};
