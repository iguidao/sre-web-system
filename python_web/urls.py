"""python_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog import views

urlpatterns = [
    #url(r'^test/',views.test,name='test'),
    url(r'^$', views.home),
    url(r'^admin', include(admin.site.urls)),
    url(r'^login', views.login_view),
    url(r'^logout', views.logout_view),
    url(r'^changepwd', views.changepwd),
    url(r'^chpasswd', views.chpasswd),

    url(r'^index', views.index),
    url(r'^project_deploy_install', views.project_deploy_install),
    url(r'^deploy_details', views.deploy_history_details),

    url(r'^property_add', views.property_add),
    url(r'^property_details', views.property_details),
    url(r'^property_operation', views.property_operation),
    url(r'^property_write', views.property_write),
    url(r'^property_delete', views.property_record_delete),
    url(r'^property_query', views.property_record_query),

    url(r'^weekly_report_add', views.weekly_report_add),
    url(r'^this_week_content', views.this_week_content),
    url(r'^report_details', views.report_details),
    url(r'^report_add', views.report_add),

    url(r'^work_add', views.work_add),
    url(r'^work_record_write', views.work_record_write),
    url(r'^work_delete', views.work_record_delete),
    url(r'^work_details', views.work_record_details),
    url(r'^work_admin_details', views.work_admin_record_details),

]

