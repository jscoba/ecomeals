from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Producto(models.Model):

    nombre = models.TextField(_("Nombre"), blank=False)
    ean_code = models.TextField(_("Código de barras"), blank=False, unique=True)
    valor_salud=models.FloatField(_("Porcentaje de salud"))
    valor_energetico = models.FloatField(_("Calorias"))
    foto = models.ImageField(_("Imagen del producto"), upload_to='productos/')
    nutrientes = models.TextField(_("Nutrientes (json)"))
    huella_ecologica = models.TextField(_("Huella (json)"))
    ingredientes = models.TextField(_("Ingredientes (json)"))
    co2_producido = models.FloatField(_("CO2 producido (gramos)"))
    origen = models.TextField(_("Origen del producto"))
    indice_reciclaje = models.FloatField(_("Indice de reciclaje"))

    class Meta:
        verbose_name = _("Producto")
        verbose_name_plural = _("Productos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Producto_detail", kwargs={"pk": self.pk})

class Receta(models.Model):

    nombre = models.TextField(_("Nombre de la receta"))
    tiempo_preparacion = models.IntegerField(_("Tiempo de preparacion (minutos)"))
    tiempo_cocinado = models.IntegerField(_("Tiempo de cocinado (minutos)"))   
    ingredientes = models.TextField(_("Ingredientes (json)"))
    cantidades = models.TextField(_("Cantidades de ingredientes (json)"))
    pasos = models.TextField(_("Pasos a seguir (json)"))
    num_comensales = models.IntegerField(_("Número de comensales"))
    dificultad = models.IntegerField(_("Dificultad (1-5)"))
    foto = models.ImageField(_("Foto de la receta"), upload_to='recetas/')

    class Meta:
        verbose_name = _("Receta")
        verbose_name_plural = _("Recetas")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Receta_detail", kwargs={"pk": self.pk})


class Autor(models.Model):

    nombre = models.TextField(_("Nombre del autor"))
    apellidos = models.TextField(_("Apellido del autor"))
    usuario = models.IntegerField(_("Id del usuario autor"))
    fecha_registro = models.DateField(_("Fecha de registro"), auto_now=True)
    

    class Meta:
        verbose_name = _("Autor")
        verbose_name_plural = _("Autores")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Autor_detail", kwargs={"pk": self.pk})


class Articulo(models.Model):

    autor = models.ForeignKey("Autor", verbose_name=_("Autor del articulo"), on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(_("Fecha de publicacion"), auto_now=True)
    contenido = models.TextField(_("Contenido del artículo (en markdown)"))
    etiquetas = models.TextField(_("Etiquetas del articulo (json)"))

    class Meta:
        verbose_name = _("articulo")
        verbose_name_plural = _("articulos")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("articulo_detail", kwargs={"pk": self.pk})

class Comentario(models.Model):

    tipo_padre = models.TextField(_("Tipo del padre (receta, producto, articulo"))
    nombre_autor = models.TextField(_("Nombre del autor"))
    contenido = models.TextField(_("Contenido del comentario"))
    fecha_publicacion = models.DateTimeField(_("Fecha de publicacion"), auto_now=True)

    class Meta:
        verbose_name = _("comentario")
        verbose_name_plural = _("comentarios")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("comentario_detail", kwargs={"pk": self.pk})
