from django.db import models
from django.utils.translation import gettext_lazy as _


class KeyType(models.IntegerChoices):
    PUBLIC = 1, _("Public")
    PRIVATE = 2, _("Private")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'KeyType<{self.name}>'


class KeyToolType(models.IntegerChoices):
    GPG = 1, _("GPG")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'KeyToolType<{self.name}>'
