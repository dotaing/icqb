#-*- coding:UTF-8 -*-

from django.http import HttpResponse,HttpResponseRedirect

from userpro.models import AccountUser,UserGroup,UserSessionCache,ViePerUrl

def SelectPerViews(request):
    try:
        Vid=ViePerUrl.objects.get(url=request.path).id
        print Vid
        return Vid
    except Exception,e:
        print e

def GetUserPer(request):
    try:
        Pro=[int(i) for i in AccountUser.objects.get(username=request.session['usernames']).in_group.permission.split(",")]
        print Pro
        return Pro
    except Exception,e:
        print e

class Permission(object):
    def process_request(self,request):
        try:
            #print request.session['usernames']
            #print request.META['HTTP_USER_AGENT']
            #print request.META['REMOTE_ADDR']
            if request.path not in ['/','/LoginIn/'] and request.path.split('/')[1] != "lib":
                username = request.session.get('usernames','anybody')
                if username == "anybody":
                    return HttpResponse("请登录")
                if SelectPerViews(request) not in GetUserPer(request):
                    return HttpResponse("无权访问")
                    print "无权访问"
        except Exception,e:
            print e
            return HttpResponse("未知错误")