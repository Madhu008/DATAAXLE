class ParkingSpot(models.Model):  lat = models.FloatField()  long = models.FloatField()
class Reservation(models.Model):  spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)  hours = models.IntegerField()  price = models.FloatField()
