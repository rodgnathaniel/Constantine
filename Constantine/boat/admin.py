from django.contrib import admin

from .models import Title
from .models import Game
from .models import Mode

admin.site.register(Title)
admin.site.register(Game)
admin.site.register(Mode)
