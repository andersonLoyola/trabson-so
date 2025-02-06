FROM debian

# Set environment variables for user and group IDs
ARG USER_UID=1000
ARG USER_GID=1000
ARG USERNAME=postgres_user

# Create a non-root user and group with specific UID and GID
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME


# Add PostgreSQL APT repository
RUN apt-get update && \
    apt-get install -y wget gnupg2 lsb-release && \
    wget -qO - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - && \
    echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list


# Add PostgreSQL APT repository
RUN apt-get install -y curl ca-certificates
RUN install -d /usr/share/postgresql-common/pgdg
RUN curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc
RUN sh -c 'echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN apt update

RUN apt-get update && \
    apt-get install -y nano ssh \
    repmgr \
    postgresql &&  \
    rm -rf /var/lib/apt/lists/* 

COPY ./db-config.sh /usr/local/bin/db-config.sh
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
COPY ./init-repmgr.sh /usr/local/bin/init-repmgr.sh
COPY ./init-db.sh /usr/local/bin/init-db.sh
COPY ./master-replication-setup.sh /usr/local/bin/master-replication-setup.sh

RUN chmod +x /usr/local/bin/db-config.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/init-repmgr.sh
RUN chmod +x /usr/local/bin/init-db.sh
RUN chmod +x /usr/local/bin/master-replication-setup.sh

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
