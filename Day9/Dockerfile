FROM ubuntu
RUN apt update
RUN apt install -y python3
EXPOSE 8000
VOLUME /content
WORKDIR /content
CMD python3 -m http.server
