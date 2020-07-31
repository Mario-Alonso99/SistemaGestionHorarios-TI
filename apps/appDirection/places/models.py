from django.db import models

# Create your models here.
PLACE_CHOICES_TIPO = (
    ('Aula', 'Aula'),
    ('Laboratorio', 'Laboratorio'),
)

PLACE_CHOICES_ENCARGADO = (
    ('Julia Gabriela Nieva Paredes', 'Julia Gabriela Nieva Paredes'),
    ('Rosa María Macias Muñoz', 'Rosa María Macias Muñoz'),
    ('José Marin Rugerio Atriano', 'José Marin Rugerio Atriano'),
    ('Blanca Aurelia Jimenez Gomez', 'Blanca Aurelia Jimenez Gomez'),
    ('Sonia López Rodríguez', 'Sonia López Rodríguez'),
    ('Margarita Lima Esteban', 'Margarita Lima Esteban'),
    ('Maricela Gress Roldan', 'Maricela Gress Roldan'), 
    ('Ruth Cervantes Gaspar', 'Ruth Cervantes Gaspar'),
    ('Arcángel Zamora García', 'Arcángel Zamora García'),
    ('Elizabeth Cortes Ramos', 'Elizabeth Cortes Ramos'),
    ('Francisco López Briones', 'Francisco López Briones'),
)

PLACE_CHOICES_UBICACION = (
    ('Edificio P Planta Baja','Edificio P Planta Baja'),
    ('Edificio P Planta Alta','Edificio P Planta Alta'),
    ('Biblioteca','Biblioteca'),
)

class Place(models.Model):
    nombre = models.TextField(max_length=200, verbose_name="Nombre", null=False, blank=False)
    tipo = models.TextField(null=False, blank=False, choices=PLACE_CHOICES_TIPO, default='Aula')
    encargado = models.TextField(null=False, blank=False, choices=PLACE_CHOICES_ENCARGADO, default='Julia Gabriela Nieva Paredes')
    ubicacion = models.TextField(null=False, blank=True, choices=PLACE_CHOICES_UBICACION, default='Edificio P Planta Baja')

    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"
        ordering = ['tipo', 'ubicacion', 'encargado']

    def __str__(self):
        return self.nombre