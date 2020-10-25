from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    url(r'^$', views.index, name='home'),
    url(r'^accounts/profile/', views.index, name='logged_in'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/(\d+)/$', views.profile, name='profile'),
    url(r'^profile/visit/(\d+)/$', views.profilevisit, name='profilevisit'),
    url(r'^create/profile/$', views.create_profile, name='createprofile'),
    url(r'^profile/edit/(\d+)/$', views.editprofile, name='editprofile'),
    url(r'^like/(\d+)/$', views.likeview, name='like_post'),
    url(r'^follow/(\d+)/$', views.followview, name='follow'),
    #url(r'^comment/(\d)/$', views.write_comment, name='write-comment'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'detail/(\d+)/$', views.view_post, name='detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
