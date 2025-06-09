from django.db import models

# Create your models here.

# table creation named reg for registration
class reg(models.Model):
    reg_mail=models.EmailField(max_length=20)
    reg_pass=models.CharField(max_length=12)

    def __str__(self):
        return self.reg_mail
    
# table creation named task for storing the task details
class task(models.Model):
    id_user=models.ForeignKey(reg,on_delete=models.CASCADE)
    task_data=models.CharField(max_length=20)
    description_data=models.CharField(max_length=50)
    date_data=models.DateField()

    def _str_(self):
        return self.id_user
    
