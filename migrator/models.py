from django.db import models
import imaplib, socket
from django.utils import timezone


class IMAPEndpoint(models.Model):
    """ An imap account definition
    """
    email_imap= models.EmailField(verbose_name='email')
    password_imap = models.CharField(max_length=200, verbose_name='password')
    host_imap = models.CharField(max_length=100, verbose_name='host')
    port_imap = models.IntegerField(default=143, verbose_name='port')
    NONE = 'NO'
    SSL_TLS = 'SSL'
    START_TLS = 'START'
    SSL_CHOICES = (
        (SSL_TLS, 'SSL/TLS'),
        (START_TLS, 'STARTTLS'),
    )
    encryption_imap = models.CharField(max_length=8, choices=SSL_CHOICES, default=START_TLS, verbose_name='encryption')
    path = models.CharField(max_length=200, verbose_name='path')

    def __str__(self):
        #return "host : %s" % self.host
        return "{} on {}".format(self.email_imap, self.host_imap)

    def connection(self):
        try:
            if self.encryption_imap == 'SSL/TLS':
                imap = imaplib.IMAP4_SSL(self.host_imap)
            else:
                imap = imaplib.IMAP4(self.host_imap)
                imap.starttls()
        except socket.gaierror:
            return False
        # Login to IMAP server account using encryption
        try:
            imap.login(self.email_imap,self.password_imap)
            return imap
        except imap.error:
            return False


class Migration(models.Model):
    origin = models.OneToOneField(IMAPEndpoint, related_name='target_migration')
    target = models.OneToOneField(IMAPEndpoint, related_name='origin_migration')
    creation_date = models.DateTimeField('Created Date', auto_now_add=True)
    processing_date = models.DateTimeField('Start Date', null=True)
    completion_date = models.DateTimeField('End Date', null=True)

    def __str__(self):
        #return "Source : %s" % self.source
        return "{}".format(self.origin)