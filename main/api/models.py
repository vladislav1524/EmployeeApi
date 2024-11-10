from django.db import models


# модель департаментов
class Department(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')

    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]        

    def __str__(self):
        return self.name
    

# модель сотрудников
class Employee(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    photo = models.ImageField(upload_to='employees/%Y/%m/%d', blank=True, verbose_name='Фото')
    position = models.CharField(max_length=70, verbose_name='Должность')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Оклад(₽)')
    age = models.PositiveIntegerField(verbose_name='Возраст')
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE,
                                   verbose_name='Департамент')

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ['last_name']
        indexes = [
            models.Index(fields=['last_name'])
        ]        

    def __str__(self):
        return self.name + self.last_name + self.patronymic
    
