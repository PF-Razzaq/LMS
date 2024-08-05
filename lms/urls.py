from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^teacher_list/$', views.TeacherList.as_view(), name='teacher_list'),
    re_path(r'^teacher_detail/(?P<pk>\d+)/$', views.TeacherDetail.as_view(), name='teacher_detail'),
]
