# PyLocalhost
## A server for serving and rendering files in localhost 

**_In the name of Allah_**

### Description

This is a web-based file explorer and its root path is your ~/Pylocalhost directory. It is useful for serving HTML files,Ajax and every thing that need a webserver.Its file explorer has a sweet GUI.Its simple and lightweight! Enjoy :)

We try to make it better. You can help us too! how? by submitting your issues (if you have) or making pull requests!

### Installtion

Before installtion you need: nginx , git & wget

If you don't have them try installing theme
(exmaple for Ubuntu):

`$ sudo apt install nginx git wget`

Then download the file `installer.py` file which is in the repository.

You can download it from [here](https://raw.githubusercontent.com/mwxgaf/pylocalhost/master/installer.py)

Or you can get it from terminal using wget:

`$ wget https://raw.githubusercontent.com/mwxgaf/pylocalhost/master/installer.py`

Or you can clone whole repository (Not recommended):

`$ git clone https://github.com/mwxgaf/pylocalhost.git`

After that just run the file with **python 3** under sudo:

`$ sudo python installer.py`

Or maybe in some OSs you must run:

`$ sudo python3 installer.py`

It will show you details. If installtion was unsuccessful please submit an issue including details and your system info.

### Usage
Very easy! just run:

`$ sudo systemctl enable --now gunicorn nginx`

And then open localhost (localhost itsself or 127.0.0.1) and then enjoy! :)

If did not work:

`$ sudo systemctl restart gunicorn nginx`

NOTE: This part will be better in upcoming updates.

### Update

To be honest, the installer is uninstaller and insaller! So follow the installion process to update the software!

### Info

***Used tools:***

* Python
* HTML
* CSS
* JavaScript
* JSON
* Jquery
* Jinja
* Shell script
* Nginx
* Gunicorn
* Flask

#### Be comfortable to submit pull requests and issues :)

**In development ...**


