from django.db import models

# Create your models here.



class Tag(models.Model):
    name=models.CharField(max_length=128)

class Post(models.Model):
    title=models.CharField(max_length=128)
    tags = models.ManyToManyField(
        Tag,
        through='PostsTags'
    )
    #tag = models.ManyToManyField(Tag,through='PostTag',related_name='posts',blank=True)
    class Meta:
        db_table = 'post'
        managed = False

    def set_tags(self,*tags):
        self.tags.clear()
        PostsTags.objects.bulk_create([PostsTags(post=self,tag=tag) for tag in tags])


class PostsTags(models.Model):
    post=models.ForeignKey(Post,db_index=True,on_delete=models.CASCADE)
    tag =models.ForeignKey(Tag,db_index=True,on_delete=models.CASCADE)
    #created_time= models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts_tags'
        managed = False
