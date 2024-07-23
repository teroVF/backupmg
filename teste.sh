#!/bin/bash

# os.environ['DATABASE_USERNAME'] = 'antero'
# os.environ['DATABASE_PASSWORD'] = '123'
# os.environ['DATABASE_CONNECT_STRING'] = '172.27.255.66:27017'
# os.environ['BD_DATABASE_NAME'] = 'myFirstDataBase'
# os.environ['BACKUP_DIR'] = ' '

# Variáveis ambiente
export DATABASE_USERNAME='antero'
export DATABASE_PASSWORD='123'
export DATABASE_CONNECT_STRING='localhost:27017'
export BD_DATABASE_NAME='myFirstDataBase'
export BACKUP_DIR=''

./backupmg

if [ $? -eq 0 ]; then
    echo "teste passou"
else
    echo "teste falhou"
fi