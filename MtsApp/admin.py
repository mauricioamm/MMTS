from django.contrib import admin


from .models import ProcedCond1Model, ProcedCond2Model,\
                    TodosOsBlocos, BlocoSaidaModel, ParticipanteModel

admin.site.register(TodosOsBlocos)
admin.site.register(BlocoSaidaModel)
admin.site.register(ParticipanteModel)
admin.site.register(ProcedCond1Model)
admin.site.register(ProcedCond2Model)

