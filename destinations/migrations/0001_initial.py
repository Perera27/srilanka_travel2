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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('category_type', models.CharField(choices=[('beach', 'Beach & Coastal'), ('wildlife', 'Wildlife & Nature'), ('cultural', 'Cultural & Heritage'), ('religious', 'Religious & Spiritual'), ('adventure', 'Adventure & Trekking'), ('historical', 'Historical Sites'), ('scenic', 'Scenic & Viewpoints'), ('waterfalls', 'Waterfalls'), ('food', 'Food & Cuisine')], default='cultural', max_length=50)),
                ('icon', models.CharField(default='🏛️', max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('short_description', models.CharField(max_length=300)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='destinations/')),
                ('budget_level', models.CharField(choices=[('free', 'Free'), ('budget', 'Budget (< LKR 500)'), ('moderate', 'Moderate (LKR 500–2000)'), ('premium', 'Premium (LKR 2000+)')], default='moderate', max_length=20)),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('challenging', 'Challenging')], default='easy', max_length=20)),
                ('best_time_to_visit', models.CharField(blank=True, max_length=200)),
                ('opening_hours', models.CharField(blank=True, max_length=200)),
                ('entry_fee', models.CharField(blank=True, max_length=100)),
                ('requires_dress_code', models.BooleanField(default=False)),
                ('dress_code_description', models.TextField(blank=True)),
                ('is_hidden_gem', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('safety_notes', models.TextField(blank=True)),
                ('tags', models.CharField(blank=True, help_text='Comma-separated tags', max_length=300)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destinations', to='destinations.category')),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destinations', to='destinations.province')),
            ],
            options={
                'ordering': ['-is_featured', '-view_count', 'name'],
            },
        ),
        migrations.CreateModel(
            name='DestinationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='destinations/gallery/')),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='destinations.destination')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='FavouriteDestination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourited_by', to='destinations.destination')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-added_at'],
                'unique_together': {('user', 'destination')},
            },
        ),
    ]
