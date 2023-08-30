# Simple-PHP-Local-Host-Bot
This is a simple local host for PHP written in Python.
To use it, run the command who follow and place your PHP file in the folder of bot.py. The file MUST BE NAMED index.php or serveo can bug and didn't find your file. I placed a index.php file in the the repositories so after testing if everything work please delete it and replace with your php file.
```bash
git clone https://github.com/Blankred0/Simple-php-local-host-bot
cd Simple-php-local-host-bot/
python3 bot.py
```
It will generate a link for you to view your PHP file in your web browser.
Press Enter to stop the server and 'C' to clear the terminal.
I've just added serveo so it's a little buggy but it works.
You can avoid your server to crash with `sleep.py` because it refresh the page every 2 min. Run :
```bash
python3 sleep.py  
https://yoursubdomain.serveo.net/
```

You can choose the subdomain by genrating a ssh key with this command :
`ssh-keygen`

Otherwhise the choose subdomain won't work and he choose you a random subdomain.


#Tip: Make sure you have PHP and pyfiglet installed on your computer. :)
For pyfiglet it's `pip install pyfiglet`
For serveo make sure you have open ssh installed.
If you don't have open ssh installed run the folowing command :

For ubutu it's : 
```bash
sudo apt-get update 
sudo apt-get install openssh-server
```
#Disclaimer: This code is provided for educational purposes only. I am not responsible for any actions taken using this code.
