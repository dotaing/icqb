#-*- coding:UTF-8 -*-
__author__ = 'maomao'
from userpro.models import AccountUser,UserGroup,UserSessionCache,ViePerUrl

def InitializeMenu(request):
    """初始化菜单"""
    MenuList=[]
    #ViePerUrlAll=ViePerUrl.objects.all()
    Pro=AccountUser.objects.get(username=request.session['usernames']).in_group.permission.split(",")
    ViePerUrlAll=ViePerUrl.objects.filter(id__in=Pro)
    Home=1000
    for i in ViePerUrlAll:
        if i.menu_type == 1:
            MenuList.append({"id":i.id,"name":i.title,"MenuB":[]})
        if i.url == request.META['PATH_INFO']:
            Home = i.in_menu
    for i in MenuList:
        for m in ViePerUrlAll:
            if i['id'] == m.in_menu:
                i['MenuB'].append({"id":m.id,"name":m.title,"URL":m.url,"MenuC":[]})
    print request.META['PATH_INFO']
    return MenuList,Home



def InitializePro(gid):
    """初始化权限页面,代码有点自虐,没用js完全用py生成标准html扔到前端"""
    try:
        MenuList=[]
        L=[int(i) for i in UserGroup.objects.get(id=gid).permission.split(",")]
        ViePerUrlAll=ViePerUrl.objects.all()
        for i in ViePerUrlAll:
            if i.menu_type == 1:
                if i.id in L:
                    MenuList.append({"id":i.id,"name":i.title,"checkbox":1,"MenuB":[]})
                else:
                    MenuList.append({"id":i.id,"name":i.title,"checkbox":0,"MenuB":[]})
        for i in MenuList:
            for m in ViePerUrlAll:
                if i['id'] == m.in_menu:
                    if m.id in L:
                        i['MenuB'].append({"id":m.id,"name":m.title,"URL":m.url,"checkbox":1,"MenuC":[]})
                    else:
                        i['MenuB'].append({"id":m.id,"name":m.title,"URL":m.url,"checkbox":0,"MenuC":[]})
        for i in MenuList:
            for m in i['MenuB']:
                for v in ViePerUrlAll:
                    if m['id'] == v.in_menu:
                        if v.id in L:
                            m['MenuC'].append({"id":v.id,"name":v.title,"checkbox":1,"URL":v.url})
                        else:
                            m['MenuC'].append({"id":v.id,"name":v.title,"checkbox":0,"URL":v.url})
        tra="""
        """
        for i in MenuList:
            trb="""
            """
            for m in i["MenuB"]:
                trc=""""""
                td=""""""
                for v in m["MenuC"]:
                    if v["checkbox"]:
                        n=""" <label><a>[<input class="proidp" type="checkbox" checked="checked" name="%s">%s]</a></label>""" %(v["id"],v["name"])
                    else:
                        n=""" <label><a>[<input class="proidp" type="checkbox"  name="%s">%s]</a></label>""" %(v["id"],v["name"])

                    td+="""
        <table cellspacing="2" cellpadding="2" >
                <tr>
                <td >
                %s
                </td>
            </tr>
        </table>
        """ %n

                if m["checkbox"]:
                    n=""" <label><a>[<input class="proidp" type="checkbox" checked="checked" name="%s">%s]</a></label>""" %(m["id"],m["name"])
                else:
                    n=""" <label><a><label>[<input class="proidp" type="checkbox"  name="%s">%s]</a></label>""" %(m["id"],m["name"])
                trc+="""
                <tr>
                <td width="100px" style="text-align:center; margin: 0 auto;">
                   %s
                </td>
                <td width="500px" style="text-align:center; margin: 0 auto;">
                    %s
                </td>
                </tr>
                    """% (n,td)

                trb+="""
        <table  border="1" cellspacing="1" cellpadding="1"  bordercolor="#E0E0E0" >
                <tbody>
                %s
                </tbody>
        </table>
        """ % trc
                if i["checkbox"]:
                    n="""<label>[<input class="proidp" type="checkbox" checked="checked" name="%s">%s]</label>""" %(i["id"],i["name"])
                else:
                    n=""" <label>[<input class="proidp" type="checkbox"  name="%s">%ss]</label>""" %(i["id"],i["name"])
            tra+="""
            <tr>
                <td width="100px" style="text-align:center; margin: 0 auto;" >
                    <a>%s</a>
                </td>
                <td >%s
                </td>
            </tr>
            """% (n,trb)

        html="""
        <form method="post" action="/EditGroupPro/">
        <table width="680px"  border="1" cellspacing="2" cellpadding="2" bordercolor="#E0E0E0">
                <tbody>
                %s
                </tbody>
        </table>
        <br>
            <input type="submit" class="btn btn-primary btn-mini" id="tj_group_button" value="EditGroupPro">
            <input type="hidden" id="gidomg" name="omg">
            <input type="hidden" id="gid" name="gid" value="%s">
        </form>
        <script>
        $("#tj_group_button").click(function(){
        var result = new Array();
        result.push(9999);
        result.push(9998);
        $(".proidp").each(function(){
            if($(this).is(":checked")){
                result.push($(this).attr("name"));
            }})
         $("#gidomg").val(result.toString());
        });
        </script>
        """ % (tra,gid)
        return html
    except Exception,e:
        return 0