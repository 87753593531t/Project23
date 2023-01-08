from django.db import models

from utils.models import AbstractUUID, AbstractTimeTracker


class Name(AbstractUUID, AbstractTimeTracker):

    name = models.CharField(
        max_length=100,
        verbose_name='Есімі'
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name='Ата-тегі'
    )
    cars = models.ForeignKey(
        'people.Car',
        on_delete=models.CASCADE,
        verbose_name='Көліктер',
        related_name='names'
    )
    city = models.ForeignKey(
        'people.City',
        on_delete=models.CASCADE,
        verbose_name='Қалалар',
        related_name='names'
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Name'
        verbose_name_plural = 'Names'
        ordering = ('uuid',)