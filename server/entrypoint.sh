#!/bin/bash
set -e
envsubst < $NGINX_TEMPLATE > /etc/nginx/conf.d/default.conf
exec "$@"