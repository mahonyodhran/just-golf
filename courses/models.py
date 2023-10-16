from django.db import models


TEE_CHOICES = [
    ("Blue", "White."),
    ("Green", "Red."),
]

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    eircode = models.CharField(max_length=7)

    class Meta:
        db_table = "course"
    
    def __str__(self):
        return self.name
    
class Tee (models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    colour = models.CharField(choices=TEE_CHOICES, max_length=5)
    slope = models.IntegerField()
    par = models.IntegerField()
    yards = models.IntegerField()

    class Meta:
        db_table = "tee"
    