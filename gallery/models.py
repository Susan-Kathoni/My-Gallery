from django.db import models

# Create your models here.
class Image(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100)
    category = models.ForeignKey('Category',default='', on_delete = models.CASCADE)
    imageDescription = models.CharField(max_length=250)
    image_location = models.ForeignKey('Location',default='', on_delete = models.CASCADE)
    date_uploaded = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.save()

    def delete_image(self):
        self.delete()

    