from django.conf.urls import patterns, include, url
from django.contrib import admin
import messengerbot.views as v
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DHLchatbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^facebook_auth/?$',v.MyChatBotView.as_view()),
    url(r'^index$',v.index),

    url(r'^admin/', include(admin.site.urls)),
)
