from django.urls import path
import xmpp.views as views

urlpatterns = [
    path("xhr/search/user/", views.XhrUserSearchView.as_view(), name="xmpp_xhr_user_search"),
    path("xhr/autojoin/", views.XhrAutoJoinView.as_view(), name="xmpp_xhr_autojoin"),
]
