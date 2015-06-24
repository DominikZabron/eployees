from django.db import models

class Pracownik(models.Model):
    fname_text = models.CharField(max_length=200)
    lname_text = models.CharField(max_length=200)

    def __str__(self):
        return self.lname_text
