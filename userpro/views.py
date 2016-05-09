#-*- coding:UTF-8 -*-
__author__ = 'maomao'
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import hashlib,json
from userpro.models import AccountUser,UserGroup,UserSessionCache,ViePerUrl
from Lib.Toole import getTimeInt
from Lib.MenuIi import InitializeMenu,InitializePro
from django.contrib.sessions.models import Session

def LoginIndex(request):
    """登录页面"""
    TempMd5= hashlib.md5(getTimeInt()).hexdigest()
    request.session['MD5']=TempMd5
    return render_to_response("login.html",{'M':TempMd5})

def LoginIn(request):
    """登录验证"""
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password']:
            username=request.POST['username']
            userpass=request.POST['password']
            try:
                userObj=AccountUser.objects.get(username=username)
                Nps=hashlib.md5(request.session['MD5'] + userObj.username + userObj.userpasswd).hexdigest()
                if Nps == userpass:
                    #防止重复登录机制
                    unlogin_key= UserSessionCache.objects.filter(username=userObj.username)
                    if unlogin_key:
                        for i in unlogin_key:
                            Session.objects.filter(session_key=i.session_key).delete()
                        UserSessionCache.objects.filter(username=userObj.username).delete()
                    UserSessionCache.objects.create(session_key=request.session._get_session_key(),username=userObj.username)
                    request.session['usernames'] = userObj.username
                    return HttpResponseRedirect('/Home/')
            except Exception,e:
                print e
                return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')


def LoginOut(request):
    """退出登录"""
    try:
        del request.session['usernames']
        #重复登录机制
        #UserSessionCache.objects.filter(username=request.session['usernames']).delete()
    except Exception,e:
        print e
    return HttpResponse('<script>alert("已退出系统");window.location.href="/"</script>')



def ShowUserList(request):
    """显示用户列表"""
    MenuList=InitializeMenu(request)
    UserGroupAll=UserGroup.objects.all()
    UserListAll=AccountUser.objects.all()
    return render_to_response("userlist.html",{"MenuList":MenuList,"UserListAll":UserListAll,"UserGroupAll":UserGroupAll,"username":request.session['usernames']})

def AddUser(request):
    """添加用户"""
    if request.method == 'POST':
        if request.POST['username'] and request.POST['password'] and request.POST['groupid']:
            try:
                username=request.POST['username']
                userpass=request.POST['password']
                groupid=request.POST['groupid']
                if len(username) < 20 and len(userpass) < 50:
                    if username.isalnum():
                        #userpass=hashlib.md5(userpass).hexdigest()
                        AccountUser.objects.create(username=username,userpasswd=userpass,is_lock=1,in_group_id=int(groupid),is_superman=0,lastlogin_host="0.0.0.0",)
                        return HttpResponseRedirect('/ShowUserList/')
                    return HttpResponse("用户名只能是字符串")
                return HttpResponse("账号或密码超出长度")
            except Exception,e:
                 return HttpResponse(e)
    return HttpResponse("0x00001")


def DelUser(request):
    """删除用户"""
    if request.method == 'POST':
        if request.POST['uid']:
            try:
                NumList = request.POST['uid'].split(",")
                NumList = [int(i) for i in NumList]
                AccountUser.objects.filter(id__in=NumList).delete()
                return HttpResponseRedirect('/ShowUserList/')
            except Exception,e:
                return HttpResponse("0x00003")
            return HttpResponse("0x00001")
    return HttpResponse("0x00002")


def EditUser(request):
    """修改用户"""
    if request.method == 'POST':
        if request.POST['edit_username'] and request.POST['edit_uid'] and request.POST['edit_stopuser'] and request.POST['edit_groupid']:
            username=request.POST['edit_username']
            edit_uid=int(request.POST['edit_uid'])
            is_lock=int(request.POST['edit_stopuser'])
            in_group=int(request.POST['edit_groupid'])
            try:
                if request.POST['edit_password']:
                    password=request.POST['edit_password']
                    AccountUser.objects.filter(id=edit_uid,username=username).update(userpasswd=password,is_lock=is_lock,in_group=in_group)
                else:
                    AccountUser.objects.filter(id=edit_uid,username=username).update(is_lock=is_lock,in_group=in_group)
                return HttpResponseRedirect('/ShowUserList/')
            except Exception,e:
                print e
                return HttpResponse("0x00001")
    return HttpResponse("err")


