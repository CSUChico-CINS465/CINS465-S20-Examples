from django.db import models

# Create your models here.
class Suggestion_Model(models.Model):
    suggestion = models.CharField(max_length=240)
    # author = models.CharField(max_length=240, default="bryan")

    def __str__(self):
        return self.suggestion 