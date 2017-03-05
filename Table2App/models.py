from __future__ import unicode_literals

from django.db import models

class architectures(models.Model):
    field1 = models.TextField()
    field2 = models.TextField()
    field3 = models.TextField()
    field4 = models.TextField()
    field5 = models.TextField()
    field6 = models.TextField()
    field7 = models.TextField()
    field8 = models.TextField()
    field9 = models.TextField()
    
    def __str__(self):
        return self.field1
