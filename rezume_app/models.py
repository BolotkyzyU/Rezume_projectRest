from django.db import models



# Create your models here.
class Applications(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    email = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Заявки'
        verbose_name_plural = 'Заявки'


class Projects(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'


class Education(models.Model):
    qualification = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'

class Experience(models.Model):
    position = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = 'Опыт'
        verbose_name_plural = 'Опыт'

class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'

class BlogDetails(models.Model):
    blogObject = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    user = models.CharField(max_length=255)
    blogObject = models.ForeignKey(Blog, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)