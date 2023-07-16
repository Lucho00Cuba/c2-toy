FROM python:alpine

ARG BUILD_DATE

LABEL maintainer="lomv0209@gmail.com" \
      owner="JustMe" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/Lucho00Cuba/c2-toy.git"

COPY src/ /opt/c2

RUN pip install -r /opt/c2/requirements.txt

WORKDIR /opt/c2/

CMD ["/usr/local/bin/python", "/opt/c2/ctx.py"]