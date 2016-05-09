#-*- coding:UTF-8 -*-
__author__ = 'maomao'

from django.conf.urls import patterns, include, url

import os
# Static files (CSS, JavaScript, Images)

from django.conf import settings

#登录操作,用户管理
urlpatterns = patterns('userpro.views',
   url(r'^$','LoginIndex'),
   url(r'^LoginIn/','LoginIn'),
   url(r'^LoginOut/','LoginOut'),
   #用户管理
   url(r'^ShowUserList/','ShowUserList'),
   url(r'^AddUser/','AddUser'),
   url(r'^DelUser/','DelUser'),
   url(r'^EditUser/','EditUser'),
   url(r'^EditUserJson/','EditUserJson'),
   #组管理
   url(r'^ShowGroupList/','ShowGroupList'),
   url(r'^EditGroupJson/','EditGroupJson'),
   url(r'^EditGroupPro/','EditGroupPro'),
)


urlpatterns += patterns('works.views',
   url(r'^ServerList/','ServerList'),
   url(r'^Home/','Home'),
)





#静态资源,JS,CSS
urlpatterns += patterns('',
    url(r'^lib/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_DIR}),
)
