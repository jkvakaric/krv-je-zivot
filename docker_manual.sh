docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=<pwd> --name=postgres96 postgres:9.6

docker run -d -p 6379:6379 --name=redis30 redis:3.0

docker run -d -p 9000:9000 --name minio20180419 minio/minio:RELEASE.2018-04-19T22-54-58Z server /data

docker run -d -p 27017:27017 --name=mongo36 mongo:3.6-jessie

docker run -d -p 1025:1025 -p 8025:8025 --name=mailhog100 mailhog/mailhog:v1.0.0
