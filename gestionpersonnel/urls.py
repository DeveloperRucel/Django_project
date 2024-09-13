
from . import views
from django.urls import path


app_name = "admin_gestion"
urlpatterns = [
    ####page de connexion et dashbord
    path('', views.login_view, name = "login_page"),
    path('dashbord', views.index_admin, name = "index_admin"),
    path('admin_dark',views.dashbord_dark, name="index_admin_dark"),


    ####information sur les etudiants
    path('liste_etudiant',views.student, name="student_page"),
    path('detail_etudiant/<int:etudiant_id>',views.student_detail, name="student_detail"),
    path('payement_etudiant/', views.payement, name = 'payement_page'),
    path('liste_enseignant', views.teacher, name="teacher_page"),
    path('ajout_etudiant', views.add_student, name = "student_add_page"),
    path('suppresssion_etudiant/<int:etudiant_id>',views.suppression_etudiant, name = 'suppression_etudiant'),


    ####information sur les enseignants
    path('detail_enseignant/<int:personnel_id>', views.teacher_detail, name="teacher_detail"),
    
    
    path('ajout_enseignant', views.add_teacher, name = "teacher_add_page"),
    path('register_user-institut-account-super', views.register, name = "register_page"),
    path('user', views.user_detail, name="user_detail_page"),
    path('chat', views.chat, name="chat_page"),
    path('calendar', views.calendar, name= "calendar_page"),
    path('stagiaire', views.stagiaire, name = "stagiaire_page"),
    path('ajout_stagiare',views.add_stagiaire, name="stagiaire_add_page"),
    path('detail_stagiaire',views.stagiaire_detail, name="stagiaire_detail"),
    path("logout-admin", views.logout_user, name="deconnexion")

]