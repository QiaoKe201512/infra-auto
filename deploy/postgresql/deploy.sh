docker run -d \
	--name infra-postgres \
	-p 5432:5432 \
	-e POSTGRES_PASSWORD=TX1hRq75fM3FTPYViNCh \
	-e PGDATA=/var/lib/postgresql/data/pgdata \
	-v /data/pg_data:/var/lib/postgresql/data \
	postgres