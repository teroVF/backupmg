#app para a criação de backups de bases de dados MongoDB
import subprocess
from os import getenv
from sys import exit, argv

# os.environ['DATABASE_USERNAME'] = 'antero'
# os.environ['DATABASE_PASSWORD'] = '123'
# os.environ['DATABASE_CONNECT_STRING'] = 'localhost:27017'
# os.environ['BD_DATABASE_NAME'] = 'myFirstDataBase'
# os.environ['BACKUP_DIR'] = ' '

def error_message():
    if (len(argv) > 1):
        print('comando inválido, utiliza: "./backupmg"')
        exit(1)
    
    if not all(getenv(var) for var in ['DATABASE_USERNAME', 'DATABASE_PASSWORD', 'DATABASE_CONNECT_STRING', 'BD_DATABASE_NAME']):
        print('Variáveis de ambiente não configuradas, utiliza: export DATABASE_USERNAME=<username>, export DATABASE_PASSWORD=<password>, export DATABASE_CONNECT_STRING=<url>, export BD_DATABASE_NAME=<database>')
        exit(1)


def make_backup(db_name):
    backup = "dump" if not getenv('BACKUP_DIR') or getenv('BACKUP_DIR').strip() == "" else getenv('BACKUP_DIR')

    command = [
        'mongodump',
        '--host', getenv('DATABASE_CONNECT_STRING'),
        '--db', db_name,
        '--username', getenv('DATABASE_USERNAME'),
        '--password', getenv('DATABASE_PASSWORD'),
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
        make_backup(getenv('BD_DATABASE_NAME'))

    except Exception as e:
        print('Falha ao conectar ao MongoDB:', e)