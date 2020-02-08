from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

#学习主题信息
class Topic(models.Model):
    ''''用户学习主题'''
    text=models.CharField(max_length=200)#主题
    date_added=models.DateTimeField(auto_now=True)#添加的时间
    owner=models.ForeignKey(User)

    def __str__(self):
        '''返回模型的字符串表示(重写str方法）'''
        return self.text

#条目信息
class Entry(models.Model):
    '''学到有关某个主题的具体知识'''
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)#建立与Topic关联的外键并且设置级联删除
    text=models.TextField()#条目内容
    data_added=models.DateTimeField(auto_now=True)#添加条目的时间

    class Meta:
        verbose_name_plural='entries'

    def __str__(self):
        return  self.text[:50]+'...'