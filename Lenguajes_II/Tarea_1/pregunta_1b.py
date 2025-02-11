import sys
from jsonp import *

def read_file(file_path):
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			return file.read()
	except FileNotFoundError:
		print(f"Error: El archivo '{file_path}' no se encontró.")
	except Exception as e:
		print(f"Error al leer el archivo: {e}")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Uso: python3 pregunta_1b.py <ruta_del_archivo>")
	else:
		try:
			print(jsonp.parse(read_file(sys.argv[1])))
		except Exception as e:
			print(f"Error: {e}")