from django.db import models
# coding: utf-8

class Ergonomic_criteria(models.Model):
    criterion = models.CharField('Criério', max_length=100)
    description = models.TextField('Descrição',)
    
    class Meta:
        verbose_name = u'Critério ergonômico'
        verbose_name_plural = u'Critérios ergonômicos'
    
    def __unicode__(self):
        return self.criterion

class Type(models.Model):
    TYPE_CHOICES = (
        ('SN', "Sim ou Não"),
        ( 'GRD', "Graduada"),
    )
    
    type = models.CharField(max_length=255, choices = TYPE_CHOICES)
    
    def __unicode__(self):
        return self.type

class Value_of_type(models.Model):
    VALUE_CHOICES = (
        ('s', 'Sim'),
        ('n','Não'),
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
	
    value = models.CharField( max_length=255, choices = VALUE_CHOICES)

    def __unicode__(self):
        return self.value

class Element_of_interaction(models.Model):
    name = models.CharField('Nome', max_length=100)
    
    def __unicode__(self):
        return self.name
    	
    class Meta:
        verbose_name = u'Elemento de interação'
        verbose_name_plural = u'Elementos de interação'

class Question(models.Model):
    ergonomic_criterion = models.ForeignKey(Ergonomic_criteria)
    enunciation = models.CharField('Enumciado', max_length=200)
    description = models.TextField('Descrição',)
    type = models.ForeignKey(Type)
    value = models.ForeignKey(Value_of_type)
    interaction_elements_associated = models.ManyToManyField(Element_of_interaction)
    
    def __unicode__(self):
        return self.enunciation
    
    class Meta:
        verbose_name = u'Questão'
        verbose_name_plural = u'Questões'
