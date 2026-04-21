from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('traveller_type', models.CharField(choices=[('domestic', 'Domestic Traveller'), ('international', 'International Traveller')], default='domestic', max_length=20)),
                ('nationality', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('preferred_budget', models.CharField(blank=True, max_length=20)),
                ('preferred_difficulty', models.CharField(blank=True, max_length=20)),
                ('interests', models.CharField(blank=True, help_text='Comma-separated interests', max_length=500)),
                ('current_province', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
