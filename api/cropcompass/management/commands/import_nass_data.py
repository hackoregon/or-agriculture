from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import FieldDoesNotExist

from cropcompass import models

import pandas as pd


FIELD_NAME_EXCEPTIONS = {
        'CV_%': 'cv_percent',
}



class Command(BaseCommand):
    help = "Imports NASS data from a CSV file"


    def add_arguments(self, parser):
        parser.add_argument('csv_path', nargs=1, type=unicode,
                help="Filepath or URL to CSV")


    def handle(self, *args, **options):
        uri = options['csv_path'][0]

        df = pd.read_csv(uri, low_memory=False).fillna("")
        saved_entries = []
        skipped_entries = []

        self.stdout.write("Attempting to add %i entries to database." % len(df))
        self.stdout.write("")

        for index, row in df.iterrows():
            entry = models.RawNassData()
            filter_args = {}

            for col in df.columns:
                value = row[col] or None
                field_name, field = self.get_field_for(col)
                filter_args[field_name] = value
                setattr(entry, field_name, value)

            existing = models.RawNassData.objects.filter(**filter_args).first()
            if existing:
                self.stderr.write(
                        "Skipping duplicate entry: %s" % existing)
                skipped_entries.append(entry)
            else:
                entry.save()
                self.stdout.write("Saved entry: %s" % entry) 
                saved_entries.append(entry)

                # @TODO failed_entries on validation errors

        self.stdout.write("")
        self.stdout.write("Added %i new entries. Skipped %i duplicates." % (
            len(saved_entries), len(skipped_entries)))

        # raise CommandError("Could not import CSV")


    def get_field_for(self, col_name):
        ''' 
        Translate original column name from NASS into 
        the field name on our model.
        '''

        field_name = FIELD_NAME_EXCEPTIONS.get(col_name)

        if not field_name:
            # All our field names are just lower case versions of NASS fields
            # if it gets more complex, use the `normalize_col_name`
            # function from django/core/management/commands/inspectdb.py 
            field_name = col_name.lower()

        try:
            field = models.RawNassData._meta.get_field(field_name)
            return field_name, field
        except FieldDoesNotExist:
            raise CommandError( 
                    "NASS model does not have an equivalent "
                    "field for '%s'. Searched for '%s'" % (
                            col_name, field_name))
