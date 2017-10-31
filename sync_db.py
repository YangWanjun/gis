# coding: utf-8
import os
import sys
import getpass
import psycopg2
import django
from django.core.management import call_command

from addr import migrations as addr_migrations
from station import migrations as station_migrations


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gis.settings")
django.setup()

if sys.platform == 'win32' and getpass.getuser() == 'EB097':
    user = 'dev'
    password = 'root'
    host = '192.168.99.100'
else:
    user = 'dev'
    password = 'root'
    host = '127.0.0.1'


def main():
    # del_migration_records()
    del_migration_files()
    # migrate()


def migrate():
    call_command('migrate', '--fake')
    call_command('makemigrations', 'master')
    call_command('makemigrations', 'parkinglot')
    call_command('makemigrations', 'contract')
    call_command('migrate', '--fake')


def del_migration_records():
    con = psycopg2.connect(user=user, password=password, database='GIS', host=host)
    cursor = con.cursor()
    try:
        cnt = cursor.execute("delete from django_migrations")
        print 'EXEC: delete from django_migrations. %s rows deleted' % cnt
        con.commit()
    except Exception as e:
        con.rollback()
        raise e
    finally:
        cursor.close()
        con.close()


def del_migration_files():
    path_list = list()
    path_list.append(os.path.dirname(addr_migrations.__file__))
    path_list.append(os.path.dirname(station_migrations.__file__))

    for path in path_list:
        for filename in os.listdir(path):
            if filename not in ('__init__.py', '__init__.pyc'):
                file_path = os.path.join(path, filename)
                os.remove(file_path)
                print 'DEL: %s' % file_path


if __name__ == '__main__':
    main()
