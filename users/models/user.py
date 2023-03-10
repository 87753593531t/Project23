from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from utils.models import AbstractUUID, AbstractTimeTracker
from users.managers import CustomUserManager
from utils.const import UserRoleChoice


class CustomUser(AbstractBaseUser, PermissionsMixin, AbstractUUID, AbstractTimeTracker):
    phone = models.CharField(
        max_length=13,
        verbose_name='phone',
        unique=True,
        blank=True,
        null=True
    )

    first_name = models.CharField(
        max_length=50,
        verbose_name='first_name',
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name='last_name',
        blank=True,
        null=True
    )
    avatar = models.ImageField(
        upload_to='uploads/avatars/',
        blank=True,
        null=True
    )
    role = models.CharField(
        max_length=100,
        choices=UserRoleChoice.choice(),
        default=UserRoleChoice.USER.value

    )
    author = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        blank=True,
        null=True

    )
    is_staff = models.BooleanField(
        default=True
    )
    is_active = models.BooleanField(
        default=True
    )

    USERNAME_FIELD = 'phone'

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('uuid',)

    def __str__(self):
        return str(self.uuid)
