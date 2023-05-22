from django.db import models

# STOCKS START
STOCK_CATEGORY = (
    ("INGR", "Ingredients"),
    ("AO", "AddOns"),
    ("UTNSL", "Utensils"),
)

STOCK_QUANTITY = (
    ("G", "Grams"),
    ("PCS", "Pieces"),
    ("ML", "MiliLiters"),
)



class Stocks(models.Model):
    stockname = models.CharField(max_length=50)
    stockcategory = models.CharField(choices=STOCK_CATEGORY, max_length=100)
    stockquantity = models.PositiveIntegerField()
    stockmeasurement = models.CharField(choices=STOCK_QUANTITY, max_length=100)
    stockdate_in = models.DateField()
    stockexpiration = models.DateField()

    def __str__(self):
        return self.stockname
# END STOCKS


# MENU START
TYPES_MENU = (
    ("DRINKS", "Drinks"),
    ("FOOD", "Food"),
)

HOT_AND_COLD_CHOICES = (
        ('hot', 'Hot'),
        ('cold', 'Cold'),
        ('both', 'Hot and Cold'),
    )

class MenuCategory (models.Model):
    name = models.CharField(max_length=100)
    categorytype = models.CharField(choices=TYPES_MENU, max_length=100)

    def __str__(self):
        return self.name


class MenuDrinks (models.Model):
    menucategory = models.ForeignKey(
        MenuCategory, on_delete=models.CASCADE)
    menuname = models.CharField(max_length=100)
    menuAOPrice1 = models.FloatField( null=True, blank=True)
    menuAOPrice2 = models.FloatField( null=True, blank=True)
    menuAOPrice3 = models.FloatField( null=True, blank=True)
    menuAOPrice4 = models.FloatField( null=True, blank=True)
    menuAOPrice5 = models.FloatField( null=True, blank=True)
    menuimage = models.ImageField(upload_to="mema/")
    menuprice1 = models.FloatField(null=True, blank=True)
    menuprice2 = models.FloatField(null=True, blank=True)
    menuprice3 = models.FloatField(null=True, blank=True)
    ingredient1 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient1', null=True, blank=True)
    ingredient2 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient2', null=True, blank=True)
    ingredient3 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient3', null=True, blank=True)
    ingredient4 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient4', null=True, blank=True)
    ingredient5 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient5', null=True, blank=True)    
    ingredient6 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient6', null=True, blank=True)
    ingredient7 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient7', null=True, blank=True)
    ingredient8 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient8', null=True, blank=True)
    ingredient9 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient9', null=True, blank=True)
    ingredient10 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='ingredient10', null=True, blank=True)
    addons1 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='addons1', null=True, blank=True)
    addons2 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='addons2', null=True, blank=True)
    addons3 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='addons3', null=True, blank=True)
    addons4 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='addons4', null=True, blank=True)
    addons5 = models.ForeignKey(
        Stocks, on_delete=models.CASCADE, related_name='addons5', null=True, blank=True)
    hotAndCold =models.CharField(max_length=15, choices=HOT_AND_COLD_CHOICES, null=True, blank=True )
    quantityIng1 = models.PositiveIntegerField(null=True, blank=True)
    quantityIng2 = models.PositiveIntegerField(null=True, blank=True)
    quantityIng3 = models.PositiveIntegerField(null=True, blank=True)
    quantityIng4 = models.PositiveIntegerField(null=True, blank=True)
    quantityIng5 = models.PositiveIntegerField(null=True, blank=True)
    quantityIng6 = models.PositiveIntegerField(null=True, blank=True)
    quantityIng7 = models.PositiveIntegerField(null=True, blank=True)
    quantityIng8 = models.PositiveIntegerField(null=True, blank=True)
    quantityIng9 = models.PositiveIntegerField(null=True, blank=True)
    quantityIng10 = models.PositiveIntegerField(null=True, blank=True)
    quantityAO1 = models.PositiveIntegerField(null=True, blank=True)
    quantityAO2 = models.PositiveIntegerField(null=True, blank=True)
    quantityAO3 = models.PositiveIntegerField(null=True, blank=True)
    quantityAO4 = models.PositiveIntegerField(null=True, blank=True)
    quantityAO5 = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.menuname} ({self.menucategory.name})"

