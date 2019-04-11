from django.db import models

# Create your models here.


class Person(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Case(models.Model):

    summary = models.TextField()
    litigants = models.ManyToManyField(Person, through='Litigant'  )

    def __str__(self):
        return 'Case %s' % (self.id)

class PersonCase(models.Model):

    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_to_case')
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='case_to_person')
    role = models.TextField()