#Python Git Post Receive Hook
This a skeliton git post receive hook using [Python](http://www.python.org/), [Flask](http://flask.pocoo.org/) and deployed using [uWSGI](http://projects.unbit.it/uwsgi/) on [Nginx](http://wiki.nginx.org/).


###Setup
```sh
#Install needed software
sudo aptitude install build-essential python python-pip python-dev
sudo pip install Flask
sudo pip install http://projects.unbit.it/downloads/uwsgi-lts.tar.gz
sudo pip install supervisor
sudo pip install simplejson


#Setup Logging directories
sudo mkdir /var/log/uwsgi
sudo chmod 755 /var/log/uwsgi
```

###Configuration
We are using [`githook.ini`](githook.ini) to configure uWSGI's behaviour.

###Running the Application
To run the application, simply call uWSGI and give it the ini file:
```sh
sudo uwsgi --ini githook.ini
```

###Testing the Application
You can test the app locally by running
```sh
python githook.py
```

You can test `POST` commands using `curl`, e.g.
```sh
curl -X POST -H "Content-Type: application/json" -d '{"username":"xyz","password":"xyz"}' http://localhost:5000/deploy
```

###Nginx Configuration
```nginx
server {
        listen          80;
        server_name     usc.alghanmi.org;

        access_log      /home/www/logs/access.log;
        error_log       /home/www/logs/error.log warn;

        index           index.html index.htm;
        root            /home/www/public_html;

        location = /githook { rewrite ^ /githook/; }
        location /githook { try_files $uri @githook; }
        location @githook {
                 include uwsgi_params;
                 uwsgi_param SCRIPT_NAME /githook;
                 uwsgi_modifier1 30;
                 uwsgi_pass unix:/tmp/uwsgi-githook.sock;
        }
}
```

###References
The following references were used when developing this hook:
  + http://flask.pocoo.org/docs/tutorial/
  + http://uwsgi-docs.readthedocs.org/en/latest/WSGIquickstart.html
  + http://uwsgi-docs.readthedocs.org/en/latest/Configuration.html#magic-variables
  + http://flask.pocoo.org/docs/deploying/uwsgi/
  + http://flaviusim.com/blog/Deploying-Flask-with-nginx-uWSGI-and-Supervisor/
  + http://blog.eyallupu.com/2012/01/how-to-configure-nginx-and-uwsgi-to.html
