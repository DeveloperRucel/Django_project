from django.contrib import admin

from gestionpersonnel.models import Dispenser, Etudiant, Examen, Fonction, Formation, Inscript, Inscription_Stagiaire, Module_Stage, Payement_Etudiant, Personnel, Resultat, Travail


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('id','nom_formation','prix_formation','module','duree')

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('id','Nom_Etudiant', 'Prenom_etudiant', 'Email', 'Telephone', 'adresse', 'nom_parent', 'Sexe', 'tel_parent','Specialite')
@admin.register(Payement_Etudiant)

class Payement_EtudiantAdmin(admin.ModelAdmin):
    list_display = ('id','Email','mode_payement','montant_paye','Reste','Date_Payement')
@admin.register(Fonction)
class FonctionAdmin(admin.ModelAdmin):
    list_display = ('id',"Nom_fonction",)

@admin.register(Personnel)
class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('id','Nom_Personnel','Telephone','Email','Date_naissance','Sexe','addresse','get_fonction','Role','photo')
@admin.register(Module_Stage)
class Module_StageAdmin(admin.ModelAdmin):
    list_display = ('id','nom_module',)


@admin.register(Inscription_Stagiaire)
class Inscription_StagiaireAdmin(admin.ModelAdmin):
    list_display  = ('id','Nom_Stagiaire','Nom_Personnel','Date_inscription')



@admin.register(Dispenser)
class DispenserAdmin(admin.ModelAdmin):
    list_display = ('id','Email', 'take_formation')

@admin.register(Travail)
class TravailAdmin(admin.ModelAdmin):
    list_display = ('id','Email', 'take_formation')

@admin.register(Inscript)

class InscriptAdmin(admin.ModelAdmin):
    list_display = ('id','Email','nom_formation','Date_inscript')


@admin.register(Examen)    

class ExamenAdmin(admin.ModelAdmin):
    list_display = ('id','Nom_Examen','Date_Examen')

@admin.register(Resultat)

class ResultatAdmin(admin.ModelAdmin):
    list_display  = ('id','Email','Nom_Examen','Note_Etudiant','Date_Resultat')


