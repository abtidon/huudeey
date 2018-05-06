from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Prodsale(models.Model):
    prodname = models.CharField(db_column='prodName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prodcode = models.CharField(db_column='prodCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(max_length=20, blank=True, null=True)
    saledate = models.DateField(db_column='saleDate', blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(blank=True, null=True)
    unitcost = models.FloatField(blank=True, null=True)
    totlcost = models.FloatField(blank=True, null=True)
    prodsale_id = models.AutoField(primary_key=True)

    class Meta:
        #managed = False
        managed = True
        db_table = 'prodsale'
