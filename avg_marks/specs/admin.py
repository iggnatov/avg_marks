from django.contrib import admin

from avgs.models import Application
from specs.models import Spec

admin.site.register(Spec)
admin.site.register(Application)

