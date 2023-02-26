from django.urls import path
from .views import adminconsoleView,profileView,contactView,faqView,accountsettingsView,welcomeView,profileupdateView,selectshopView

urlpatterns = [
    path('admin-console/', adminconsoleView, name="adminconsoleUrl"),
    path('profile/', profileView, name="profileUrl"),
    path('contact-tck/', contactView, name="contactTCKUrl"),
    path('faqs/', faqView, name="faqUrl"),
    path('home/', adminconsoleView, name="homeUrl"),
    path('account-settings/', accountsettingsView, name='accountsettingsUrl'),
    path('', welcomeView, name='welcomeUrl'),
    path('select-shops/',selectshopView, name='selectshopUrl'),
    path('update-profile/', profileupdateView, name='profileupdateUrl')
]
