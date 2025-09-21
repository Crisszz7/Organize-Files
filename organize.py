# Organizar los archivos sueltos de la carpeta documentos en carpetas segun su extension

import os
import shutil

documents_directory = r"C:\Users\Criss\OneDrive\Documentos" # Tu ruta de documentos
organize_directory = "Archivos Organizados" # Nombre de la carpeta donde se organizaran los archivos
path_directory = os.path.join(documents_directory, organize_directory)

if not os.path.exists(path_directory):
    os.makedirs(path_directory)

# Mover los archivos sueltos a la carpeta de organizados
for i in os.listdir(documents_directory):
    if "." in i:
        src_path = os.path.join(documents_directory, i) #ruta origen
        dst_path = os.path.join(path_directory, i) #ruta destino
        shutil.move(src_path, dst_path)

# Crear las carpetas segun la extension
for j in os.listdir(path_directory):
    extension = j.split(".")[-1]
    folder_path = os.path.join(path_directory, extension)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Mover los archivos a su respectiva carpeta
for k in os.listdir(path_directory):
    src_file_path = os.path.join(path_directory, k)
    
    if not os.path.isfile(src_file_path):
        continue
    
    file_extension = k.split(".")[-1]
    dst_file_path = os.path.join(path_directory, file_extension, k)
    shutil.move(src_file_path, dst_file_path)