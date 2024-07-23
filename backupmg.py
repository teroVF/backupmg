#app para a criação de backups de bases de dados MongoDB
import os
import subprocess
import sys

# os.environ['DATABASE_USERNAME'] = 'antero'
# os.environ['DATABASE_PASSWORD'] = '123'
# os.environ['DATABASE_CONNECT_STRING'] = 'localhost:27017'
# os.environ['BD_DATABASE_NAME'] = 'myFirstDataBase'
# os.environ['BACKUP_DIR'] = ' '

def error_message():
    if (len(sys.argv) > 1):
        print('comando inválido, utiliza: "./backupmg"')
        sys.exit(1)
    if os.getenv('DATABASE_USERNAME') is None or os.getenv('DATABASE_PASSWORD') is None or os.getenv('DATABASE_CONNECT_STRING') is None or os.getenv('BD_DATABASE_NAME') is None:
        print('Variáveis de ambiente não configuradas, utiliza: export DATABASE_USERNAME=<username>, export DATABASE_PASSWORD=<password>, export DATABASE_CONNECT_STRING=<url>, export BD_DATABASE_NAME=<database>')
        sys.exit(1)


def make_backup(db_name):
    backup = os.getenv('BACKUP_DIR') if os.getenv('BACKUP_DIR').strip() != "" \
        or os.getenv('BACKUP_DIR') is None  else "dump"
    command = [
        'mongodump',
        '--host', os.getenv('DATABASE_CONNECT_STRING'),
        '--db', db_name,
        '--username', os.getenv('DATABASE_USERNAME'),
        '--password', os.getenv('DATABASE_PASSWORD'),
        '--out', backup
    ]
    try:
        subprocess.run(command, check=True)
        print('Backup realizado com sucesso, verifique a pasta: ' + backup)
    except subprocess.CalledProcessError as e:
        print('Falha ao realizar o backup:', e)
    except KeyboardInterrupt:
        print('Backup cancelado pelo usuário')

if __name__ == "__main__":
    error_message()
    try:
        make_backup(os.getenv('BD_DATABASE_NAME'))
    except Exception as e:
        print('Falha ao conectar ao MongoDB:', e)