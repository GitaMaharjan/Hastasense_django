from django.db import models


from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sign_images/category_images/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category_title

class Content(models.Model):
    content_id = models.AutoField(primary_key=True)
    content_title = models.CharField(max_length=100)
    content_image = models.ImageField(upload_to='sign_images/contents/content_sign_thumbnail/', default='default_image.png')
    content_sign_video = models.FileField(upload_to='sign_images/contents/content_sign_videos/', default='default_video.mp4')
    slug = models.SlugField(unique=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.IntegerField()


    def __str__(self):
        return self.content_title


class Word(models.Model):
    word_id = models.AutoField(primary_key=True)
    word_title = models.CharField(max_length=100)
    word_image = models.ImageField(upload_to='sign_images/words/word_image/', default='default_image.png')
    word_video_file = models.FileField(upload_to='sign_images/words/word_video/', default='default_video.mp4')
    # content = models.ForeignKey(Content, on_delete=models.CASCADE)
    content = models.IntegerField()


    def __str__(self):
        return self.word_title
    
    
class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title