#HOME START


PAYMENT_CHOICES = (
        ('cash', 'Cash'),
        ('gcash', 'GCash'),
    )

IN_OUT = (
        ('IN', 'Dine In'),
        ('OUT', 'Dine Out'),
    )


class buyItem(models.Model):
    buyName= models.CharField (max_length=255, null=True, blank=True)
    buySize = models.CharField(max_length=15, null=True, blank=True)
    buyQuantityMenu = models.PositiveIntegerField (null=True, blank=True)
    buyPrice = models.FloatField (null=True, blank=True)
    buyAddOns1 = models.CharField (max_length=255, null=True, blank=True)
    buyAddOns2 = models.CharField (max_length=255, null=True, blank=True)
    buyAddOns3 = models.CharField (max_length=255, null=True, blank=True)
    buyAddOns4 = models.CharField (max_length=255, null=True, blank=True)
    buyAddOns5 = models.CharField (max_length=255, null=True, blank=True)
    buyQuantityAO1 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityAO2 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityAO3 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityAO4 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityAO5 = models.PositiveIntegerField (null=True, blank=True)
    menuAOPrice1 = models.FloatField(default=0,null=True, blank=True)
    menuAOPrice2 = models.FloatField(default=0,null=True, blank=True)
    menuAOPrice3 = models.FloatField(default=0,null=True, blank=True)
    menuAOPrice4 = models.FloatField(default=0,null=True, blank=True)
    menuAOPrice5 = models.FloatField(default=0,null=True, blank=True)
    buyingredient1 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient2 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient3 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient4 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient5 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient6 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient7 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient8 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient9 = models.CharField (max_length=255, null=True, blank=True)
    buyingredient10 = models.CharField (max_length=255, null=True, blank=True)
    buyQuantityIng1 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityIng2 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityIng3 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityIng4 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityIng5 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityIng6 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityIng7 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityIng8 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityIng9 = models.PositiveIntegerField (null=True, blank=True)
    buyQuantityIng10 = models.PositiveIntegerField (null=True, blank=True)
    buyOrBought = models.BooleanField(default=False)
    DoneOrder = models.BooleanField(default=False)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_CHOICES, null=True, blank=True)
    DineIn_Out = models.CharField(max_length=255, choices=IN_OUT, null=True, blank=True)
    AllPayment = models.FloatField(null=True, blank=True)
    tenderedPayment = models.FloatField(null=True, blank=True)
    orderNumber = models.PositiveIntegerField (null=True, blank=True)
    dateordered = models.DateTimeField (null=True, blank=True)
    priceSize = models.FloatField( null=True, blank=True)

    @property
    def total_price(self):
        if not self.buyOrBought:
            buyPrice = self.buyPrice or 0.0
            menuAOPrice1 = self.menuAOPrice1 or 0.0
            menuAOPrice2 = self.menuAOPrice2 or 0.0
            menuAOPrice3 = self.menuAOPrice3 or 0.0
            menuAOPrice4 = self.menuAOPrice4 or 0.0
            menuAOPrice5 = self.menuAOPrice5 or 0.0

            return round((buyPrice + menuAOPrice1 + menuAOPrice2 + menuAOPrice3 + menuAOPrice4 + menuAOPrice5) * self.buyQuantityMenu, 2)


@property
def total_AO(self):
    menuAOPrice1 = self.menuAOPrice1 or 0.0
    menuAOPrice2 = self.menuAOPrice2 or 0.0
    menuAOPrice3 = self.menuAOPrice3 or 0.0
    menuAOPrice4 = self.menuAOPrice4 or 0.0
    menuAOPrice5 = self.menuAOPrice5 or 0.0
    
    if self.buyOrBought and menuAOPrice1 and menuAOPrice2 and menuAOPrice3 and menuAOPrice4 and menuAOPrice5:
        total_AO = menuAOPrice1 + menuAOPrice2 + menuAOPrice3 + menuAOPrice4 + menuAOPrice5
        return round(total_AO, 2)
    
    return round(menuAOPrice1 + menuAOPrice2 + menuAOPrice3 + menuAOPrice4 + menuAOPrice5, 2)

