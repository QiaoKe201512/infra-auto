# docker 部署
docker run -d --name minio-server \
    --env MINIO_ROOT_USER="qiaoke" \
    --env MINIO_ROOT_PASSWORD="iGGeRqRrddCdo5X3QQ0g" \
    --publish 9000:9000 \
    --publish 9001:9001 \
    --volume /data/minio:/bitnami/minio/data \
    bitnami/minio:latest


docker run --name minio \
    --publish 9000:9000 \
    --publish 9001:9001 \
    --volume /path/to/minio-persistence:/bitnami/minio/data \
    bitnami/minio:latest
