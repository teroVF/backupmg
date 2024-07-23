#!/bin/bash

#instalar pyinstaller se necessário
if [ ! -f /home/${whoami}/.local/bin/pyinstaller ]; then
    echo "Instalando pyinstaller"
    pip install pyinstaller
fi
#criar binario
/home/${whoami}/.local/bin/pyinstaller --onefile --clean --name backupmg backupmg.py

echo "Criou um binario na pasta dist"