from django.db import InterfaceError, models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from slugify import slugify


class ArticleColumn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='article_column')
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    
    def _str_(self):
        return self.column    


class ArticleTag(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="tag")
    tag = models.CharField(max_length=500)

    def __str__(self):
        return self.tag

class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name="article")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn, on_delete=models.CASCADE,related_name="article_column")
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now())   
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("title",)
        ordering = ("-updated",)
        index_together = (('id', 'slug'),)   

    def __str__(self):
        return self.title

    def save(self, *args, **kargs):   
        self.slug = slugify(self.title)   
        super(ArticlePost, self).save(*args, **kargs)

    def get_absolute_url(self):   
        return reverse("article:article_detail", args=[self.id, self.slug])

    def get_url_path(self):
        #return "/article/read-article/{0}/{1}".format(self.id, self.slug)
        return reverse("article:list_article_detail", args=[self.id, self.slug])


class Comment(models.Model):
    article = models.ForeignKey(ArticlePost, on_delete=models.CASCADE,related_name="comments") 
    commentator = models.CharField(max_length=90)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',) 

    def __str__(self):
        return "Comment by {0} on {1}".format(self.commentator.username, self.article)