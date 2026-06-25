usuarios_list = []

# validaciones


def validar_sexo(Sexo):
    if sexo in ["M", "F"]:
        return True
    else:
        print("error es valido F o M")
        return False


def validar_password(password):
    if len(password.strip()) < 8:
        return False

    tiene_numero = False
    for letra in password:
        if letra.isnumeric():
            tiene_numero = True

    tiene_letras = False
    for letra in password:
        if letra.isalpha():
            tiene_letras = True

    if " " in password:
        print("Error no puede tener espacios")
        return False

    return tiene_numero and tiene_letras


def imprimir_usuario(usuario):
    print(f""" 
        -------------------------------
        nombre usuario: {usuario["Nombre_usuario"]}
        sexo: {usuario["sexo"]}
        password: {usuario["password"]} """)
