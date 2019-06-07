from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.
# 包含了应用程序的数据模型


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'),)

    title = models.CharField(max_length=250)    # 帖子标题  字段定义为CharField 在sql数据库中将转换为varchar
    slug = models.SlugField(max_length=250, unique_for_date='publish')   # 作为一种简短的标记
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')   # 作者 表示为一个外键，并定义了一对多关系。
                                                                                            # on_delete=models.CASCADE,
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)    # 帖子发布时间。
    created = models.DateTimeField(auto_now_add=True)   # 帖子创建的时间   由于使用了auto_now_add 保存时会自动保存日期
    updated = models.DateTimeField(auto_now=True)   # 帖子更新的时间
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft') # 显示了帖子的状态

    objects = models.Manager() # The default manager.默认的管理器
    published = PublishedManager() # Our custom manager.我们创建的管理器 查询发布的帖子

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title



