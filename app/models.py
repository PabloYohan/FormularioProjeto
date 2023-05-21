# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Valores(models.Model):
    entrada = models.CharField(db_column='Entrada', primary_key=True, max_length=15)  # Field name made lowercase.
    data = models.CharField(db_column='Data', max_length=11)  # Field name made lowercase.
    produto = models.CharField(db_column='Produto', max_length=20)  # Field name made lowercase.
    h_disp = models.FloatField(db_column='H_disp')  # Field name made lowercase.
    q_cs = models.IntegerField(db_column='Q_CS')  # Field name made lowercase.
    ag_tq_fus = models.FloatField(db_column='Ag_Tq_Fus')  # Field name made lowercase.
    bat_tq_fus = models.IntegerField(db_column='Bat_TQ_Fus')  # Field name made lowercase.
    bb_fus = models.FloatField(db_column='BB_Fus')  # Field name made lowercase.
    q_sol = models.IntegerField(db_column='Q_Sol')  # Field name made lowercase.
    hh_prog = models.FloatField(db_column='HH_Prog')  # Field name made lowercase.
    ag_tq_car = models.FloatField(db_column='Ag_Tq_Car')  # Field name made lowercase.
    bat_tq_mis = models.IntegerField(db_column='Bat_TQ_Mis')  # Field name made lowercase.
    bb_mis = models.FloatField(db_column='BB_Mis')  # Field name made lowercase.
    ag_tq_ali = models.FloatField(db_column='Ag_Tq_Ali')  # Field name made lowercase.
    bb_ali = models.FloatField(db_column='BB_Ali')  # Field name made lowercase.
    acc_maq_form = models.FloatField(db_column='Acc_Maq_form')  # Field name made lowercase.
    acc_trans_estoc = models.FloatField(db_column='Acc_trans_Estoc')  # Field name made lowercase.
    q_mf_real = models.FloatField(db_column='Q_MF_real')  # Field name made lowercase.
    aprov_qual = models.FloatField(db_column='Aprov_qual')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Valores'

