#!/bin/bash

# In the name of Allah
if [ ! "$1" ]
then 
    echo -e "\nNo command received!\nRun 'pylh help' for help\n"
elif [ "$1" == "start" ]
then
    systemctl start gunicorn nginx
elif [ "$1" == "stop" ]
then
    systemctl stop gunicorn nginx
elif [ "$1" == "restart" ]
then
    systemctl daemon-reload && systemctl restart gunicorn nginx
elif [ "$1" == "disable" ]
then
    systemctl disable gunicorn nginx
elif [ "$1" == "enable" ]
then
    systemctl enable gunicorn nginx
elif [ "$1" == "password" ]
then
    sudo etc/pylocalhost/.venv/bin/python /etc/pylocalhost/password.py
elif [[ "$1" == "help" || "$1" == "?" ]]
then
    echo -e "In the name of Allah\n\nPyLocalhost v1.5\n\nWebsite: https://mwxgaf.github.io/pylocalhost\nEmail: i@mwxg.ir\n\nUsage: pylh <command>\n\nCommands:\n  start --> Start Pylocalhost\n  stop --> Stop Pylocalhost\n  restart --> Reload config files & restart Pylocalhost\n  enable --> Enable run as startup for Pylocalhost\n  disable --> Disable run as startup for Pylocalhost and probably stop it\n  password --> See your password\n  help --> Show this help\n  ? --> Show this help\n\nBy: Amirreza Aliakbari (MWX)\nWebsite: i.mwxg.ir\nEmail: i@mwxg.ir"
else
    echo -e "\nInvalid command!\nRun 'pylh help' for help\n"
fi
