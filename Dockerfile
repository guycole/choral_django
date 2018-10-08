#
FROM ubuntu:16.04
#
EXPOSE 80
#
RUN apt-get update && apt-get install -y python3 && apt-get install -y python3-pip
#
needs virtualenv
#
