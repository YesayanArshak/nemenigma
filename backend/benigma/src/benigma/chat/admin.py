from django.contrib import admin


from chat.models import Chat, Participant, File, Attachment, Message


admin.site.register(Chat)
admin.site.register(Participant)
admin.site.register(File)
admin.site.register(Attachment)
admin.site.register(Message)
