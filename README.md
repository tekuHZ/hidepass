# Hidepass
Este script sirve para mostrar asteriscos al momento de ingresar una contaseñas por consola.

## Instalacion
```sh
$ cd hidepass/
$ python3 setup.py sdist
$ cd dist/
$ pip install hidepass-1.0.0.tar.gz
```
## Forma de uso
```python 
import hidepass
password = hidepass.hidepass("Ingrese su contraseña: ")
print(password)
```