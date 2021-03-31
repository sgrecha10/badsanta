# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Catalog(models.Model):
    id0 = models.PositiveIntegerField(primary_key=True)
    id1 = models.PositiveIntegerField()
    type = models.PositiveIntegerField(verbose_name='Тип ГОСТа')
    gtype = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    num = models.CharField(max_length=128)
    snum = models.PositiveBigIntegerField(blank=True, null=True)
    namer = models.TextField(blank=True, null=True)
    namee = models.TextField(blank=True, null=True)
    obl = models.TextField(blank=True, null=True)
    date0 = models.DateField()
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField()
    dates = models.TextField(blank=True, null=True)
    rel = models.TextField(blank=True, null=True)
    okp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog'
        unique_together = (('type', 'id0'), ('type', 'snum', 'id0'),)


class Catalog1(models.Model):
    id0 = models.AutoField(primary_key=True)
    id1 = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    num = models.TextField(blank=True, null=True)
    snum = models.PositiveBigIntegerField()
    catid = models.TextField(blank=True, null=True)
    namer = models.TextField(blank=True, null=True)
    obl = models.TextField(blank=True, null=True)
    ogl = models.TextField(blank=True, null=True)
    norm = models.TextField(blank=True, null=True)
    words = models.TextField(blank=True, null=True)
    pack = models.TextField(blank=True, null=True)
    date0 = models.DateField(blank=True, null=True)
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog1'
        unique_together = (('snum', 'id0'),)


class Catalog2(models.Model):
    part = models.PositiveIntegerField()
    id0 = models.PositiveIntegerField()
    pkey = models.PositiveBigIntegerField(unique=True, primary_key=True)
    id1 = models.PositiveIntegerField()
    # type = models.PositiveSmallIntegerField()
    type = models.ForeignKey('mycat.Types2', on_delete=models.CASCADE)


    status = models.PositiveSmallIntegerField()
    stype = models.PositiveIntegerField()
    numru = models.TextField(blank=True, null=True)
    numen = models.TextField(blank=True, null=True)
    snum = models.PositiveBigIntegerField(blank=True, null=True)
    nameru = models.TextField(blank=True, null=True)
    nameen = models.TextField(blank=True, null=True)
    obl = models.TextField(blank=True, null=True)
    ogl = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    pub = models.TextField(blank=True, null=True)
    html = models.PositiveIntegerField()
    gif = models.PositiveIntegerField()
    pages = models.PositiveSmallIntegerField()
    date0 = models.DateField()
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    date3 = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog2'
        unique_together = (('snum', 'part', 'id0'), ('part', 'id0'), ('type', 'part', 'id0'),)


class Catmenu2(models.Model):
    base = models.PositiveIntegerField(primary_key=True)
    id0 = models.PositiveIntegerField()
    id1 = models.PositiveIntegerField()
    sub = models.PositiveIntegerField()
    nameru = models.TextField()
    nameen = models.TextField(blank=True, null=True)
    comru = models.TextField(blank=True, null=True)
    comen = models.TextField(blank=True, null=True)
    sort = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'catmenu2'
        unique_together = (('base', 'id0'),)


class Changes(models.Model):
    id0 = models.PositiveIntegerField(primary_key=True)
    id1 = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    date1 = models.DateField(blank=True, null=True)
    date2 = models.DateField(blank=True, null=True)
    numr = models.CharField(max_length=128)
    reg = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'changes'


class Designers(models.Model):
    id0 = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()
    addr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designers'


class Doccat(models.Model):
    id0 = models.PositiveIntegerField()
    idcat = models.PositiveIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'doccat'
        unique_together = (('id0', 'idcat'), ('idcat', 'id0'),)


class Doccat1(models.Model):
    id0 = models.PositiveIntegerField()
    idcat = models.PositiveIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'doccat1'
        unique_together = (('idcat', 'id0'), ('id0', 'idcat'),)


class Doccat2(models.Model):
    part = models.PositiveIntegerField()
    id0 = models.PositiveIntegerField()
    idcat = models.PositiveIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'doccat2'
        unique_together = (('part', 'id0', 'idcat'), ('idcat', 'part', 'id0'),)


class Doclink2(models.Model):
    part0 = models.PositiveIntegerField()
    id0 = models.PositiveIntegerField()
    part1 = models.PositiveIntegerField()
    id1 = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'doclink2'


class Docrel2(models.Model):
    typerel = models.PositiveIntegerField()
    part0 = models.PositiveIntegerField()
    id0 = models.PositiveIntegerField()
    part1 = models.PositiveIntegerField()
    id1 = models.PositiveIntegerField()
    num = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docrel2'


class Org2(models.Model):
    typeorg = models.PositiveIntegerField(primary_key=True)
    idorg = models.PositiveIntegerField()
    nameru = models.TextField()
    nameen = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org2'
        unique_together = (('typeorg', 'idorg'),)


class Orgrel2(models.Model):
    part = models.PositiveIntegerField()
    id0 = models.PositiveIntegerField()
    typeorg = models.PositiveIntegerField()
    idorg = models.PositiveIntegerField()
    typerel = models.PositiveIntegerField()
    date = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgrel2'


class Reg(models.Model):
    id0 = models.PositiveIntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'reg'


class Status2(models.Model):
    id0 = models.PositiveSmallIntegerField(primary_key=True)
    type = models.PositiveIntegerField()
    name = models.CharField(max_length=42)
    typename = models.CharField(max_length=18)

    class Meta:
        managed = False
        db_table = 'status2'
        unique_together = (('id0', 'type', 'name'),)


class Types(models.Model):
    id0 = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=43)
    count = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'types'
        unique_together = (('name', 'id0', 'count'),)


class Types2(models.Model):
    id0 = models.PositiveSmallIntegerField(primary_key=True)
    nameru = models.CharField(max_length=64)
    nameen = models.CharField(max_length=64, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    count = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'types2'
        unique_together = (('nameru', 'count', 'id0'),)


class Windex2(models.Model):
    wid = models.PositiveIntegerField()
    part = models.PositiveIntegerField()
    id0 = models.PositiveIntegerField()
    density = models.FloatField()

    class Meta:
        managed = False
        db_table = 'windex2'
        unique_together = (('wid', 'part', 'id0'),)


class Words2(models.Model):
    wid = models.PositiveIntegerField(primary_key=True)
    word = models.CharField(max_length=16)
    count = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'words2'
        unique_together = (('word', 'wid'),)
