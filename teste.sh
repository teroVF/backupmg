#!/bin/bash

# Variáveis ambiente
export DATABASE_USERNAME='antero'
export DATABASE_PASSWORD='123'
export DATABASE_CONNECT_STRING='localhost:27017'
export BD_DATABASE_NAME='myFirstDataBase'
export BACKUP_DIR=''

./backupmg || echo "Erro ao executar o binário"