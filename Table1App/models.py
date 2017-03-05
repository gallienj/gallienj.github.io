from __future__ import unicode_literals

from django.db import models

class fasta(models.Model):
    gi = models.TextField()
    sequence = models.TextField()
    
    def __str__(self):
        return self.gi
