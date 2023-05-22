# Generated by Django 4.2.1 on 2023-05-21 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buyItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyName', models.CharField(blank=True, max_length=255, null=True)),
                ('buySize', models.CharField(blank=True, max_length=15, null=True)),
                ('buyQuantityMenu', models.PositiveIntegerField(blank=True, null=True)),
                ('buyPrice', models.FloatField(blank=True, null=True)),
                ('buyAddOns1', models.CharField(blank=True, max_length=255, null=True)),
                ('buyAddOns2', models.CharField(blank=True, max_length=255, null=True)),
                ('buyAddOns3', models.CharField(blank=True, max_length=255, null=True)),
                ('buyAddOns4', models.CharField(blank=True, max_length=255, null=True)),
                ('buyAddOns5', models.CharField(blank=True, max_length=255, null=True)),
                ('buyQuantityAO1', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityAO2', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityAO3', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityAO4', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityAO5', models.PositiveIntegerField(blank=True, null=True)),
                ('menuAOPrice1', models.FloatField(blank=True, default=0, null=True)),
                ('menuAOPrice2', models.FloatField(blank=True, default=0, null=True)),
                ('menuAOPrice3', models.FloatField(blank=True, default=0, null=True)),
                ('menuAOPrice4', models.FloatField(blank=True, default=0, null=True)),
                ('menuAOPrice5', models.FloatField(blank=True, default=0, null=True)),
                ('buyingredient1', models.CharField(blank=True, max_length=255, null=True)),
                ('buyingredient2', models.CharField(blank=True, max_length=255, null=True)),
                ('buyingredient3', models.CharField(blank=True, max_length=255, null=True)),
                ('buyingredient4', models.CharField(blank=True, max_length=255, null=True)),
                ('buyingredient5', models.CharField(blank=True, max_length=255, null=True)),
                ('buyingredient6', models.CharField(blank=True, max_length=255, null=True)),
                ('buyingredient7', models.CharField(blank=True, max_length=255, null=True)),
                ('buyingredient8', models.CharField(blank=True, max_length=255, null=True)),
                ('buyingredient9', models.CharField(blank=True, max_length=255, null=True)),
                ('buyingredient10', models.CharField(blank=True, max_length=255, null=True)),
                ('buyQuantityIng1', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityIng2', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityIng3', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityIng4', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityIng5', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityIng6', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityIng7', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityIng8', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityIng9', models.PositiveIntegerField(blank=True, null=True)),
                ('buyQuantityIng10', models.PositiveIntegerField(blank=True, null=True)),
                ('buyOrBought', models.BooleanField(default=False)),
                ('DoneOrder', models.BooleanField(default=False)),
                ('payment_method', models.CharField(blank=True, choices=[('cash', 'Cash'), ('gcash', 'GCash')], max_length=255, null=True)),
                ('DineIn_Out', models.CharField(blank=True, choices=[('IN', 'Dine In'), ('OUT', 'Dine Out')], max_length=255, null=True)),
                ('AllPayment', models.FloatField(blank=True, null=True)),
                ('tenderedPayment', models.FloatField(blank=True, null=True)),
                ('orderNumber', models.PositiveIntegerField(blank=True, null=True)),
                ('dateordered', models.DateTimeField(blank=True, null=True)),
                ('priceSize', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('categorytype', models.CharField(choices=[('DRINKS', 'Drinks'), ('FOOD', 'Food')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockname', models.CharField(max_length=50)),
                ('stockcategory', models.CharField(choices=[('INGR', 'Ingredients'), ('AO', 'AddOns'), ('UTNSL', 'Utensils')], max_length=100)),
                ('stockquantity', models.PositiveIntegerField()),
                ('stockmeasurement', models.CharField(choices=[('G', 'Grams'), ('PCS', 'Pieces'), ('ML', 'MiliLiters')], max_length=100)),
                ('stockdate_in', models.DateField()),
                ('stockexpiration', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MenuDrinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuname', models.CharField(max_length=100)),
                ('menuAOPrice1', models.FloatField(blank=True, null=True)),
                ('menuAOPrice2', models.FloatField(blank=True, null=True)),
                ('menuAOPrice3', models.FloatField(blank=True, null=True)),
                ('menuAOPrice4', models.FloatField(blank=True, null=True)),
                ('menuAOPrice5', models.FloatField(blank=True, null=True)),
                ('menuimage', models.ImageField(upload_to='mema/')),
                ('menuprice1', models.FloatField(blank=True, null=True)),
                ('menuprice2', models.FloatField(blank=True, null=True)),
                ('menuprice3', models.FloatField(blank=True, null=True)),
                ('hotAndCold', models.CharField(blank=True, choices=[('hot', 'Hot'), ('cold', 'Cold'), ('both', 'Hot and Cold')], max_length=15, null=True)),
                ('quantityIng1', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityIng2', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityIng3', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityIng4', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityIng5', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityIng6', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityIng7', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityIng8', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityIng9', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityIng10', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityAO1', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityAO2', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityAO3', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityAO4', models.PositiveIntegerField(blank=True, null=True)),
                ('quantityAO5', models.PositiveIntegerField(blank=True, null=True)),
                ('addons1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addons1', to='pos.stocks')),
                ('addons2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addons2', to='pos.stocks')),
                ('addons3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addons3', to='pos.stocks')),
                ('addons4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addons4', to='pos.stocks')),
                ('addons5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addons5', to='pos.stocks')),
                ('ingredient1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient1', to='pos.stocks')),
                ('ingredient10', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient10', to='pos.stocks')),
                ('ingredient2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient2', to='pos.stocks')),
                ('ingredient3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient3', to='pos.stocks')),
                ('ingredient4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient4', to='pos.stocks')),
                ('ingredient5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient5', to='pos.stocks')),
                ('ingredient6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient6', to='pos.stocks')),
                ('ingredient7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient7', to='pos.stocks')),
                ('ingredient8', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient8', to='pos.stocks')),
                ('ingredient9', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ingredient9', to='pos.stocks')),
                ('menucategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos.menucategory')),
            ],
        ),
    ]