from django.db import models

class Flash(models.Model):
    description = models.CharField(max_length=50)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.description} in {self.color}'
    

class Artist(models.Model):
  instagram = models.CharField(max_length=50, default='off the grid')
  name = models.CharField(max_length=25)
  position = models.CharField(max_length=20)
  experience = models.IntegerField()
  flash = models.ManyToManyField(Flash)

  def __str__(self):
    return self.name

TATS = (
    ('F', 'Flash'),
    ('N', 'Custom'),
    ('C', 'Cover Up'),
)
  
class Tats(models.Model):
    date = models.DateField('Date')
    tat = models.CharField(
        max_length=1,
        choices=TATS,
        default=TATS[0][0]
        )
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_tat_display()} on {self.date}"