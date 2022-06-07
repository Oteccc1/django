from django.db import models
class BlockCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'

class MastersCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'

class UslugiCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'

class Uslugi(models.Model):
    category = models.ForeignKey(
        UslugiCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Услуга',
        max_length=128
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True
    )

    short_desc = models.CharField(
        verbose_name='Описание услуги',
        max_length=60,
        blank=True,
    )
    dop = models.CharField(
        verbose_name='доп услуга',
        max_length=128,
        blank=True,
    )
    price = models.DecimalField(verbose_name='цена',
                                max_digits=8,
                                decimal_places=2,
                                default=8
                                )
    def __str__(self):
        return f'{self.name} ({self.category})'
class Block(models.Model):
    category = models.ForeignKey(
        BlockCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Услуга',
        max_length=128
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True
    )

    short_desc = models.CharField(
        verbose_name='Описание',
        max_length=60,
        blank=True,
    )

    def __str__(self):
        return f'{self.name} ({self.category})'

class Masters(models.Model):
    category = models.ForeignKey(
        MastersCategory,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Имя мастера',
        max_length=128
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True
    )

    short_desc = models.CharField(
        verbose_name='Специальность',
        max_length=60,
        blank=True,
    )

    def __str__(self):
        return f'{self.name} ({self.category})'