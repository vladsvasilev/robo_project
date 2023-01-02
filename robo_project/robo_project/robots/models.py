from enum import Enum

from django.db import models

from robo_project.robots.mixins.model_mixins import ChoicesEnumMixin


class Types(ChoicesEnumMixin, Enum):
    home = "Home"
    software = "Software"
    industrial = "Industrial"


class RobotTypes(models.Model):
    MAX_LENGTH_TYPE = 25

    name = models.CharField(
        max_length=Types.max_len(),

    )

    description = models.CharField(
        max_length= 250,
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.name

class AppRobots(models.Model):
    MAX_LENGTH_NAME = 15

    robot_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )

    available_quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL',
    )
    # TODO to replace the URLField with ImageField if needed

    type = models.ForeignKey(
        RobotTypes,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.robot_name

