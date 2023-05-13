# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    comuna = models.ForeignKey('Comuna', models.DO_NOTHING)
    cod_postal = models.CharField(max_length=255, blank=True, null=True)
    casa_o_dep = models.IntegerField()
    calle = models.CharField(max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING, primary_key=True)
    numero = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'


class Admin(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=255)
    admin_name1 = models.CharField(max_length=255)
    admin_name2 = models.CharField(max_length=255, blank=True, null=True)
    admin_surname1 = models.CharField(max_length=255)
    admin_surname2 = models.CharField(max_length=255, blank=True, null=True)
    admin_email = models.CharField(max_length=255)
    admin_date_hire = models.DateField()
    admin_status = models.BooleanField()
    is_super_admin = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'admin'


class Affinity(models.Model):
    af_id = models.IntegerField(primary_key=True)
    af_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'affinity'


class AppScore(models.Model):
    app_score_id = models.CharField(primary_key=True, max_length=255)
    user = models.ForeignKey('User', models.DO_NOTHING)
    as_date = models.DateField()
    as_q1 = models.IntegerField()
    as_q2 = models.IntegerField()
    as_q3 = models.IntegerField()
    as_q4 = models.IntegerField()
    as_q5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_score'


class Category(models.Model):
    cat_id = models.CharField(primary_key=True, max_length=255)
    cat_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'category'


class Comuna(models.Model):
    comuna_id = models.IntegerField(primary_key=True)
    provincia = models.ForeignKey('Provincia', models.DO_NOTHING)
    comuna_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'comuna'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Historical(models.Model):
    hist_id = models.IntegerField(primary_key=True)
    date = models.DateField()
    buyer_id = models.CharField(max_length=255)
    prod = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'historical'


class Indictment(models.Model):
    id_prod_indct = models.IntegerField(primary_key=True)
    report_date = models.DateField()
    user_reported = models.CharField(max_length=255)
    user_accuser = models.CharField(max_length=255)
    report_description = models.CharField(max_length=255)
    report_action = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'indictment'


class Match(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, primary_key=True)
    match_date = models.DateField()
    user_liked = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'match'


class Product(models.Model):
    prod_id = models.CharField(primary_key=True, max_length=255)
    prod_name = models.CharField(max_length=255)
    prod_new = models.BooleanField()
    permuta = models.BooleanField()
    prod_price = models.IntegerField()
    prod_date = models.DateField()
    prod_score = models.IntegerField(blank=True, null=True)
    prod_seller = models.ForeignKey('User', models.DO_NOTHING, db_column='prod_seller')
    prod_reported = models.NullBooleanField()
    prod_active = models.BooleanField()
    prod_description = models.CharField(max_length=255)
    prod_affinitie1 = models.IntegerField()
    prod_affinitie2 = models.IntegerField(blank=True, null=True)
    prod_photo1 = models.CharField(max_length=255)
    prod_photo2 = models.CharField(max_length=255)
    prod_photo3 = models.CharField(max_length=255, blank=True, null=True)
    prod_photo4 = models.CharField(max_length=255, blank=True, null=True)
    prod_photo5 = models.CharField(max_length=255, blank=True, null=True)
    id_prod_indct = models.ForeignKey(Indictment, models.DO_NOTHING, db_column='id_prod_indct', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, models.DO_NOTHING, db_column='product')
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='category')

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductScore(models.Model):
    score_id = models.IntegerField(primary_key=True)
    user_reviewer = models.CharField(max_length=255)
    product_reviewed = models.ForeignKey(Product, models.DO_NOTHING, db_column='product_reviewed')
    score_date = models.DateField()
    score_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_score'


class Provincia(models.Model):
    provincia_id = models.IntegerField(primary_key=True)
    region = models.ForeignKey('Region', models.DO_NOTHING)
    provincia_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'provincia'


class Region(models.Model):
    region_id = models.IntegerField(primary_key=True)
    region_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'region'


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=255)
    user_name1 = models.CharField(max_length=255)
    user_name2 = models.CharField(max_length=255, blank=True, null=True)
    user_surname1 = models.CharField(max_length=255)
    user_surname2 = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)
    user_last_loc_lat = models.FloatField(blank=True, null=True)
    user_last_loc_long = models.FloatField(blank=True, null=True)
    user_date_lastloc = models.DateField(blank=True, null=True)
    date_registred = models.DateField()
    date_last_login = models.DateField()
    user_score = models.IntegerField()
    user_phone = models.IntegerField()
    user_active = models.BooleanField()
    user_inetrest1 = models.IntegerField()
    user_interest2 = models.IntegerField()
    user_photo = models.CharField(max_length=255)
    user_sells = models.IntegerField()
    user_is_premium = models.BooleanField()
    user_premium_start = models.DateField(blank=True, null=True)
    user_premium_ends = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserScore(models.Model):
    score_id = models.IntegerField(primary_key=True)
    user_reviwer = models.ForeignKey(User, models.DO_NOTHING, db_column='user_reviwer', blank=True, null=True)
    user_reviwed = models.CharField(max_length=255)
    score_date = models.DateField()
    score_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_score'

class Comment(models.Model):
    id_comment = models.CharField(primary_key=True, max_length=255)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'comment'
