import os
import sys

programa = "google-chrome"
print("Invocando processo")
parametros=["www.google.com"]

os.execvp(programa,(programa,)+tuple(parametros))

print("Saindo do invocador...")