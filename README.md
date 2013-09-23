#Python Git Post Receive Hook
This a skeliton git post receive hook using [Python](http://www.python.org/), [Flask](http://flask.pocoo.org/) and deployed using [uWSGI](http://projects.unbit.it/uwsgi/) on [Nginx](http://wiki.nginx.org/).


###Setup
```sh
#Install needed software
sudo aptitude install build-essential python python-pip python-dev supervisor
sudo pip install Flask
sudo pip install http://projects.unbit.it/downloads/uwsgi-lts.tar.gz
sudo pip install simplejson


#Setup Logging directories
sudo mkdir /var/log/uwsgi
sudo chmod 755 /var/log/uwsgi
```

##Configuration
###uWSGI
We are using [`githook.ini`](githook.ini) to configure uWSGI's behaviour.

###Nginx
This configuration is part of the `server` block. Current configuration is in
```
/etc/nginx/sites-enabled/usclug.deterlab.net.conf
```

```nginx
server {
        
        #
        # Actual server configuration
        #

        location = /git { rewrite ^ /git/; }
        location /git { try_files $uri @git; }
        location @git {
                include uwsgi_params;
                uwsgi_param SCRIPT_NAME /git;
                uwsgi_modifier1 30;
                uwsgi_pass unix:/tmp/uwsgi-githook.sock;
        }
}
```

###Supervisor Configuration
[Supervisor](http://supervisord.org/) is an application used to monitor and control your Flask app. Your webserver, for example, is setup to start after a machine crash or reboot. Supervisor will take care to restarting uWSGI and in turn your Flask app.

In debian-based systems, you install application configuration in the `/etc/supervisor/conf.d` directory. The configuration for our `githook` app would look like:

```
[program:githook]
command=/usr/local/bin/uwsgi --ini /opt/git_hook/githook.ini
directory=/opt/git_hook
numprocs=1
autostart=true
autorestart=true
stdout_logfile=/var/log/supervisor/githook-supervisord.log
redirect_stderr=true
stopsignal=INT
```


##Running
```
sudo service nginx restart
sudo service supervisor stop
sudo service supervisor start
```
