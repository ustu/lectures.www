#!/bin/bash

nginx && while inotifywait -e modify /etc/nginx/includes /etc/nginx/sites-enabled; do
    pkill nginx
    nginx
    echo "File in Config Folder Changed, Restarted"
done
