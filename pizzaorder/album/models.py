from django.db import models

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    # class Meta:
    #     unique_together = ('album', 'order')
    #     order_by = 'order'
    #
    # def __unicode__(self):
    #     return '{}{}'.format (self.order, self.title)