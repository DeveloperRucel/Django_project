from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from gestionpersonnel.models import Etudiant, Formation, Inscript, Payement_Etudiant, Personnel, Dispenser

Date1 = datetime.now()
#page d'acceuil


# def base(request):
    
#     return render(request, 'administration/base.html')



def index_admin(request):
    # context1 = {'content_index':"La programmation d'un site de gestion avec django"}
    student = Etudiant.objects.count()
    enseignant = Personnel.objects.count()
    formations = Formation.objects.count()
    return render(request, "administration/index.html",{'etudiant': student, 'teacher':enseignant,'formation':formations})
#page de liste des etudiant
def student(request):
    context2 = {'student':Etudiant.objects.all()}

    return render(request, "administration/student.html", context2)
#page des details de l'etudiant
def student_detail(request, etudiant_id):
    context = {'student_detail': get_object_or_404(Etudiant, pk = etudiant_id )}
    # E_intance = Etudiant.objects.get( pk = etudiant_id)
    # Email = E_intance.Email
    # payement = get_object_or_404(Payement_Etudiant, Email = Email)

    return render(request, 'administration/student-detail.html', context)
#page de dashbord en dark
def dashbord_dark(request):
    context3 = {'content_dashbord':'Le Dashbord du site en mode dark '}
    return render(request, 'administration/index-2.html',context3)
#page de listes des enseignants
def teacher(request):
    teacher = Personnel.objects.all().select_related('Dispenser')
    enseignant = Personnel.objects.all() 
    

    return render(request, 'administration/teacher.html', {'teacher':enseignant})
#page des details des enseignants
def teacher_detail(request, personnel_id):
    context5 = {'teacher_detail': get_object_or_404(Personnel, pk = personnel_id )}
    return render(request, 'administration/teacher-detail.html', context5)

def add_student(request):
    content_formation  = {'special':Formation.objects.all()}
    content_etude = {'etudient': Etudiant.objects.all()}
    message_insert  = 'insertion de l\'etudiant reussi'
    context6 = {'content_add_student':"AJout de l'etudiant "}
    if request.method == "POST":
        E_Telephone = request.POST.get('Telephone')
        E_Nom_Etudiant = request.POST.get('nom_etudiant')
        E_Prenom_etudiant = request.POST.get('prenom')
        E_Email = request.POST.get('email')
        E_adresse= request.POST.get('adresse')
        E_nom_parent = request.POST.get('nom_parent')
        E_Sexe = request.POST.get('sexe')
        E_Date_naissance = request.POST.get('date_naissance')
        
        E_Tel_parent = request.POST.get('tel_parent')
        E_Specialite = request.POST.get('formation_choisi')
        E_photo = request.POST.get('image')

        E_formation_intance = Formation.objects.get(nom_formation = E_Specialite)
            
        my_student  = Etudiant.objects.create(Nom_Etudiant=E_Nom_Etudiant, Prenom_etudiant=E_Prenom_etudiant, Telephone=E_Telephone, Email=E_Email, Date_naissance =E_Date_naissance, Sexe=E_Sexe, Specialite=E_formation_intance, photo=E_photo, adresse=E_adresse, nom_parent=E_nom_parent, tel_parent=E_Tel_parent)
        my_student.save()
        # my_section = {
        #     'id':Etudiant.id,
        #     'Email':Etudiant.Email,
        #     'Montant_verse' :Etudiant.Montant_verse,
        #     'formation':Etudiant.Specialite,
        # }
        # request.session['my_student'] = my_section

        return redirect('admin_gestion:payement_page')
    return render(request, 'administration/add-student.html',content_formation)
def payement(request):
    
    my_section ={'my_section':Etudiant.objects.all(), 'special':Formation.objects.all()} 
    if request.method == "POST":
        E_Email = request.POST['email']
        my_section_email = Etudiant.objects.get(Email= E_Email)
        E_Specialite = request.POST['formation_choisi']
        E_formation_intance = Formation.objects.get(nom_formation = E_Specialite)
        E_mode_payement= request.POST['mode_payement']
        E_Montant_verse = request.POST['Montant_verse']
        E_prix_formation = request.POST['prix_total']
        E_Reste = int(E_prix_formation) - int(E_Montant_verse)
        E_Date_Payement = Date1

        # mon_paye = (mode_payement = E_mode_payement, Nom_Etudiant = E_Nom_Etudiant,Montant_verse= E_Montant_verse, Reste = E_Reste, Date_Payement =E_Date_Payement)
        mon_payement = Payement_Etudiant.objects.create(mode_payement = E_mode_payement, Email = my_section_email, montant_paye = E_Montant_verse, Reste = E_Reste, Date_Payement =E_Date_Payement)
        # mon_inscript = (Nom_Etudiant=E_Nom_Etudiant, nom_formation = E_formation_intance, Date_inscript= E_Date_Payement)
        mon_inscription = Inscript.objects.create(Email = my_section_email, nom_formation = E_formation_intance, Date_inscript= E_Date_Payement)
        mon_payement.save()
        mon_inscription.save()
        return redirect(reverse("admin_gestion:student_page"))

    return render(request,'administration/payement.html', my_section)

