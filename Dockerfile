FROM python:2

RUN apt-get -y install gcc git \
    && pip install google-cloud-logging \
    && pip install git+https://github.com/shikajiro/xmppgcm

COPY android_stackdriver_log.py /

#CMD ["export" "GOOGLE_CLOUD_DISABLE_GRPC=true"]
# CMD ["python", "xmpp.py"]
ENTRYPOINT ["python", "/android_stackdriver_log.py"]

# docker build -t shikajiro/xmpp_gcm .
