from django.conf.urls import url
from django.contrib import admin


class MyAdmin(admin.AdminSite):
    site_header = "Administration E. P. T."

    # def get_urls(self):
    #     urls = super(MyAdmin, 
    #                 self).get_urls()
    #     custom_urls = [
    #                     url('home/myadmin',
    #                     self.admin_view())
    #     ]


my_admin = MyAdmin(name="my_admin")

