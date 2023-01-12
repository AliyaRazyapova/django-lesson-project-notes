from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class BaseModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Tag(BaseModel):
	title = models.CharField(max_length=200)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	parent_tag = models.ForeignKey(
		"self",
		on_delete=models.SET_NULL,
		null=True
	)


class Note(BaseModel):
	title = models.CharField(max_length=500)
	text = models.TextField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	alert_send_at = models.DateTimeField(null=True)
	tags = models.ManyToManyField(Tag)
