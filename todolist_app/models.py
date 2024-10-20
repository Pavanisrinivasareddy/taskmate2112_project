from django.db import models # type: ignore
from django.contrib.auth.models import User
# create your model
class TaskList(models.Model):
    
    manage=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    task=models.CharField(max_length=300)
    done=models.BooleanField(default=False)
    
    class Meta:
        ordering=['id']
    
    def __str__(self):
        return self.task + "-"+ str(self.done)