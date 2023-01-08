from django.db import models

from utils.models import AbstractUUID, AbstractTimeTracker

class Car(AbstractUUID, AbstractTimeTracker):

    model = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        # related_name='model',
        verbose_name='Көлік'
    )
    number = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        verbose_name='Нөмірі',
        # related_name='cars',
    )

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
        ordering = ('uuid',)

    def __str__(self):
        return str(self.model)