from django.db import models
from django.utils import timezone
from baserooter.models import programVersion

class requestNormal(models.Model):    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    attachment = models.FileField(upload_to='uploads/',blank=True,null=True)
    status = models.CharField(max_length=100)
    requested_by = models.CharField(max_length=100)   
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        output = str(self.id )
        return output
    class Meta:
        db_table = 'request_normal'
        indexes = [
            models.Index(fields=['id', 'title','description','attachment','status','requested_by'])
        ]