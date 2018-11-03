from django.db import models


class Video(models.Model):
    class Meta():
        db_table = 'VideoTable'

    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta():
        db_table = 'CommentTable'

    videoparent = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    objects = models.Manager()

    def __str__(self):
        return self.text
