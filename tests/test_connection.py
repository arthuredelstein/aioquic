import io
from unittest import TestCase

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from aioquic.connection import QuicConnection

from .utils import load

SERVER_CERTIFICATE = x509.load_pem_x509_certificate(
    load('ssl_cert.pem'), backend=default_backend())
SERVER_PRIVATE_KEY = serialization.load_pem_private_key(
    load('ssl_key.pem'), password=None, backend=default_backend())


class QuicConnectionTest(TestCase):
    def test_connect(self):
        client = QuicConnection(
            is_client=True)
        server = QuicConnection(
            is_client=False,
            certificate=SERVER_CERTIFICATE,
            private_key=SERVER_PRIVATE_KEY)

        # perform handshake
        client.connection_made()
        for datagram in client.pending_datagrams():
            server.datagram_received(datagram)

        for datagram in server.pending_datagrams():
            client.datagram_received(datagram)

        for datagram in client.pending_datagrams():
            server.datagram_received(datagram)

        for datagram in server.pending_datagrams():
            client.datagram_received(datagram)

    def test_connect_with_log(self):
        client_log_file = io.StringIO()
        client = QuicConnection(
            is_client=True,
            secrets_log_file=client_log_file)
        server_log_file = io.StringIO()
        server = QuicConnection(
            is_client=False,
            certificate=SERVER_CERTIFICATE,
            private_key=SERVER_PRIVATE_KEY,
            secrets_log_file=server_log_file)

        # perform handshake
        client.connection_made()
        for datagram in client.pending_datagrams():
            server.datagram_received(datagram)

        for datagram in server.pending_datagrams():
            client.datagram_received(datagram)

        for datagram in client.pending_datagrams():
            server.datagram_received(datagram)

        for datagram in server.pending_datagrams():
            client.datagram_received(datagram)

        # check secrets were logged
        client_log = client_log_file.getvalue()
        server_log = server_log_file.getvalue()
        self.assertEqual(client_log, server_log)
        labels = []
        for line in client_log.splitlines():
            labels.append(line.split()[0])
        self.assertEqual(labels, [
            'QUIC_SERVER_HANDSHAKE_TRAFFIC_SECRET',
            'QUIC_CLIENT_HANDSHAKE_TRAFFIC_SECRET',
            'QUIC_SERVER_TRAFFIC_SECRET_0',
            'QUIC_CLIENT_TRAFFIC_SECRET_0'])
