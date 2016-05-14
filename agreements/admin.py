from django.contrib import admin
from .models import Company, Agreement, Period,  Country


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company', 'country')


class ContryAdmin(admin.ModelAdmin):
    list_display = ('country', 'iso')


class PeriodInline(admin.TabularInline):
    model = Period
    extra = 1


class PeriodAdmin(admin.ModelAdmin):
    list_display = ('choice', 'start_date', 'end_date')


class AgreementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Negotiator', {'fields': [
            'negotiator']}),
        ('Info about company', {'fields': [
         'company', 'credit', 'debet']}),
        ('Start and end agreement', {
         'fields': ['start_agreement', 'end_agreement']})
    ]
    inlines = [PeriodInline]
    list_filter = ['negotiator', 'start_agreement']
    list_display = ('negotiator', 'company',
                    'start_agreement', 'end_agreement')
    search_fields = ['negotiator__username',
                     'company__company', 'company__country__country']
    date_hierarchy = 'start_agreement'

admin.site.register(Company, CompanyAdmin)

admin.site.register(Country, ContryAdmin)

admin.site.register(Period, PeriodAdmin)

admin.site.register(Agreement, AgreementAdmin)
