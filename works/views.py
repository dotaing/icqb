#-*- coding:UTF-8 -*-
__author__ = 'maomao'
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from works.models import HostGroup,ServerList as ServerListMod
import json,ast,os
from Lib.Toole import RANDOM_STR
from Lib.MenuIi import InitializeMenu

def Index(request):
    return render_to_response("login.html")

def Home(request):
    MenuList=InitializeMenu(request)
    return render_to_response("index.html",{"MenuList":MenuList,"username":request.session['usernames']})


def ServerList(request):
    """服务器列表"""
    MenuList=InitializeMenu(request)
    HostGroupAll=HostGroup.objects.all()
    if request.method == "GET":
        if "gid" in request.GET:
            try:
                gid=int(request.GET['gid'])
                ServerAll=ServerListMod.objects.filter(InGroup=gid)
                return render_to_response("serverlist.html",{"MenuList":MenuList,"HostGroupall":HostGroupAll,"ServerAll":ServerAll,"username":request.session['usernames']})
            except Exception,e:
                print e

    ServerAll=ServerListMod.objects.all()
    return render_to_response("serverlist.html",{"MenuList":MenuList,"HostGroupall":HostGroupAll,"ServerAll":ServerAll,"username":request.session['usernames']})