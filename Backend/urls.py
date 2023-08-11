from django.urls import path
from Backend import views

urlpatterns =[
    path('mainfun/',views.mainfun,name="mainfun"),
    path('Addcat/',views.Addcat,name="Addcat"),
    path('savcat/',views.savcat,name="savcat"),
    path('discat/',views.discat,name="discat"),
    path('editcat/<int:dataid>/',views.editcat,name="editcat"),
    path('updatecat/<int:dataid>/',views.updatecat,name="updatecat"),
    path('deletecat/<int:dataid>/',views.deletecat,name="deletecat"),
    path('Adminpage/',views.Adminpage,name="Adminpage"),
    path('Admin_Login/',views.Admin_Login,name="Admin_Login"),
    path('AdminLogout/',views.AdminLogout,name="AdminLogout"),
    path('displaycontact/',views.displaycontact,name="displaycontact"),
    path('deletecontact/<int:dataid>/',views.deletecontact,name="deletecontact"),
    path('displayuser/',views.displayuser,name="displayuser"),
    path('deleteuser/<int:dataid>/',views.deleteuser,name="deleteuser"),
    path('displaycheck/',views.displaycheck,name="displaycheck"),
    path('deletecheck/<int:dataid>/',views.deletecheck,name="deletecheck"),
]