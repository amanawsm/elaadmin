from django.db import models
from baserooter.models import applicationType,Environment
from django.utils import timezone

class applicationHeader(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    environment = models.ForeignKey(Environment,on_delete=models.CASCADE,related_name='env',blank=True,null=True) 
    application_type = models.ForeignKey(applicationType,on_delete=models.CASCADE,related_name='app_type',blank=True,null=True)     
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        output = self.name + '({})'.format(self.id)
        return output
    class Meta:
        db_table = 'application_header'
        indexes = [
            models.Index(fields=['id', 'name'])
        ]