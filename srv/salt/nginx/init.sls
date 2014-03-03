nginx:  # Name of the package or service
    pkg: # Tells salt that this is a package
        - installed  # This tells salt to install this package
    service:  # Tells salt that this is also a service
        - running  # Tells salt to make ensure that the service is running
        - watch:  # Tells salt to watch the following items.
            - pkg: nginx  # If the package nginx gets updated, restart the service.
            - file: /etc/nginx/nginx.conf  # If the file nginx.conf gets updated, restart the service



/etc/nginx/nginx.conf  # Name of the file
    file:  # Tells salt that this is a file
        - managed  ## Tells salt to manage this file
        - source: salt://nginx/nginx.conf  # Tells salt where to find the local copy on the master
        - user: root  # Tells salt to ensure the owner of the file is root
        - group: root  # Tells salt to ensure the group of the file is root
        - mode: 644  # Tells salt to ensure the permission of the file is 644
