postgresql:
    pkg:
        - name: postgresql-9.1
        - installed

    service.running:
        - enable: True
        - watch:
            - file: /etc/postgresql/9.1/main/pg_hba.conf

postgresql-server-dev-9.1:
    pkg:
        - installed
        - name: postgresql-server-dev-9.1

pg_hba.conf:
    file.managed:
        - name: /etc/postgresql/9.1/main/pg_hba.conf
        - source: salt://postgresql/pg_hba.conf
        - user: postgresql
        - group: postgres
        - mode: 644
        - require:
            - pkg: postgresql-9.1
