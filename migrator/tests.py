import unittest
from django.test import Client
from django.test import TestCase
from migrator.models import IMAPEndpoint

# Create your tests here.

class IMAPEndpointTests(TestCase):

    def setUp(self):
        IMAPEndpoint.objects.create(email_imap="test1@example.com", host_imap="143")
        IMAPEndpoint.objects.create(email_imap="test2@example.com", host_imap="993")

    def test_imapendpoint_can_connect(self):
        """Animals that can speak are correctly identified"""
        imap1 = IMAPEndpoint.objects.get(email_imap="test1@example.com")
        imap2 = IMAPEndpoint.objects.get(email_imap="test2@example.com")
        self.assertEqual(imap1.__str__(), 'imap1 has "port 143"')
        self.assertEqual(imap2.__str__(), 'imap2 has "port 993"')


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_index(self):
        client = Client()
        response = client.get('/migrator/index/')
        self.assertEqual(response.status_code, 200)