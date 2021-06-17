#----------------------django imports--------------------
from django.db import models
from django.db.models.deletion import CASCADE

#----------------------django Model imports--------------------
from authorization.models import User

# Create your models here.
class CourseDetails(models.Model):
    '''
    Courses are added in this models. 
    '''
    name = models.CharField(max_length=512)
    author = models.CharField(max_length=512)
    date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class CourseWishlist(models.Model):
    '''
    Courses can be added to the users whishlist and those courses wishlist are saved in this model. 
    '''
    course = models.ForeignKey(CourseDetails, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)

    class Meta:
        unique_together = ('course', 'user')