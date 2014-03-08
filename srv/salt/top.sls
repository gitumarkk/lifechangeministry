base:  # What environment this is for
    '*':  # Telling salt to apply to minions matching this
        - requirements  # Tells salt to apply this state to the matching minions
        - nginx  ## Tells salt to apply the nginx state to these hosts
        - git ##
        - postgresql
        - django
        - supervisor

