from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

	# The dunder str gives a more descriptive output
	def __str__(self): 	
		return f'{self.user.username} Profile'

	#To resize the image though the save method exist in the parent class, we'll create ours.
	#In order to override the default save, you'll have to use *args & *kwargs	
	def save(self, *args, **kwargs):
		super(Profile, self).save(*args, **kwargs)

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

			