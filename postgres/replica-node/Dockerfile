FROM postgres
# Install necessary packages
RUN apt-get update && \
    apt-get install -y nano ssh postgresql-17-repmgr && \
    rm -rf /var/lib/apt/lists/*
COPY ./init-replica-server.sh /init-replica-server.sh
RUN chmod +x /init-replica-server.sh
USER postgres
ENTRYPOINT ["/init-replica-server.sh"]
CMD ["postgres"]