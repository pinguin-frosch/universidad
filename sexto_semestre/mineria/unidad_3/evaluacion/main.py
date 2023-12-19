import json

def main():
    configuracion = open('configuracion.json')
    datos = json.load(configuracion)
    print(datos)

if __name__ == '__main__':
    main()
