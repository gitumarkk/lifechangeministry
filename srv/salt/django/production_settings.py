DATABASES = {
    'default': {
                'ENGINE': '{{ pillar["dbengine"] }}',
                'NAME': '{{ pillar["dbname"] }}',
                'USER': '{{ pillar["dbuser"] }}',
                'PASSWORD': '{{ pillar["dbpassword"] }}',
                'HOST': '{{ pillar["dbhost"] }}',
                'PORT': '{{ pillar["dbport"] }}',
            }
}

MANDRILL_KEY = '{{ pillar["dbport"] }}'
