from django.db import models

# Create your models here.
class ActionList(models.Model):
    name = models.CharField('action_name', max_length=50)

    def __str__(self) -> str:
        return self.name
    

class User(models.Model):
    firstname = models.CharField('firstname', max_length=50, null=False)
    lastname = models.CharField("lastname", max_length=50, null=False)
    age = models.PositiveIntegerField("user_age", null=False)
    sex = models.CharField("user_sex", max_length=10, null=False)
    occupation = models.CharField("user_occupation", max_length=50, null=False)
    phone = models.CharField('user_phone', max_length=20, unique=True, null=False)
    email = models.EmailField('user_email', max_length=70, unique=True, null=False)
    pass1 = models.CharField('user_pass1', max_length=50, null=False)
    pass2 = models.CharField("user_pass2", max_length=50, null=False)

    def __str__(self) -> str:
        return self.firstname + ' ' + self.lastname

class ActionRecord(models.Model):
    date = models.DateField('action_date', null=False)
    name = models.CharField('action_name', max_length=50, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

# New class Addition.
