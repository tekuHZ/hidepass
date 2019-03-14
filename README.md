# Hidepass
Este script sirve para mostrar asteriscos al momento de ingresar una contaseñas por consola.

## Instalacion
Para las distribuciones de debian y derivados instalar:
- apt-get install python3-setuptools
- apt-get install python3-pip 
```sh
$ cd hidepass/
$ python3 setup.py sdist
$ cd dist/
$ pip3 install hidepass-1.0.0.tar.gz
```
## Forma de uso
```python 
import hidepass
password = hidepass.hidepass("Ingrese su contraseña: ")
print(password)
```
##### Compatible con:
- Windows
- GNU/Linux
- MacOS(Aún no se a probado).
