
import subprocess

def check():
    print ("Comprobando sintaxis ... \n")

    salida = subprocess.run(['pylint', '-E','mercadoclubespro'])
    if salida.returncode == 0:
        print("No hay errores")
    else: 
        print("Se han encontrado errores")
    
    return salida
