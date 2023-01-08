from django.db import models


from utils.models import AbstractUUID, AbstractTimeTracker


class City(AbstractUUID, AbstractTimeTracker):

    city = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Қала'
    )
    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='citys'
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Citys'
        ordering = ('uuid',)

    def __str__(self):
        return str(self.city)