def suppression_etudiant(request, etudiant_id):
    conntext_sup = {'message_sup':"Etudiant supprimer avec success"}
    supprimer = Etudiant.objects.get(pk = etudiant_id)
    supprimer.delete()
    return render(request, 'administration/student.html',conntext_sup)

def essai(request):
    context = {'message':'Le contenu de la page d\'essai'}
    return render(request, 'administration/essai.html')
def add_teacher(request):
    context7 = {'content_add_teacher':'Ajout d\'un Enseignant'}
    if request.method == "POST":
        T_nom = request.POST['nom']
        T_prenom = request.POST['prenom']
        T_email = request.POST['email']
        T_adresse = request.POST['adresse']
        T_date_birth = request.POST['date_birth']
        T_telephone = request.POST['phone']
        T_image = request.POST['image']
        T_university = request.POST['university']
        T_date_debut = request.POST['debut_date']
        T_date_fin = request.POST['fin_date']
        T_niveau_etude = request.POST['niveau']
        T_pays = request.POST['pays']
        T_fonction = 'Enseignant'
        T_role = 'Enseignant'
        T_sexe = request.POST['sexe']
        my_teacher = Personnel.objects.create(Nom_Personnel = T_nom, Prenom_Personnel = T_prenom, Email = T_email, Telephone = T_telephone, addresse = T_adresse, Date_naissance = T_date_birth, Sexe = T_sexe, Fonction = T_fonction, Role = T_role, University = T_university, date_debut_universite = T_date_debut, date_fin_universite = T_date_fin, niveau_etude = T_niveau_etude, pays = T_pays,photo = T_image )
        my_teacher.save()
        return redirect(reverse('admin_gestion:teacher_page'))


    return render(request, 'administration/add-teacher.html',context7 )

def login_view(request):
    context_login = {'content_login':"Connexion"}
    erreur = 'Username or Password incorrect'
    erreur_username = 'veiller entrer votre nom utilsateur'
    erreur_password = 'ce champ ne peux pas etre vide'
    # message = {"authentification reussi !!!"}
    if request.method == "POST":
        
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username = username, password = password)
        if username == '':
            return render(request, 'administration/page-login.html',{'erreur_username':erreur_username})
        if password =='':
            return render(request, 'administration/page-login.html',{'erreur_password':erreur_password})
        if user is not None:
            login(request, user) 
            
            return HttpResponseRedirect("dashbord")
        else:
            return render(request, 'administration/page-login.html',{'erreur':erreur})

    return render(request, 'administration/page-login.html',context_login)

def register(request):
    context_register = {'content_register':'Inscription'}
    message_erreur = {'message_erreur':'essayer une nouvelle methode de connexion'}
    if request.method == "POST":
      U_name = request.POST.get('Username')
      U_email = request.POST.get('Email')
      U_password = request.POST.get('Password')
      my_user = User.objects.create_user(U_name, U_email, U_password)
      my_user.save()
      return redirect('admin_gestion:login_page')
    else:
        return render(request,'administration/page-register.html',message_erreur)
    return render(request, 'administration/page-register.html', context_register)

def user_detail(request):
    context = {'content_user':"Les utilisateurs"}
    return render(request, 'administration/user.html',context)

def chat(request):
    context = {'content_chat':"Le Chat"}
    return render(request, 'administration/chat.html',context)

def calendar(request):
    context = {'content_calendar':"Le Calendrier"}
    return render(request, 'administration/calendar.html',context)

def stagiaire(request):
    context = {'content_stage':"Liste des Stagiaires"}
    return render(request, 'administration/stagiaire.html',context)

def add_stagiaire(request):
    context = {'content_add_stage':"Ajout d'un Stagiaire"}
    return render(request, 'administration/add-stagiaire.html',context)

def stagiaire_detail(request):
    context = {'content_detail_stagiaire':"Detail Stagiaire"}
    return render(request, 'administration/stagiaire-detail.html',context)

def chat_teacher(request):
    context_chat = {'content_chat':'Les messages sont affiche ici '}
    return render(request, 'gestionpersonnel/chat.html', context_chat)



def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('admin_gestion:login_page'))
