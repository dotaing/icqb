#-*- coding:UTF-8 -*-
from django.db import models


class UserGroup(models.Model):
    """用户权限分组"""
    name = models.CharField(unique=type,max_length=20,verbose_name="组名称")
    permission  = models.CharField(max_length=500,verbose_name="组所有权限")
    is_doc = models.CharField(max_length=200,verbose_name="注释")

    def __unicode__(self):
        return self.name


class AccountUser(models.Model):
    """用户表"""
    username  =models.CharField(unique=type,max_length=30,verbose_name="登陆名")
    userpasswd  = models.CharField(max_length=50,verbose_name="登陆密码")
    is_lock = models.BooleanField(default=False,verbose_name="是否锁定")
    in_group =models.ForeignKey(UserGroup)
    is_superman  = models.IntegerField(max_length=4,verbose_name="管理员")
    lastlogin_host = models.CharField(max_length=50,verbose_name="最后登录地址")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    lastlogin_time = models.DateTimeField(auto_now_add=True,verbose_name="最后登陆时间")


class UserSessionCache(models.Model):
    """用户表"""
    session_key  =models.CharField(unique=type,max_length=40,verbose_name="每个用户session_key")
    username  = models.CharField(unique=type,max_length=50,verbose_name="登录用户名")
    expire_date = models.DateTimeField(auto_now_add=True,verbose_name="登陆时间")

class ViePerUrl(models.Model):
    """试图,权限,Url"""
    title = models.CharField(max_length=50, verbose_name="权限名")
    url = models.CharField(max_length=50, verbose_name="访问URL")
    menu_type = models.IntegerField(max_length=1, verbose_name="菜单级别1:顶级菜单,2:二级菜单,3:应用方法")
    in_menu = models.IntegerField(max_length=50, verbose_name="id")