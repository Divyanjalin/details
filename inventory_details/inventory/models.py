from django.db import models


# Create your models here.
class Std(models.Model):
    age=models.IntegerField()
    name=models.CharField(max_length=100)
    school=models.CharField(max_length=100)

class Meta:
        abstract=True

def __str__(self):
        return'age:{0} name:{1}'.format(self.age,self.name)


class One(Std):
    pass


class Two(Std):
    pass