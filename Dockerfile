FROM python:2

RUN apt-get -y install gcc git \
    && pip install google-cloud-logging \
    && pip install git+https://github.com/shikajiro/xmppgcm

COPY xmpp.py /

#CMD ["export" "GOOGLE_CLOUD_DISABLE_GRPC=true"]
CMD ["python", "/xmpp.py"]

# docker build -t shikajiro/xmpp_gcm .