from django.db import models

class IMAPEndpoint(models.Model):
    """ An imap account definition
    """
    email = models.EmailField(verbose_name='email')
    password = models.CharField(max_length=200, verbose_name='password')
    host = models.CharField(max_length=100, verbose_name='host')
    port = models.IntegerField(default=143, verbose_name='port')
    NONE = 'NO'
    SSL_TLS = 'SSL'
    START_TLS = 'START'
    SSL_CHOICES = (
        (NONE, 'None'),
        (SSL_TLS, 'SSL/TLS'),
        (START_TLS, 'STARTTLS'),
    )
    encryption = models.CharField(max_length=8, choices=SSL_CHOICES, default=NONE, verbose_name='encryption')
    origin_file = models.CharField(max_length=200, verbose_name='originfile')

    def __str__(self):
        #return "host : %s" % self.host
        return "{} on {}".format(self.email, self.host)


class Migration(models.Model):
    origin = models.OneToOneField(IMAPEndpoint, related_name='target_migration')
    target = models.OneToOneField(IMAPEndpoint, related_name='origin_migration')
    creation_date = models.DateTimeField('Created Date')
    processing_date = models.DateTimeField('Start Date')
    completion_date = models.DateTimeField('End Date')

    def __str__(self):
        #return "Source : %s" % self.source
        return "{}".format(self.origin)