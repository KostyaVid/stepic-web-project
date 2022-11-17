sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
cd web
sudo -c gunicorn --bind='0.0.0.0:8080' hello:app
sudo -c gunicorn --bind='0.0.0.0:8000' ask.wsgi:application
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start