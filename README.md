# gotthegist
Get the gist of different sports

VMware Workstation
1.	New Virtual Machine with Ubuntu 14.04.1 amd 64 (Geng has copy on Desktop)
Username: gwang
Password: same
20GB – Single File, 2 core 2processors, 4096 MB
2.	Changes to gedit & make new directory for gotthegist http://learnpythonthehardway.org/book/ex0.html   
3.	Install pip and virtualenv 
a.	First check where python is installed by typing: $which python
i.	Should say: /usr/bin/python
b.	$ sudo apt-get install python-pip
c.	$ sudo pip install virtualenv
4.	Create Virtual Env in gotthegist dir
a.	$ cd gotthegist
b.	$ virtualenv env
c.	$ source ./env/bin/activate  
i.	This activates the virtualenv.  To deactivate just type “deactivate” 
5.	Install virtualenvwrapper  (https://www.youtube.com/watch?v=UcbUXq0wd-8) 
a.	$ deactivate #not needed if step 4 is skipped)
b.	$ cd 
c.	$ sudo pip install virtualenvwrapper
6.	Create a folder to contain all virtual environemnts:
a.	$ mkdir ~/.virtualenvs 
7.	Install Vim 
a.	$ sudo apt-get install vim
b.	Built in tutorial on how to use Vim = $ vimtutor
c.	Vim commands: http://www.computerhope.com/unix/vim.htm 
i.	To quit without saving =    :q!
ii.	To save and quit = ZZ 
iii.	To insert text = i
iv.	Go back to command mode = Esc
v.	Undo = u
vi.	Revert to saved version of file = :e!
vii.	Move around = h (left), j (down), k (up), l (right)
8.	Make developer directory
a.	$ mkdir Developer
9.	Update .bashrc file
a.	$ cd
b.	$ vim .bashrc
i.	Add this to the file:
1.	export WORKON_HOME=$HOME/.virtualenvs 
a.	# this will make a new directory that contains all your virtual environments
2.	export PROJECT_HOME=$HOME/Developer
3.	source /usr/local/bin/virtualenvwrapper.sh
ii.	Save file and exit out (Esc, ZZ)
c.	Activate the changes: 
i.	$ source .bashrc
ii.	Check that /.virtualenvs and /developer directories are made
1.	$ cd
2.	$ ls -a
10.	Create a new virtual environment
a.	$ mkvirtualenv gtgenv 
i.	To deactivate it’s still “deactivate”
ii.	To activate, all you need is “workon”
iii.	Note “gtgenv” is can be named anything.  I chose it to stand for “gotthegist environment”   
iv.	Useful Commands
1.	$ lsvirtualenv will list all the virtual environments
2.	$ rmvirtualenv ENVNAME will remove a virtual environment
3.	$ cdvirtualenv will take you to the directory of your virtualenv even if you are elsewhere. 
11.	Connect the virtual environment to the associated project directory
a.	$ workon gtgenv      #if you are not already in the virtual environment
b.	$ cd #return to home directory if not already there
c.	$ cd developer 
d.	$ mkdir gotthegist
e.	$ cd gotthegist
f.	$ setvirtualenvproject    #now everytime we type $workon gtgenv, we will automatically be taken to our project directory
g.	# you can test if this is working by deactivating and the doing workon
12.	Not sure if we need Distribute or nose but says to install them here: http://learnpythonthehardway.org/book/ex46.html 
a.	$ pip install Distribute  #makesure you are in the virtualenv
b.	$ pip install nose
13.	Install Django (in the virtual env)
a.	$ pip install django  #this will be installed in the virtualenv 
b.	Test:
i.	$ python
ii.	>>> from django import get_version
iii.	>>> get_version()
14.	Install PyCharm (http://linuxg.net/how-to-install-pycharm-3-4-on-ubuntu-14-04-linux-mint-17-pinguy-os-14-04-and-other-ubuntu-14-04-derivatives/) 
a.	$ wget -q -O - http://archive.getdeb.net/getdeb-archive.key | sudo apt-key add -
b.	$ sudo sh -c 'echo "deb http://archive.getdeb.net/ubuntu trusty-getdeb apps" >> /etc/apt/sources.list.d/getdeb.list'
c.	$ sudo apt-get update
d.	$ sudo apt-get install pycharm
15.	Install MySQL & MySQLdb (http://stackoverflow.com/questions/7459766/installing-mysql-python) 
a.	Check if mysql is already installed and running:
i.	$ ps aux | grep mysql
ii.	# if sql is running it will show something like:
1.	mysql 24294 0.1 1.3 550012….
b.	If mysql is not installed and running then do:
i.	$ sudo apt-get install mysql-server
ii.	$ mysqld   #to get the mysql server running 
iii.	$ sudo apt-get install mysql-client-5.5 mysql-server-5.5  
1.	Password: gothegist2015
16.	Configure MySQL to have a password
a.	$ mysql –u root
b.	Set up password:
i.	mysql> UPDATE mysql.user SET Password=PASSWORD(‘whateveryouwant’) WHERE User=’root’;
ii.	mysql> FLUSH PRIVILEGES;
iii.	quit:   mysql> \q 
c.	Create Database
i.	Log back into mysql:  $mysql –u root –p
ii.	mysql> CREATE DATABASE nameofdatabase;  #remember to include the ;
iii.	quit:   mysql> \q 
17.	Install pHpMyAdmin 
a.	$ sudo apt-get install php5-cli 
b.	 $ sudo apt-get update
c.	$ sudo apt-get install lamp-server^
d.	$ sudo apt-get install phpmyadmin     # make sure Apache 2 is checked in the dialog box that comes up	
i.	Choose “yes” for configure database for phpmyadmin with dbconfig-common
ii.	Use “gotthegist2015” for both passwords…
e.	$ sudo ln -s /etc/phpmyadmin/apache.conf /etc/apache2/conf-available/phpmyadmin.conf
f.	$ sudo a2enconf phpmyadmin
g.	$ sudo /etc/init.d/apache2 reload
h.	http://localhost/phpmyadmin
i.	https://help.ubuntu.com/community/phpMyAdmin 
i.	Login at: http://localhost/phpmyadmin
ii.	Username: root
iii.	Password: gotthegist2015

-------------------------------------------------------

18.	Create a new project in PyCharm 
a.	CD into directory you want the project to be in
b.	$ django-admin.py startproject gotthegist
i.	Accepted default settings: Script path: /usr/local/bin/charm
c.	Open up project in PyCharm
19.	Install MySQL-Python and mysqldb
a.	http://codeinthehole.com/writing/how-to-set-up-mysql-for-python-on-ubuntu/
b.	$ sudo apt-get install build-essential python-dev libmysqlclient-dev
c.	$ pip install MySQL-python
d.	$ sudo apt-get install python-mysqldb 
20.	Set up Django to work with MySQL database
a.	http://www.webforefront.com/django/setupdjangodatabase.html Open up settings.py 
b.	https://www.youtube.com/watch?v=9vX_0irE9Pc 
c.	Scroll down to databases
i.	‘ENGINE’: ‘django.db.backends.mysql’,
ii.	‘NAME’: ‘nameofdatabase’,
iii.	‘USER’: ‘root’,
iv.	‘PASSWORD’: ‘whatever’,
21.	Run python server
a.	$ cd gotthegist   #makesure if you ls you can see the file manage.py
b.	$ python manage.py migrate
c.	$ python manage.py runserver 
22.	Create Python App
a.	$ python manage.py startapp nameofapp  #make sure you are in the same directory as manage.py
23.	Install Git
a.	$ sudo apt-get install git
b.	Note: add env directory to .gitignore file (maybe…)
c.	In PyCharm go to the VCS menu and choose git as version control system
d.	Tell Git who you are:
i.	$ git config --global user.name "Gengscode" 
ii.	$ git config --global user.email gengwang04@gmail.com
e.	Create repository on Github (https://help.github.com/articles/create-a-repo/)  

f.	Add files
g.	    git add *
h.	Commit
i.	    git commit -m "Commit message"
j.	    # commit any files you have added with git add and any files changed since then     
k.	    git commit -a 
l.	Push
m.	    git push origin master
n.	Status
o.	    git status
p.	Pull
q.	    git pull
Other commands:
Everytime we change models.py (which defines our database) we need to run:
•	$ python manage.py syncdb 
Youtube using django to create a simple app: https://www.youtube.com/watch?v=bRnm8f6Wavk 
