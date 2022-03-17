from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField('Firs Name', max_length=50, help_text='first name')
    last_name = models.CharField('Last Name', max_length=50, help_text='last name')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self) -> str:
        return f'{self.pk} - Author: {self.first_name}{self.last_name}'

    def info_autor(self):
        info = print(f'O autor {self.first_name} foi criado em {self.created_at}. Sua última atualização ocorreu dia {self.updated_at}')
        return info

    def info_id(self):
        info = print(f'ID {self.pk} - {self.first_name} {self.last_name}')
    

class Book(models.Model):
    first_name = models.CharField('Firs Name', max_length=50, help_text='first name')
    last_name = models.CharField('Last Name', max_length=50, help_text='last name')
    edition_date = models.DateTimeField()
    authors = models.ManyToManyField('Author', related_name='authors') 
    # O campo "DateTimeField" com o atributo "auto_now_add=True" instância a data na hora da criação do livro
    created_at = models.DateTimeField(auto_now_add=True)
    # O campo "DateTimeField" com o atributo "auto_now=True" instância a data na hora que o objeto é alterado
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self) -> str:
        full_name = self.first_name + self.last_name
        return full_name
        #return f'{self.first_name} {self.last_name}'