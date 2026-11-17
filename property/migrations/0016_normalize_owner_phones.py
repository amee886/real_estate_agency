import phonenumbers
from django.db import migrations


def normalize_phones(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.all():
        phone = flat.owners_phonenumber

        try:
            parsed = phonenumbers.parse(phone, 'RU')

            if phonenumbers.is_valid_number(parsed):
                flat.owner_pure_phone = parsed
            else:
                flat.owner_pure_phone = None

        except phonenumbers.NumberParseException:
            flat.owner_pure_phone = None

        flat.save(update_fields=['owner_pure_phone'])


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0015_flat_owners_phonenumber'),
    ]

    operations = [
        migrations.RunPython(normalize_phones),
    ]
