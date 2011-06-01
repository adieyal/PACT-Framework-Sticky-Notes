from django.db import models

class Note(models.Model):
    text = models.CharField(max_length=255, null=False, blank=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    color = models.CharField(max_length=20, null=False)
    x = models.IntegerField(null=False)
    y = models.IntegerField(null=False)
    z = models.IntegerField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        l = 20
        return self.text[0:l] + ("..." if len(self.text) > l else "")