def EditUserJson(request):
    """返回要修改用户json"""
    if request.method == 'POST':
        if request.POST['uid']:
            try:
                UserGroupAll=UserGroup.objects.all()
                GroupList=""

                uid=int(request.POST['uid'])
                UserOB=AccountUser.objects.get(id=uid)
                if UserOB.is_lock:
                    UserSTOP="""<option value="1" selected>正常</option>
                    <option  value="0">停用</option>
                    """
                else:
                    UserSTOP="""<option value="1">正常</option>
                    <option selected value="0" selected>停用</option>
                    """
                for ig in UserGroupAll:
                    if UserOB.in_group_id == ig.id:
                        GroupList+='<option selected value="%s">%s</option>'%(ig.id,ig.name)
                    else:
                        GroupList+='<option value="%s">%s</option>'%(ig.id,ig.name)
                html="""

                	<form id="edit_form" class="form-horizontal" method="post" action="/EditUser/">
        <div class="control-group">
            <label class="control-label" style="color:	#4F4F4F;">用户名</label>
            <div class="controls">
                <input type="text" name="edit_username" id="edit_name" value="%s" readonly >
            </div>
        </div>
         <div class="control-group">
            <label class="control-label" style="color:	#4F4F4F;">设置密码</label>
            <div class="controls">
                <input type="text" name="edit_password" id="edit_password" >
                <input type="hidden" id="edit_uid" name="edit_uid" value="%s">
            </div>
        </div>

            <div class="control-group">
			<label class="control-label" style="color:	#4F4F4F;">所属角色</label>
			<div class="controls">
				<select  name="edit_groupid">
                %s
				</select>
			</div>
			<div class="control-group">
			<label class="control-label" style="color:#FF2D2D;">停用账户</label>
			<div class="controls">
				<select  name="edit_stopuser">
				%s
				</select>
					</form>
			</div>
		</div>


      </div>

	</div>

			<div class="modal-footer">

	<input type="submit"  class="btn btn-primary"  id="edit_fa_button" value="提交修改">
		</div>
   <script>
    $("#edit_fa_button").click(function(){
    if($("#edit_password").val()!=""){
    if($("#edit_password").val().length < 6){
        alert("密码长度不能小于6位");
        return;
    }else{
        $("#edit_password").attr("value",$.md5($("#edit_password").val()));
        $("#edit_form").submit();
    }
    }
 $("#edit_form").submit();
    });
</script>
                """ % (UserOB.username.encode("utf-8"),UserOB.id,GroupList.encode("utf-8"),UserSTOP)
                return HttpResponse(json.dumps(html,ensure_ascii=False))
            except Exception,e:
                return HttpResponse("err")




def EditGroupJson(request):
    """返回要修改组json"""
    if request.method == 'POST':
        if request.POST['gid']:
            try:
                html=InitializePro(int(request.POST['gid']))
                return HttpResponse(json.dumps(html,ensure_ascii=False))
            except Exception,e:
                return HttpResponse("err")

def ShowGroupList(request):
    """显示用户页面"""
    UserGroupAll=UserGroup.objects.all()
    MenuList=InitializeMenu(request)
    return render_to_response("grouplist.html",{"UserGroupAll":UserGroupAll,"MenuList":MenuList,"username":request.session['usernames']})

def EditGroupPro(request):
    """权限修改后提交"""
    UserGroupAll=UserGroup.objects.all()
    MenuList=InitializeMenu(request)
    if request.method == 'POST':
        if request.POST['omg'] and request.POST['gid'] :
            try:
                omg=request.POST['omg']
                gidomg=[ int(i) for i in omg.split(",")]
                gid=int(request.POST['gid'])
                #permission,表格里必须有个默认0的权限
                UserGroup.objects.filter(id=gid).update(permission=omg)
            except Exception,e:
                print e
    return render_to_response("grouplist.html",{"UserGroupAll":UserGroupAll,"MenuList":MenuList,"username":request.session['usernames']})