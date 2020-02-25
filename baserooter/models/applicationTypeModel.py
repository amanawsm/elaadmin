from django.db import models
from django.utils import timezone

class applicationType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        output = self.name + '({})'.format(self.id)
        return output
    class Meta:
        db_table = 'application_type'
        indexes = [
            models.Index(fields=['id', 'name'])
        ]