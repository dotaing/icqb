#-*- coding:UTF-8 -*-
from django.db import models

# Create your models here.
class HostGroup(models.Model):
    """服务器分组"""
    Name = models.CharField(max_length=50,verbose_name="分组名称")
    AnHost = models.CharField(max_length=30,verbose_name="ID范围")
    def __unicode__(self):
        return self.name

class ServerList(models.Model):
    """线上服务器列表"""
    Name = models.CharField(max_length=50,verbose_name="主机名称")
    ServerId = models.CharField(max_length=20,verbose_name="游戏服ID")
    Flag = models.CharField(max_length=2,verbose_name="批量执行开关")
    Ip = models.CharField(max_length=20,verbose_name="主机地址")
    InGroup =models.ForeignKey(HostGroup)
    Type = models.CharField(max_length=20,verbose_name="类型")
    Status = models.IntegerField(max_length=2,verbose_name="服务器状态1:正常,2:合服中,3:架服中,4:闲置")
    WorkNow =  models.CharField(max_length=30,verbose_name="当前在做什么")
    def __unicode__(self):
        return self.Name