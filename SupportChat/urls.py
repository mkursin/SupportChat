from django.conf.urls import patterns, include, url

from django.contrib import admin
from ChatAdmin.views import add_question_by_db, list_question_by_db
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SupportChat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^question', add_question_by_db),
    url(r'^list', list_question_by_db),



)
