from django.shortcuts import render
from .models import TableStatus

def db_status_view(request):
    context = TableStatus.objects.all()

    data = [{
        "database_name": i.database_name,
        "table_name": i.table_name,
        "loaded_date": i.loaded_date,
        "record_count": i.record_count
    } for i in context]

    return render(request, "home.html", {'data':data})
