from django.db import models

# Create your models here.
class TableStatus(models.Model):
    table_name = models.CharField(max_length=100, primary_key=True)
    database_name = models.CharField(max_length=100)
    loaded_date = models.DateField()
    record_count = models.IntegerField()

    class Meta:
        db_table = 'claims_table_details'
        managed = False

    def __str__(self):
        return f'{self.table_name} - {self.database_name} - {self.loaded_date} - {self.record_count} - {self.database_name}'