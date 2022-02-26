from cryptography.fernet import Fernet
def main():
    texto = str(input("Introduce la contraseña a cifrar: "))
    

    key = Fernet.generate_key()
    objeto_cifrado = Fernet(key)
    texto_encriptado = objeto_cifrado.encrypt(str.encode(texto))
    print(texto_encriptado)

   
   
    texto_desencriptado = objeto_cifrado.decrypt(texto_encriptado)
    print(texto_desencriptado)

if __name__ == '__main__':
    main()