from django.contrib import admin
from ergocoin.models import Question, Ergonomic_criteria, Element_of_interaction

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('ergonomic_criterion', 'enunciation', 'type')
    list_filter = ['interaction_elements_associated', 'ergonomic_criterion']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Element_of_interaction)

admin.site.register(Ergonomic_criteria)
