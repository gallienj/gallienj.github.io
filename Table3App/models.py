from __future__ import unicode_literals

from django.db import models

class toxin(models.Model):
    field1 = models.TextField()
    field2 = models.TextField()
    field3 = models.TextField()
    field4 = models.TextField()
    
    def __str__(self):
        return self.field1
