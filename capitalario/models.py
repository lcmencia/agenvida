from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse


# Create your models here.

class Purpose(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    meta = models.PositiveIntegerField(default=0)
    fecha_inicio = models.DateField(null=True)
    fecha_fin = models.DateField(null=True)
    creado = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(editable=False)
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='purpose_contribute')

    def __str__(self):
        return self.nombre
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nombre)
        super(Purpose, self).save(*args, **kwargs)
    def get_absolute_url(self):
        #return "detail/%s/" %(self.id)
        return reverse("detail", kwargs={"id": self.id})
      
    def get_contribute_url(self):
        return reverse("contribute-toggle", kwargs={"id": self.id})