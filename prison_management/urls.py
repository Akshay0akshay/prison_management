"""
URL configuration for prison_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from prison_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('users-login/',views.users_login),
    path('guest-view-criminal/',views.guest_view_criminal),
    #admin
    path('admin-dashboard/',views.admin_dashboard),
    path('admin-approve_police/',views.admin_approve_police),
    path('admin-approve_allpolice/',views.admin_approve_allpolice),
    path('admin-approve_singlepolice/',views.admin_approve_singlepolice),
    path('admin-reject_singlepolice/',views.admin_reject_singlepolice),
    path('admin-view_police/',views.admin_view_police),
    path('admin-view_jailor/',views.admin_view_jailor),
    path('admin-view_criminals/',views.admin_view_criminals),
    path('admin_view_prisoner_detailed/',views.admin_view_prisoner_detailed),
    path('admin-view-police-duty/',views.admin_view_police_duty),
    path('admin-visitor-list/',views.admin_visitor_list),
    #police
    path('police-register/',views.police_register),
    path('police_dashboard/',views.police_dashboard),
    path('police-view-profile/',views.police_view_profile),
    path('police-updateprofile/',views.police_updateprofile),
    path('police-view-prisoners/',views.police_view_prisoners),
    path('police_view_prisoner_detailed/',views.police_view_prisoner_detailed),
    path('police_add_remarks/',views.police_add_remarks),
    path('police_request_parole/',views.police_request_parole),
    path('police_view_parole_status/',views.police_view_parole_status),
    path('police_view_duties/',views.police_view_duties),
    path('police_visitors_list/',views.police_visitors_list),
    #jailor
    path('jailor-dashboard/',views.jailor_dashboard),
    path('jailor-add-prisoner/',views.jailor_add_prisoner),
    path('jailor-view-prisoners/',views.jailor_view_prisoners),
    path('jailor_view_prisoner_detailed/',views.jailor_view_prisoner_detailed),
    path('jailor_edit_prisoner_detailed/',views.jailor_edit_prisoner_detailed),
    path('jailor_delete_prisoner_detailed/',views.jailor_delete_prisoner_detailed),
    path('jailor-add-duty/',views.jailor_add_duty),
    path('jailor-view-polices/',views.jailor_view_polices),
    path('jailor-deletesinglepolice/',views.jailor_deletesinglepolice),
    path('jailor-delete-duty/',views.jailor_delete_duty),
    path('jailor-view-police-duty/',views.jailor_view_police_duty),
    path('jailor-view-parole_list/',views.jailor_view_parole_list),
    path('jailor-accept-parole/',views.jailor_accept_parole),
    path('jailor-reject-parole/',views.jailor_reject_parole),
    path('jailor-view-visitors/',views.jailor_view_visitors),
]
