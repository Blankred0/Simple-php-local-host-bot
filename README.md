# Simple-PHP-Local-Host-Bot
This is a simple local host for PHP written in Python.
To use it, download the file `bot.py` and place it in the folder that contains your PHP file.
Navigate to your/folder/path in the terminal and then run `python3 bot.py`. It will generate a link for you to view your PHP file in your web browser.
Press Enter to stop the server and 'C' to clear the terminal.
I've just added serveo so it's a little buggy but it works.
You can choose the subdomain by genrating a ssh key with this command :
$ ssh-keygen

Otherwhise the choose subdomain won't work and he choose you a random subdomain.


#Tip: Make sure you have PHP installed on your computer. :)
For serveo make sure you have open ssh installed.
If you don't have open ssh installed run the folowing command :

For ubutu it's : 
sudo apt-get update 

sudo apt-get install openssh-server
