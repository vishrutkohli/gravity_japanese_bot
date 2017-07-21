from django.conf.urls import patterns, include, url
from django.contrib import admin
import messengerbot.views as v
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DHLchatbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^facebook_auth/?$',v.MyChatBotView.as_view()),
    url(r'^index$',v.index),
    url(r'^otp_form$',v.otp_form),
    url(r'^receipt$',v.receipt),
    url(r'^track$',v.track),
    url(r'^help$',v.help),
    url(r'^identity_confirmed$',v.identity_confirm),
    url(r'^api_ai$', v.api_ai_webhook, name='api_ai'),


    url(r'^admin/', include(admin.site.urls)),
)

