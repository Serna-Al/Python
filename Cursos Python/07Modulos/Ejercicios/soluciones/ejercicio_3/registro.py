import validaciones

def registrar_usuario(nombre, email):
    if validaciones.validar_email(email):
        print(f"El usuario {nombre} ha sido registrado con el correo {email}.")
    else:
        print("El correo electrónico no es válido.")

