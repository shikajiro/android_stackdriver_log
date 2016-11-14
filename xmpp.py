"""
This source is the process of transferring to see the Android of the log in StackDriver of GCP.
By working with https://hub.docker.com/r/shikajiro/xmpp_gcm/
Android -> GCM -> XMPP -> StackDriver
To achieve the flow.
"""
import logging
import json
import os

from xmppgcm import GCM, XMPPEvent
from google.cloud import logging as gcl

LOGGER_NAME = "AndroidLog"
logger = gcl.Client().logger(LOGGER_NAME)


def on_disconnect(draining):
    print 'inside on_disconnect'
    xmpp.connect(('fcm-xmpp.googleapis.com', 5235), use_ssl=True)


def on_session_start(queue_length):
    print 'inside on_session_start {0}'.format(queue_length)


def on_receipt(data):
    print 'inside on_receipt {0}'.format(data)


def on_message(data):
    print 'inside onMessage {0}'.format(data)
    msg = data.data
    print "msg {0}".format(msg)

    logger.log_text(json.dumps(msg))
#    logger.log_struct(msg) # TODO 0.20 bug


logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')
logging.debug("Starting up")

xmpp = GCM(os.environ["SENDER_ID"] + '@gcm.googleapis.com', os.environ["SERVER_KEY"])
xmpp.add_event_handler(XMPPEvent.CONNECTED, on_session_start)
xmpp.add_event_handler(XMPPEvent.DISCONNECTED, on_disconnect)
xmpp.add_event_handler(XMPPEvent.RECEIPT, on_receipt)
xmpp.add_event_handler(XMPPEvent.MESSAGE, on_message)

# xmpp.connect(('fcm-preprod.googleapis.com', 5236), use_ssl=True)  # test environment
xmpp.connect(('fcm-xmpp.googleapis.com', 5235), use_ssl=True)  #prod environment

while True:
    xmpp.process(block=True)

if __name__ == '__main__':
    pass
