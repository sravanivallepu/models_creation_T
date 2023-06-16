from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()

class Department(models.Model):
    dname=models.CharField(max_length=100)
    count_of_employees=models.IntegerField()

    def __str__(self):
        return self.dname

class Employee(models.Model):
    ename=models.CharField(max_length=100)
    dname=models.ForeignKey(Department,on_delete=models.CASCADE)
    job=models.CharField(max_length=100)
    empno=models.IntegerField()
    hiredate=models.DateField()
    loc=models.CharField(max_length=100)

    def __str__(self):
        return self.ename
    def __str__(self):
        return self.job
    def __str__(self):
        return self.loc

    