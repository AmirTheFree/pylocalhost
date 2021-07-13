**_In the name of Allah_**

## Description

This is a web-based file explorer and its root path is your `~/Pylocalhost` directory. It is useful for serving HTML files,Ajax,PHP and every thing that needs a webserver.Its file explorer has a sweet GUI.Its simple and lightweight! Enjoy!

![home](https://raw.githubusercontent.com/mwxgaf/pylocalhost/gh-pages/home.png)
![editor](https://raw.githubusercontent.com/mwxgaf/pylocalhost/gh-pages/editor.png)

We try to make it better. You can help us too! How? By submitting your issues (if you have) or making pull requests!

## Prerequisites

Before installtion you need: `nginx` & `git`

If you don't have them try installing theme
(Exmaple for Ubuntu):

`$ sudo apt install nginx git`

If you want Pylocalhost to serve and render PHP files you will also need `php-fpm` Version 7.0 or higher(Exmaple for Ubuntu):

`$ sudo apt install php8.0 php8.0-fpm`

`$ sudo systemctl enable --now php8.0-fpm`

## Installation

Download `preinstaller.py` file from [here](https://github.com/mwxgaf/pylocalhost/releases/download/v1.5/preinstaller.py)

After that just run the file with **python 3**:

`$ python3 preinstaller.py`

In some OSs may be you must type `python` instead of `python3`

Then run the `installer.py` file(it will be created once you ran `preinstaller.py`) with **python 3** under **sudo**:

`$ sudo python3 installer.py`

It will show you details. If installation was unsuccessful please submit an issue including details and your system info.

*For installing Beta versin view the README.md in repository*

## Usage

Run:

`$ sudo pylh enable`

And then:

`$ sudo pylh start`

Then go to [http://localhost](http://localhost)

It will show you anything which is in `~/Pylocalhost` and always it will start automatically when you turn your computer on

Just this!

_**This descriptions are for starting using PyLocalHost. In user manual page(which is in PyLocalHost) you can learn using PyLocalHosts futures and options**_.

## Update

To be honest, the installer is uninstaller and insaller! So follow the installation process to update the software!

And then run:(to prevent possible problems):

`$ sudo pylh restart`

## Info

***Used tools:***

* Python
    * Flask
    * Jinja
    * GUnicorn
    * [MWXpy](https://github.com/mwxgaf/mwxpy)
* HTML
* CSS
* JavaScript
    * JSON
* Bash script
* Nginx

_Made in Iran_ 🇮🇷

#### Be comfortable to submit pull requests and issues

## About Us

Founder : Amirreza Aliakbari (MWX)

Website : [mwxgaf.ir](http://mwxgaf.ir)

Email : [mwxgaf@yahoo.com](mailto:mwxgaf@yahoo.com)
