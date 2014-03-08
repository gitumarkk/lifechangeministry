nginx:
  pkg:
    - name: nginx
    - installed
  service.running:
    - enable: True
    - watch:
        - file: /etc/nginx/nginx.conf

default-nginx:
  file.absent:
    - name: /etc/nginx/sites-enabled/default

nginx.conf:
  file.managed:
    - name: /etc/nginx/nginx.conf
    - source: salt://nginx/nginx.conf
    - user: {{ pillar["user"]}}
    # - group: www-data
    - mode: 644
    - require:
        - pkg: nginx


nginx-server-conf:
    file.managed:
        - name: /etc/nginx/conf.d/server.conf
        - source: salt://nginx/server.conf
        - require:
            - pkg: nginx


# nginx:  # Name of the package or service
#     pkg: # Tells salt that this is a package
#         - installed  # This tells salt to install this package
#     service:  # Tells salt that this is also a service
#         - running  # Tells salt to make ensure that the service is running
#         - watch:  # Tells salt to watch the following items.
#             - pkg: nginx  # If the package nginx gets updated, restart the service.
#             - file: nginxconf  # If the file nginx.conf gets updated, restart the service



# nginxconf:  # Name of the file
#     file.managed:  # Tells salt that this is a file ## Tells salt to manage this file
#         - name: /etc/nginx/sites-enabled/default
#         - source: salt://nginx/nginx.conf  # Tells salt where to find the local copy on the master
#         - template: jinja
#         - makedirs: True
#         - user: {{ pillar["user"]}}  # Tells salt to ensure the owner of the file is root
#         # - group: root  # Tells salt to ensure the group of the file is root
#         - mode: 644  # Tells salt to ensure the permission of the file is 644


# /etc/nginx/nginx.conf  # Name of the file
#     file:  # Tells salt that this is a file
#         - managed  ## Tells salt to manage this file
#         - source: salt://nginx/nginx.conf  # Tells salt where to find the local copy on the master
#         - user: root  # Tells salt to ensure the owner of the file is root
#         - group: root  # Tells salt to ensure the group of the file is root
#         - mode: 644  # Tells salt to ensure the permission of the file is 644

# nginx:
#   pkg:
#     - latest
#   service:
#     - running
#     - watch:
#       - file: nginxconf

# nginxconf:
#   file.managed:
#     - name: /etc/nginx/sites-enabled/default
#     - source: salt://webserver/nginx.conf
#     - template: jinja
#     - makedirs: True
#     - mode: 755
