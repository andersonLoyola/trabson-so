FROM debian:latest

RUN apt-get update
COPY ./pgpool.conf /usr/local/etc/pgpool.conf
COPY ./pool_hba.conf /usr/local/etc/pool_hba.conf
COPY ./pgpool-setup.sh /usr/local/bin/pgpool-setup.sh
COPY ./replication-setup.sh /usr/local/bin/replication-setup.sh
COPY ./init_app_db.sh /usr/local/bin/init_app_db.sh
COPY ./failback-command.sh /usr/local/bin/failback-command.sh
COPY ./failover-command.sh /usr/local/bin/failover-command.sh
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/pgpool-setup.sh
RUN chmod +x /usr/local/bin/replication-setup.sh
RUN chmod +x /usr/local/bin/init_app_db.sh
RUN chmod +x /usr/local/bin/failover-command.sh
RUN chmod +x /usr/local/bin/failback-command.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

RUN apt-get update && \
    apt-get install -y \
    nano postgresql-client \
    netcat-traditional \
    curl \ 
    tar \ 
    build-essential \ 
    autoconf \ 
    automake \ 
    libtool \ 
    libpq-dev \
    postgresql-server-dev-all \
    libpcp3

COPY ./pgpool2.tar.gz /tmp/pgpool2.tar.gz
RUN tar -xzf /tmp/pgpool2.tar.gz -C /tmp 
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["pgpool", "-f", "/usr/local/etc/pgpool.conf", "-n"]