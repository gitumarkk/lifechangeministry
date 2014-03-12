include:
    - requirements
    - postgresql
    - supervisor
    - nginx

/srv/lifechangeministry/venv:
    virtualenv.managed:
        - system_site_packages: False
        - runas: {{ pillar["user"]}}  # Who to run it as
        - requirements: salt://django/requirements.txt
        - require:
            - pkg: python-dev
            - pkg: python-pip
            - pkg: python-virtualenv
            - pkg: libpq-dev


django.supervisor.conf:
    file.managed:
        - name: /etc/supervisor/conf.d/django.conf
        - source: salt://supervisor/django.conf
        - require:
            - pkg: supervisor


djangouser: # Name of the package or service
    postgres_user.present:
        - name: {{ pillar["dbuser"]}}
        - password: {{ pillar["dbpassword"]}}
        - runas: postgres
        - require:
            - service: postgresql


djangodb:
    postgres_database.present:
        - name: {{ pillar["dbname"]}}
        - encoding: UTF8
        - lc_ctype: en_US.UTF8
        - lc_collate: en_US.UTF8
        - template: template0
        - owner: {{ pillar["dbuser"]}}
        - runas: postgres
        - require:
            - postgres_user: djangouser


production_settings.py:
    file.managed:
        - name: /srv/lifechangeministry/lcm/production_settings.py
        - source: salt://django/production_settings.py
        - template: jinja  # What in the world is the template? I think it tells salt how to fill in the variables
        - require:
            - postgres_user: djangouser
