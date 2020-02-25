from django.db import models
from django.utils import timezone
from baserooter.models import Environment, applicationType

class Program(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    server = models.CharField(max_length=100)
    environment = models.ForeignKey(Environment, blank=True, 
                    null=True, related_name = 'environment', 
                    on_delete=models.CASCADE)
    application_type = models.ForeignKey(applicationType, blank=True,
                    null=True, related_name = 'application_type', 
                    on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        output = self.name + '({})'.format(self.id)
        return output
    class Meta:
        db_table = 'program'
        indexes = [
            models.Index(fields=['id', 'name','server','environment','application_type'])
        ]