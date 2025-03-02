from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


from key.models import KeyType, KeyToolType


class UserType(models.IntegerChoices):
    USER = 1, _("User")
    BOT = 2, _("Bot")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'UserType<{self.name}>'


class User(models.Model):
    username = models.CharField(
        _("Username"), max_length=32, unique=True, blank=False, null=False
    )
    password = models.CharField(_("Password"), max_length=256, blank=False, null=False)
    description = models.TextField(_("Description"), blank=True, null=False, default="")
    user_type = models.IntegerField(
        _("User Type"),
        choices=UserType.choices,
        default=UserType.USER,
        blank=False,
        null=False,
    )
    creation_time = models.DateTimeField(_("Creation Time"), auto_now_add=True)

    def set_password(self, password: str) -> None:
        self.password = settings.PASSWORD_HASHER.hash(password)

    def verify_password(self, password: str) -> bool:
        return settings.PASSWORD_HASHER.verify(self.password, password)

    def __str__(self) -> str:
        return f'{self.username}'

    def __repr__(self) -> str:
        return f'User<{self.pk}, {self.username}, {UserType(self.user_type)!r}>'


class Key(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    key_type = models.IntegerField(
        _("Key Type"),
        choices=KeyType.choices,
        default=KeyType.PUBLIC,
        blank=False,
        null=False,
    )
    tool_type = models.IntegerField(
        _("Tool Type"),
        choices=KeyToolType.choices,
        default=KeyToolType.GPG,
        blank=False,
        null=False,
    )
    key = models.TextField(blank=False, null=False)
    creation_time = models.DateTimeField(_("Creation Time"), auto_now_add=True)
