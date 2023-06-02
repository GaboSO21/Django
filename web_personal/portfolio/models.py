from django.db import models

# Create your models here.

class Project(models.Model):

    # atributo verbose_name para cambiar nombre de idioma o customizar en panel
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # verbose_name: 'proyecto'
        # verbose_name_plural: 'proyectos'
        oredering: ['-created']


    def __str__(self):
        return self.title
