# PyLocalhost
## A server for serving and rendering files in localhost 

**_In the name of Allah_**

### Description

This is a web-based file explorer and its root path is your ~/Pylocalhost directory. It is useful for serving HTML files,Ajax and every thing that need a webserver.Its file explorer has a sweet GUI.Its simple and lightweight! Enjoy! :white_check_mark:

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

Run:

`$ sudo pylh enable`

And then:

`$ sudo pylh start`

Then go to [http://localhost](http://localhost)

It will show you anything which is in ~/Pylocalhost and always it will start automaticaly when you turn your computer on :white_check_mark:

Just this! :white_check_mark:

A little more about PyLH CLI:

`$ sudo pylh <command>`

Commands: 

* start --> Start Pylocalhost
* stop --> Stop Pylocalhost
* restart --> Reload config files & restart Pylocalhost
* enable --> Enable run as start up for Pylocalhost
* disable --> Disable run as start up for Pylocalhost
* help --> Show help
* ? --> Show help

### Update

To be honest, the installer is uninstaller and insaller! So follow the installion process to update the software!

### Info

***Used tools:***

* Python
    * Flask
    * Gunicorn
    * Jinja
* HTML
* CSS
* JavaScript
    * JSON
    * Jquery
* Bash script
* Nginx

_Made by an Iranian_ :iran:

#### Be comfortable to submit pull requests and issues :white_check_mark:


