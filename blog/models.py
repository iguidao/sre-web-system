from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Deploy_history(models.Model):
    staff_name = models.CharField(max_length=20)
    project_name = models.CharField(max_length=100)
    deploy_name = models.CharField(max_length=100)
    ip_name = models.CharField(max_length=1000)
    update_time = models.DateTimeField('update_time', auto_now_add=True)

    def __unicode__(self):
        return  self.staff_name

# Create your models here.

class Property_operation_history(models.Model):
    staff_name = models.CharField(max_length=1000)
    ip_name = models.CharField(max_length=100000)
    operation_name = models.CharField(max_length=100000, blank=True, null=True)
    update_time = models.DateTimeField('update_time', auto_now_add=True)

class Property_content(models.Model):
    team_name = models.CharField(max_length=100, blank=True, null=True)
    domain_name = models.CharField(max_length=1000, blank=True, null=True)
    ip_name = models.CharField(max_length=100)
    ip_remark = models.CharField(max_length=100, blank=True, null=True)
    app_name = models.CharField(max_length=100, blank=True, null=True)
    system_name = models.CharField(max_length=100, blank=True, null=True)
    principal_name = models.CharField(max_length=100, blank=True, null=True)
    xen_name = models.CharField(max_length=100, blank=True, null=True)
    room_name = models.CharField(max_length=100, blank=True, null=True)
    xen_ip = models.CharField(max_length=100, blank=True, null=True)
    host_cpu = models.CharField(max_length=100, blank=True, null=True)
    host_memory = models.CharField(max_length=100, blank=True, null=True)
    host_disk = models.CharField(max_length=100, blank=True, null=True)
    server_model = models.CharField(max_length=100, blank=True, null=True)
    update_time = models.DateTimeField('update_time', auto_now_add=True)
    class Meta:
        unique_together = ("team_name", "ip_name")


# Create your models here.

class Weekly_report(models.Model):
    staff_name = models.CharField(max_length=20)
    start_time = models.DateField()
    #start_time = models.DateTimeField(blank=True, null=True)
    #end_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateField()
    report_content = models.CharField(max_length=1000)
    update_time = models.DateTimeField('update_time', auto_now_add=True)

    def __unicode__(self):
        return  self.staff_name

# Create your models here.

class Work_time(models.Model):
    staff_name = models.CharField(max_length=20)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    #date_number = models.CharField(max_length=20)
    duration_number = models.FloatField(blank=True, null=True)
    type_name = models.CharField(max_length=100)
    development_name = models.CharField(max_length=20)
    reason_explain = models.CharField(max_length=1000)
    update_time = models.DateTimeField('update_time', auto_now_add=True)

    def __unicode__(self):
        return  self.staff_name
