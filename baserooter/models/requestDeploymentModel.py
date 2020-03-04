from django.db import models
from django.utils import timezone
from baserooter.models import programVersion

class deploymentRequest(models.Model):    
    id = models.AutoField(primary_key=True)
    program_version = models.ForeignKey(programVersion,on_delete=models.CASCADE, related_name='program_version',blank=True,null=True)
    requested_branch = models.CharField(max_length=2000)    
    requested_by = models.CharField(max_length=100)  
    description = models.CharField(max_length=1000)
    technician_id = models.IntegerField()
    status = models.CharField(max_length=100) 
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):        
        return str(self.id)
    
    class Meta:
        db_table = 'deployment_request'
        indexes = [
            models.Index(fields=['id', 'program_version','requested_branch',
            'requested_by','description','technician_id','status'])
        ]
    