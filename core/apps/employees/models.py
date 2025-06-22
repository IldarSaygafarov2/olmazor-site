from django.db import models

from core.apps.base_app.models import BaseModel


class EmployeeType(BaseModel):
    """
    Model representing a type of employee.
    """

    name = models.CharField(max_length=100, verbose_name="Тип сотрудника")

    class Meta(BaseModel.Meta):
        verbose_name = "Тип сотрудника"
        verbose_name_plural = "Типы сотрудников"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Employee(BaseModel):
    """
    Model representing an employee in the system.
    """

    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Почта")
    position = models.CharField(max_length=255, verbose_name="Должность")
    department = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Место работы",
    )
    nationality = models.CharField(
        max_length=100,
        verbose_name="Национальность",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="employees/images/",
        blank=True,
        null=True,
        verbose_name="Изображение",
    )
    birth_place = models.CharField(
        max_length=255,
        verbose_name="Место рождения",
        blank=True,
        null=True,
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True,
    )
    reception_schedule = models.CharField(
        max_length=255,
        verbose_name="График приема",
        blank=True,
        null=True,
    )
    employee_type = models.ForeignKey(
        EmployeeType,
        on_delete=models.CASCADE,
        related_name="employees",
        verbose_name="Тип сотрудника",
    )

    class Meta(BaseModel.Meta):
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        """
        Returns the full name of the employee.
        """
        return f"{self.first_name} {self.last_name}"
