from django.contrib import admin
from baserooter.models import (Environment,Program,Application,applicationType,
        Program,programVersion,User,applicationHeader,requestNormal,
        deploymentRequest,Role,chatModel)


# Register your models here.


admin.site.register(Role)
admin.site.register(User)
admin.site.register(Environment)
admin.site.register(Program)
admin.site.register(Application)
admin.site.register(applicationType)
admin.site.register(programVersion)
admin.site.register(applicationHeader)
admin.site.register(deploymentRequest)
admin.site.register(requestNormal)
admin.site.register(chatModel)