from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models import User


class ChatType(models.IntegerChoices):
    DIRECT = 1, _("Direct")
    GROUP = 2, _("Group")
    CHANNEL = 3, _("Channel")


class Chat(models.Model):
    name = models.CharField(_("Chat Name"), max_length=64, blank=False, null=False)
    chat_type = models.IntegerField(
        _("Chat Type"), choices=ChatType.choices, blank=False, null=False
    )
    creation_time = models.DateTimeField(_("Chat Creation Time"), auto_now_add=True)
    participants = models.ManyToManyField(
        User, through="Participant", related_name="chats"
    )


class ParticipantRole(models.IntegerChoices):
    ADMIN = 1, _("Admin")
    MODERATOR = 2, _("Moderator")
    MEMBER = 3, _("Member")


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=False, null=False)
    role = models.IntegerField(
        _("Participant Role"),
        choices=ParticipantRole.choices,
        default=ParticipantRole.MEMBER,
    )

    class Meta:
        unique_together = ("user", "chat")


class File(models.Model):
    uploader = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False
    )

    file = models.FileField(blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, blank=False, null=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    message = models.TextField(_("Message"), blank=False, null=False)
    attachments = models.ManyToManyField(
        File, through="Attachment", related_name="chats"
    )


class Attachment(models.Model):
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, blank=False, null=False
    )
    file = models.ForeignKey(File, on_delete=models.CASCADE, blank=False, null=False)
