sudo apt update
sudo apt install python3.10 -y
sudo apt install python3.10-dev -y
sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.10 /usr/bin/python3
sudo python3 -m pip install gunicorn
sudo python3 -m pip install django==4.1
sudo python3 -m pip install mysqlclient

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE stepic_web;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"
# python3 manage.py makemigrations qa
# python3 manage.py migrate
# sudo /etc/init.d/gunicorn restart
# sudo gunicorn --bind='0.0.0.0:8000' ask.wsgi:application
#sudo -c gunicorn --bind='0.0.0.0:8080' hello:app
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test