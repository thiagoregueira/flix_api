import unicodedata
from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('CANADA', 'Canadá'),
    ('FRANCE', 'França'),
    ('GERMANY', 'Alemanha'),
    ('ITALY', 'Itália'),
    ('SPAIN', 'Espanha'),
    ('AUSTRALIA', 'Austrália'),
    ('CHINA', 'China'),
    ('INDIA', 'Índia'),
    ('JAPAN', 'Japão'),
    ('ARGENTINA', 'Argentina'),
    ('MEXICO', 'México'),
    ('UK', 'Reino Unido'),
    ('AUSTRIA', 'Áustria'),
    ('BELGIUM', 'Bélgica'),
    ('CZECH_REPUBLIC', 'República Tcheca'),
    ('DENMARK', 'Dinamarca'),
)

# colocar em ordem alfabética(Levando em conta os acentos da língua portuguesa)


def normalize_for_sorting(text):
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII').lower()


# colocar em ordem alfabética(Levando em conta os acentos da língua portuguesa)
NATIONALITY_CHOICES = sorted(NATIONALITY_CHOICES, key=lambda x: normalize_for_sorting(x[1]))


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(choices=NATIONALITY_CHOICES, max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
