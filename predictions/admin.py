from django.contrib import admin
from predictions.models import Prediction
from django.urls import path
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render 

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class AdminPrediction(admin.ModelAdmin):
    list_display=('actual_x','predicted_x','date','team_x','opponent_x','result_x','new_team_x','actual_y','predicted_y','team_y','opponent_y','result_y','new_team_y')
    
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Prediction.objects.update_or_create(
                    actual_x = fields[0],
                    predicted_x = fields[1],
                    date = fields[2],
                    team_x = fields[3],
                    opponent_x = fields[4],
                    result_x = fields[5],
                    new_team_x = fields[6],
                    actual_y = fields[7],
                    predicted_y = fields[8],
                    team_y = fields[9],
                    opponent_y = fields[10],
                    result_y = fields[11],
                    new_team_y = fields[12],



                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)
admin.site.register(Prediction, AdminPrediction)
# Register your models here.
