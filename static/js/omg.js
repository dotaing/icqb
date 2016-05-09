

$("#login_button").click(function(){
var SMD5 = $("#ntime").val();
var U = $("#id_myname").val();
var P = $.md5($("#id_passwd").val());
var MN = SMD5 + U + P;

$("#password_n").attr("value",$.md5(MN));
});

$("#del_button").click(function(){
    var result = new Array();
    var result_name=new Array();
    $("table input:checkbox").each(function(){
        if($(this).is(":checked")){
            result.push($(this).attr("value"));
            result_name.push($(this).attr("uname"));
        }})
    if(result.length < 1){
        alert("请勾选要删除的用户!");
        return;
    }
    if(confirm('确定要删除以下用户  ' + result_name + ' ？' )){
    $("#uid").val(result.join(","));
    $("#delu").submit();
     }
});

$("#add_button").click(function(){
    $("#add_password").attr("value",$.md5($("#add_password").val()));
    $("#basic_validate").submit();
});


$("#edit_button").click(function(){
    var result = new Array();
    var result_name=new Array();
    $("table input:checkbox").each(function(){
        if($(this).is(":checked")){
            result.push($(this).attr("value"));
            result_name.push($(this).attr("uname"));
        }})
    if(result.length < 1){
        alert("请勾选要修改的用户!");
        return;
    }
    if(result.length > 1){
        alert("只能修改一个用户!");
        return;
    }

JSON={'uid':result.join(",")}
$.ajax({
type:'post',
url:'/EditUserJson/',
dataType: "json",
data:JSON,
success:function(data){
    $("#edit_user").html(data)
        $("#myAlert2").modal();
},
error:function(){alert(1)}
});

});


$(".edit_group").click(function(){
JSON={'gid':this.name};
$.ajax({
type:'post',
url:'/EditGroupJson/',
dataType: "json",
data:JSON,
success:function(data){
    $("#editgroup_body").html(data);
    $("#myAlert").modal();
},
error:function(){alert(1)}
});

});

$(".GetLog").click(function(){
JSON={'TID':this.name};
$.ajax({
type:'post',
url:'/GetLogData/',
dataType: "json",
data:JSON,
success:function(data){
    $("#html_body").html(data)
    $("#myAlert").modal();
},
error:function(){
    $("#html_body").html("Error")
    $("#myAlert").modal();
}
});

});


$(".delhefu").click(function(){
JSON={'TID':this.name}
if(confirm('确认要删除这个合服任务' + this.name + ' ？' )){
    $.ajax({
type:'post',
url:'/DelAtTask/',
dataType: "json",
data:JSON,
success:function(data){
alert(data);
},
error:function(){
alert("请求错误或没权限！");
}
});
 }
});