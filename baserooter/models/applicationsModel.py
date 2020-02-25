from django.db import models
from django.utils import timezone
from baserooter.models import Program

class Application(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    program = models.ForeignKey(Program,related_name ='program',blank=True,
                            null=True,on_delete=models.CASCADE )     
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        output = self.name + '({})'.format(self.id)
        return output
    class Meta:
        db_table = 'application'
        indexes = [
            models.Index(fields=['id', 'name','program'])
        ]