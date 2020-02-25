from django.db import models
from django.utils import timezone
from baserooter.models import Application,Environment

class programVersion(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    application = models.ForeignKey(Application,related_name ='application',
                    on_delete=models.CASCADE )
    branch = models.CharField(max_length=100, blank=True, null=True)
    updated_by = models.CharField(max_length=100, blank=True, null=True)   
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        output = self.name + '({})'.format(self.id)
        return output
    class Meta:
        db_table = 'program_version'
        indexes = [
            models.Index(fields=['id', 'name','branch','updated_by','application'])
        ]