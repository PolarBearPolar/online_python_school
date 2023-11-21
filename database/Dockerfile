FROM postgres:12-alpine

COPY db.pgsql /tmp/
COPY restore_db.sh /docker-entrypoint-initdb.d/

RUN apk update \
	&& apk add bash