from django.db import models
import datetime as dt
import cloudinary
from cloudinary.models import CloudinaryField


# Create your models here.
class Image(models.Model):
    image = CloudinaryField(upload_to = 'cloudinary')
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category',default='', on_delete = models.CASCADE)
    imageDescription = models.CharField(max_length=250)
    image_location = models.ForeignKey('Location',default='', on_delete = models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        class method to display images by date posted
        '''
        ordering = ['date_uploaded']

    
    def __str__(self):
        return self.save()


    def upload_image(self,image=None,title=None, category=None, image_location=None, imageDescription=None, date_uploaded=None)
        self.image = image if image else self.image
        self.title = title if title else self.Title
        self.category = category if category else self.category
        self.image_location = image_location if image_location else self.image_location
        self.imageDescription = imageDescription if imageDescription else self.imageDescription
        self.date_uploaded = date_uploaded if date_uploaded else self.date_uploaded 


    def delete_image(self):
        self.delete()

    
    @classmethod
    def search_by_category(cls, search_term):
        '''
        Method to filter images by category
        '''
        result = cls.objects.filter(category__category__icontains=search_term)
        return result 

    