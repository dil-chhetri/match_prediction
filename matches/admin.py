from django.contrib import admin
from matches.models import Match
from django.urls import path
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render 

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class MatchAdmin(admin.ModelAdmin):
    list_display = ('date','time','comp','round','day','venue','gf','ga','opponent','xg','xga','poss','attendance','captain','formation','referee','sh','sot','dist','fk','pickem','pkatt','season','team')

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
                created = Match.objects.update_or_create(
                    date = fields[0],
                    time = fields[1],
                    comp = fields[2],
                    round = fields[3],
                    day = fields[4],
                    venue = fields[5],
                    result = fields[6],
                    gf = fields[7],
                    ga = fields[8],
                    opponent = fields[9],
                    xg = fields[10],
                    xga = fields[11],
                    poss = fields[12],
                    attendance = fields[13],
                    captain = fields[14],
                    formation = fields[15],
                    referee = fields[16],
                    sh = fields[17],
                    sot = fields[18],
                    dist = fields[19],
                    fk = fields[20],
                    pickem = fields[21],
                    pkatt = fields[22],
                    season = fields[23],
                    team = fields[24]


                    )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Match, MatchAdmin)
# Register your models here.
