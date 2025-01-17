"""s3_browser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required

from djangoS3Browser.s3_browser import settings
from djangoS3Browser.s3_browser import views

urlpatterns = [
    url(r'^get_folder_items/(.+)/(.+)/$', staff_member_required(views.get_folder_items), name='get_folder_items'),
    url(r'^upload/$', staff_member_required(views.upload), name='upload'),
    url(r'^create_folder/$', staff_member_required(views.create_folder), name='create_folder'),

    url(r'^download/$', staff_member_required(views.download), name='download'),
    url(r'^get_item/$', staff_member_required(views.get_item), name='get_item'),
    url(r'^get_item_content/$', staff_member_required(views.get_item_content), name='get_item_content'),
    url(r'^update_item_content/$', staff_member_required(views.update_item_content), name='update_item_content'),

    url(r'^rename_file/$', staff_member_required(views.rename_file), name='rename_file'),
    url(r'^paste_file/$', staff_member_required(views.paste_file), name='paste_file'),
    url(r'^move_file/$', staff_member_required(views.move_file), name='move_file'),
    url(r'^delete_file/$', staff_member_required(views.delete_file), name='delete_file'),
    url(r'', staff_member_required(views.admin_index), name='admin_index')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
