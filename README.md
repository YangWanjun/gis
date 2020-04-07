# server
docker run -d --name gis --link postgres:postgres -p 8004:80 -v /workspace/gis/:/gis yangwanjun/gis python /gis/manage.py runserver 0.0.0.0:80