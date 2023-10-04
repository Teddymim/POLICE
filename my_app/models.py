from django.db import models



class Criminal(models.Model):
    criminal_name = models.CharField(max_length = 40)
    gender = models.CharField(max_length = 12)
    age = models.IntegerField()
    next_of_kin = models.CharField(max_length = 30)

def __str__(self):
    return f"{self.criminal_name}-{self.gender}-{self.age}-{self.next_of_kin}"

class Crime(models.Model):
    crime_date = models.DateField(auto_now= False)
    crime_time = models.IntegerField()
    offence = models.CharField(max_length = 14)
    location = models.CharField(max_length = 23)
    

def __str__(self):
    return f"{self.crime_date}-{self.crime_time}-{self.offence}-{self.location}"


class Casuality(models.Model):
    crime = models.ForeignKey(Crime, on_delete = models.CASCADE)
    casuality_name = models.CharField(max_length = 24)
    gender = models.CharField(max_length = 24)
    effect = models.CharField(max_length = 22)
    

def __str__(self):
    return f"{self.crime}-{self.casuality}-{self.gender}-{self.effect}"


class Witness(models.Model):
    crime = models.ForeignKey(Crime, on_delete = models.CASCADE)
    witness_name = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 24)
    contact = models.CharField(max_length = 13)
def __str__(self):
    return f"{self.crime}-{self.witness_name}-{self.gender}-{self.contact}"


class Offence(models.Model):
    offence_name = models.CharField(max_length = 21)
    penalty = models.CharField(max_length = 25)
    description = models.TextField()
    
def __str__(self):
    return f"{self.offence_name}-{self.penalty}-{self.description}"


