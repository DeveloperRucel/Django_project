
from datetime import datetime
from django.db import models


iso8601_datetime = '2024-01-16T11:12:00'
dateformat = datetime.fromisoformat(iso8601_datetime)
class Formation(models.Model):
    nom_formation = models.CharField(max_length = 50, verbose_name = "Specialite")
    module = models.CharField(max_length = 200, verbose_name = 'Description')
    prix_formation = models.IntegerField()
    duree = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.nom_formation
    
    class Meta:
        verbose_name = 'Formation'
        verbose_name_plural = 'Formations'

class Examen(models.Model):
    Nom_Examen = models.CharField(max_length = 60, verbose_name = "Nom Examen", default = "Examen")
    Date_Examen = models.DateTimeField(default = dateformat)
    class Meta:
        verbose_name = 'Examen'
        verbose_name_plural = "Examens"


class Etudiant(models.Model):
    Nom_Etudiant = models.CharField(max_length = 70)
    def __str__(self) -> str:
        return self.Nom_Etudiant
    Prenom_etudiant = models.CharField(max_length = 70)
    Telephone = models.IntegerField(unique = True, null = False, default = "656317630")
    Email = models.EmailField(max_length = 70,unique = True)
    def __str__(self) -> str:
        return self.Email
    Date_naissance = models.DateField()
    Sexe= models.CharField(max_length = 20)
    Specialite = models.ForeignKey(Formation, on_delete = models.CASCADE)
    photo = models.ImageField(verbose_name='Photo', upload_to='static/images/profile/')
    adresse = models.CharField(max_length = 60)
    nom_parent = models.CharField(max_length = 70)
    tel_parent = models.IntegerField()
    class Meta:
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants"


class Stagiaire(models.Model):
    Nom_Stagiaire = models.CharField(max_length = 70)
    Telephone = models.IntegerField(unique = True)
    Email = models.EmailField(max_length = 100, unique = True)
    Date_naissance = models.DateField()
    Sexe= models.CharField(max_length = 20)
    Payement = models.IntegerField( verbose_name = "Montant Paye" )
    photo = models.ImageField(upload_to='static/images/profile/', verbose_name='Photo')


class Payement_Etudiant(models.Model):
    mode_payement = models.CharField(max_length = 50)
    Email = models.ForeignKey(Etudiant, on_delete = models.CASCADE, verbose_name = 'Montant Paye par ')
    def __type__ (self):
        return self.Email
    montant_paye = models.IntegerField()
    Reste = models.IntegerField(default = 100000)
    Date_Payement = models.DateTimeField(default = dateformat)



class Fonction(models.Model):
    Nom_fonction  = models.CharField(max_length = 50)
    def __str__(self) -> str:
        return self.Nom_fonction



class Personnel(models.Model):
    Nom_Personnel = models.CharField(max_length = 70)
    def __str__(self) -> str:
        return self.Nom_Personnel
    Prenom_Personnel = models.CharField(max_length = 64, default = "Teacher")
    Telephone = models.IntegerField(unique = True)
    Email = models.EmailField(max_length = 70,unique = True)
    addresse = models.CharField(max_length = 64, verbose_name = "Adresse", default = 'Cameroun-Dchang')
    Date_naissance = models.DateField()
    Sexe= models.CharField(max_length = 20, default ="Masculin")
    Fonction = models.ManyToManyField(Fonction, verbose_name = "Fonction")
    Role = models.CharField(max_length = 30)
    photo = models.ImageField(verbose_name='Photo', upload_to='static/images/profile/')
    Universite = models.CharField(max_length = 64, default = "NANFAH")
    date_debut_universite = models.DateField(null = False, default = dateformat)
    date_fin_universite = models.DateField(null = False, default = dateformat)
    niveau_etude = models.CharField(max_length = 64, default ="Master")
    pays = models.CharField(max_length = 64, default = 'Cameroun')

    def get_fonction(self):
        return "\n".join([f.Nom_fonction for f in self.Fonction.all()])

class Module_Stage(models.Model):
    nom_module = models.CharField(max_length = 50)
    


class Inscription_Stagiaire(models.Model):
    
    Nom_Personnel = models.ForeignKey(Personnel, on_delete = models.CASCADE, verbose_name= 'Nom_Personnel')
    def __str__(self):
        return self.Nom_Personnel
    Nom_Stagiaire = models.ForeignKey(Stagiaire, on_delete = models.CASCADE, verbose_name = "Nom_stagiare")
    def __str__(self):
        return self.Nom_Stagiaire
    Date_inscription = models.DateTimeField(default = dateformat)


class Inscript(models.Model):
    Email = models.ForeignKey(Etudiant, on_delete = models.CASCADE, verbose_name = 'Email Etudiant')
    
    nom_formation = models.ForeignKey(Formation, on_delete = models.CASCADE, verbose_name = "Formation Choisi")
  
    
    Date_inscript= models.DateTimeField(default = dateformat)


class Dispenser(models.Model):
    Email = models.ForeignKey(Personnel, on_delete = models.CASCADE, verbose_name = 'Email Enseignant', default = 1)
    Nom_Formation = models.ManyToManyField(Formation, verbose_name = 'Nom Formation')
    def take_formation(self):
        return "\n".join([f.nom_formation for f in self.Formation.all()])

class Travail(models.Model):
    Email = models.ForeignKey(Personnel, on_delete = models.CASCADE, verbose_name = 'Email Enseignant', default = 1)
    Nom_Formation = models.ManyToManyField(Formation, verbose_name = 'Nom Formation')
    def take_formation(self):
        return "\n".join([f.nom_formation for f in self.Formation.all()])
class Resultat(models.Model):
    Email = models.ForeignKey(Etudiant, on_delete = models.CASCADE, verbose_name = 'Nom Etudiant')

    Nom_Examen = models.ForeignKey(Examen, on_delete = models.CASCADE, verbose_name = 'Nom Examen')

    Note_Etudiant  = models.IntegerField()
    Date_Resultat = models.DateTimeField(default = dateformat )


