def validar_email(email):
    if email.endswith('@gmail.com') and not email.startswith('@'):
        return True
    else:
        return False
