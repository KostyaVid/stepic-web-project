git clone https://github.com/KostyaVid/stepic-web-project.git /home/box/web
bash /home/box/web/init.sh

sudo pip3 install django==2.0

sudo /etc/init.d/mysql start
mysql -uroot -e "create database ask;"
mysql -uroot -e "grant all privileges on ask.* to 'box'@'localhost' with grant option;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate