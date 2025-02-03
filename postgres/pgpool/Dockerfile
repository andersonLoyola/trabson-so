FROM debian:latest
RUN apt-get update

COPY ./pgpool.conf /usr/local/etc/pgpool.conf
COPY ./pgpool-setup.sh /usr/local/bin/pgpool-setup.sh
COPY ./replication-setup.sh /usr/local/bin/replication-setup.sh
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

RUN chmod +x /usr/local/bin/pgpool-setup.sh
RUN chmod +x /usr/local/bin/replication-setup.sh
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
    libpcp3

COPY ./pgpool2.tar.gz /tmp/pgpool2.tar.gz
RUN tar -xzf /tmp/pgpool2.tar.gz -C /tmp 
RUN groupadd -r pgpool && useradd -r -g pgpool pgpool
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
CMD ["pgpool", "-f", "/usr/local/etc/pgpool.conf", "-n"]