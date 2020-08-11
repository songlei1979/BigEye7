from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Client(models.Model):
    ClientID = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=25, null=False, blank=False)
    FirstName = models.CharField(max_length=25, null=False, blank=False)
    StreetAddress = models.CharField(max_length=50, null=False, blank=False)
    Suburb = models.CharField(max_length=20, null=False, blank=False)
    City = models.CharField(max_length=25, null=False, blank=False)
    PhoneNumbrer = models.CharField(max_length=16, null=True, blank=True)
    EmailAddress = models.CharField(max_length=30, null=True, blank=True)
    status = (
        ('Valid', 'Valid'),
        ('Invalid', 'Invalid'),
    )
    ClientStatus = models.CharField(max_length=7, choices=status, null=False, blank=False)

class Case(models.Model):
    CaseID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=40, null=False, blank=False)
    Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    types = (
        ('Insurance Check', 'Insurance Check'),
        ('Surveillance', 'Surveillance'),
        ('Credit Check', 'Credit Check'),
        ('Employee Background Check', 'Employee Background Check'),
        ('Accident Report', 'Accident Report'),
        ('Security Inspection', 'Security Inspection'),
    )
    CaseType = models.CharField(max_length=50, choices=types, null=False, blank=False)
    CaseDate = models.DateField(null=False, blank=False)
    status = (
        ('Open', 'Open'),
        ('Complete', 'Complete'),
        ('Closed', 'Closed'),
    )
    Status = models.CharField(max_length=50, choices=status, null=False, blank=False)
    Fee = models.FloatField(validators=[MaxValueValidator(50000), MinValueValidator(200)], null=False, blank=False)
    Notes = models.CharField(max_length=100, null=True, blank=True)

class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    PaymentDate = models.DateField(null=False, blank=False)
    Amount = models.FloatField(validators=[MaxValueValidator(50000), MinValueValidator(50)], null=False, blank=False)
    Case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Investigator(models.Model):
    InvestigatorID = models.AutoField(primary_key=True)
    LastName = models.CharField(max_length=30, null=False, blank=False)
    FirstName = models.CharField(max_length=30, null=False, blank=False)
    StreetAddress = models.CharField(max_length=50, null=False, blank=False)
    Suburb = models.CharField(max_length=20, null=False, blank=False)
    PhoneNumbrer = models.CharField(max_length=16, null=False, blank=False)
    HourlyRate = models.FloatField(validators=[MaxValueValidator(80), MinValueValidator(15)], null=False, blank=False)

class Equipment(models.Model):
    EquipmentID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=50, null=False, blank=False)
    Cost = models.FloatField(validators=[MaxValueValidator(5000), MinValueValidator(10)], null=False, blank=False)

class Assignment(models.Model):
    Investigator = models.ForeignKey(Investigator, on_delete=models.CASCADE, to_field='InvestigatorID', null=False, blank=False)
    Case = models.ForeignKey(Case, on_delete=models.CASCADE, to_field='CaseID', null=False, blank=False)
    hours = models.IntegerField(validators=[MaxValueValidator(400), MinValueValidator(1)], null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'eye_assignment'
        unique_together = (('Investigator_id',
                            'Case_id'),)

class Allocation(models.Model):
    Case = models.ForeignKey(Case, on_delete=models.CASCADE, to_field='CaseID', null=False, blank=False)
    Equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, to_field='EquipmentID', blank=False, null=False)
    AllocationDate = models.DateField(null=False, blank=False)

    class Meta:
        managed = False
        db_table = 'eye_allocation'
        unique_together = (('Case_id',
                            'Equipment_id'),)
