from django.db import models


TEE_CHOICES = [
    ("Blue", "Blue"),
    ("White", "White"),
    ("Green", "Green"),
    ("Red", "Red"),
]


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    eircode = models.CharField(max_length=7)

    class Meta:
        db_table = "course"

    def __str__(self):
        return self.name


class Tee(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    colour = models.CharField(choices=TEE_CHOICES, max_length=10)
    slope = models.IntegerField()
    par = models.IntegerField()
    yards = models.IntegerField()

    objects = models.Manager()

    def is_colour_available(self):
        existing_colours = Tee.objects.filter(course=self.course).values_list(
            "colour", flat=True
        )
        return self.colour not in existing_colours

    class Meta:
        db_table = "tee"

    def __str__(self):
        return self.colour
