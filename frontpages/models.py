from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'Contact Us'
        verbose_name_plural = u'Contact Us'
    def __unicode__(self):
        return self.email
