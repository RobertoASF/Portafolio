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
    user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)
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


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
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


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigIntegerField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


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
    id_prod = models.IntegerField(primary_key=True)
    report_date = models.DateField()
    user_reported = models.CharField(max_length=255)
    user_accuser = models.CharField(max_length=255)
    report_description = models.CharField(max_length=255)
    report_action = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'indictment'


class Match(models.Model):
    prod_seller = models.OneToOneField('User', models.DO_NOTHING, db_column='prod_seller')
    match_date = models.DateField()
    user_liked = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'match'


class Product(models.Model):
    prod = models.ForeignKey(Indictment, models.DO_NOTHING, primary_key=True)
    prod_name = models.CharField(max_length=255)
    prod_new = models.BooleanField()
    permuta = models.BooleanField()
    prod_price = models.IntegerField()
    prod_date = models.DateField()
    prod_score = models.IntegerField(blank=True, null=True)
    prod_seller = models.ForeignKey('User', models.DO_NOTHING, db_column='prod_seller')
    prod_reported = models.BooleanField(null=True)
    prod_active = models.BooleanField()
    prod_description = models.CharField(max_length=255)
    prod_affinitie1 = models.IntegerField()
    prod_affinitie2 = models.IntegerField(blank=True, null=True)
    prod_photo1 = models.CharField(max_length=255)
    prod_photo2 = models.CharField(max_length=255)
    prod_photo3 = models.CharField(max_length=255, blank=True, null=True)
    prod_photo4 = models.CharField(max_length=255, blank=True, null=True)
    prod_photo5 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'


class ProductCategory(models.Model):
    product = models.ForeignKey(Category, models.DO_NOTHING, db_column='product')
    category = models.ForeignKey(Product, models.DO_NOTHING, db_column='category')

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
