FROM postgres

RUN apt-get update && \
    apt-get install -y nano ssh \
    repmgr &&\
    rm -rf /var/lib/apt/lists/* 
COPY ./init-db.sh /docker-entrypoint-initdb.d/
COPY ./master-replication-setup.sh /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/init-db.sh
RUN chmod +x /docker-entrypoint-initdb.d/master-replication-setup.sh
USER postgres
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["postgres"]