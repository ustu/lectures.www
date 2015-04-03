server {
         listen ${SRC_SERVER_PUB_IP}:80;
         servern_name ${FQDN} www.${FQDN}

          location / {
              proxy_pass         http://${SRC_SERVER_LOCAL_IP}:80/;
              proxy_redirect     off;

              proxy_set_header   Host             $host;
              proxy_set_header   X-Real-IP        $remote_addr;
              proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;
         }
}
