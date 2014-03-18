include:
    - requirements
    - postgresql

/srv/venv:
    virtualenv.managed:
        - system_site_packages: False
        - runas: {{ pillar["user"]}}  # Who to run it as
        - requirements: salt://django/requirements.txt
        - require:
            - pkg: python-dev
            - pkg: python-pip
            - pkg: python-virtualenv
            - pkg: libpq-dev

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
        - template: jinja  # WHat in the world is the template
        - require:
            - postgres_user: djangouser
