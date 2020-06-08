# PyLocalhost
## A server for serving and rendering files in localhost + some interesting options

**_In the name of Allah_**

### Description

This is a web-based file explorer and its root path is your `~/Pylocalhost` directory. It is useful for serving HTML files,Ajax,PHP and every thing that needs a webserver.Its file explorer has a sweet GUI.Its simple and lightweight! Enjoy! :heavy_check_mark: 

![GUI](https://raw.githubusercontent.com/mwxgaf/pylocalhost/master/static/image/explorer.png)
![404](https://raw.githubusercontent.com/mwxgaf/pylocalhost/master/static/image/404.png)

We try to make it better. You can help us too! How? By submitting your issues (if you have) or making pull requests!

### Installtion

Before installtion you need: `nginx` & `git`

If you don't have them try installing theme
(Exmaple for Ubuntu):

`$ sudo apt install nginx git`

If you want Pylocalhost to serve and render PHP files you will also need `php-fpm` Version 7.0 or higher(Exmaple for Ubuntu):

`$ sudo add-apt-repository ppa:ondrej/php`

`$ sudo apt update`

`$ sudo apt install php7.4 php7.4-fpm php7.4-mysql php7.4-imagick php7.4-cli php7.4-xmlrpc php7.4-gd php7.4-tidy php7.4-recode`

`$ sudo systemctl enable --now php7.4-fpm`

Then download `installer.py` file which is in the repository.

You can get it from terminal using wget:

`$ wget https://raw.githubusercontent.com/mwxgaf/pylocalhost/master/installer.py`

After that just run the file with **python 3** under sudo:

`$ sudo python installer.py`

In some OSs may be you must type `python3` instead of `python`

It will show you details. If installtion was unsuccessful please submit an issue including details and your system info.

### Usage

Run:

`$ sudo pylh enable`

And then:

`$ sudo pylh start`

Then go to [http://localhost](http://localhost)

It will show you anything which is in `~/Pylocalhost` and always it will start automatically when you turn your computer on :heavy_check_mark: 

Just this! :heavy_check_mark: 

NOTE : Pylocalhost will return you a JSON api including info of contents of a directory if you add ?api=ture at the end of directory urls.

For example:

`http://localhost/folder1/folder2/`(Returns the GUI file manager) --> `http://localhost/folder1/folder2/?api=true`(Returns JSON)

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
    * Jinja
    * GUnicorn
* HTML
* CSS
* JavaScript
    * JSON
* Bash script
* Nginx

_Made by an Iranian_ :iran:

#### Be comfortable to submit pull requests and issues :heavy_check_mark: 