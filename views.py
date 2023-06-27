from django.shortcuts import get_object_or_404from django.http import JsonResponse
from .models import ParkingSpot, Reservation
def get_all_parking_spots(request):  spots = ParkingSpot.objects.all()  data = [{'id': spot.id, 'lat': spot.lat, 'long': spot.long} for spot in spots]  return JsonResponse(data, safe=False)
def search_nearby_parking_spots(request, lat, long, radius):  spots = ParkingSpot.objects.raw("""    SELECT id, lat, long    FROM parking_parkingspot    WHERE (lat - %s) * (lat - %s) + (long - %s) * (long - %s) <= %s * %s  """, [lat, lat, long, long, radius, radius])  data = [{'id': spot.id, 'lat': spot.lat, 'long': spot.long} for spot in spots]  return JsonResponse(data, safe=False)
def reserve_parking_spot(request, spot_id, hours):  spot = get_object_or_404(ParkingSpot, pk=spot_id)  price = calculate_price(hours)  reservation = Reservation.objects.create(spot=spot, hours=hours, price=price)  return JsonResponse({'spot_id': spot_id, 'hours': hours, 'price': price})
def get_all_reservations(request):  reservations = Reservation.objects.all()  data = [{'spot_id': reservation.spot_id, 'hours': reservation.hours, 'price': reservation.price} for reservation in reservations]  return JsonResponse(data, safe=False)
def calculate_price(hours):  # Simplified price calculation for demonstration purposes  return hours * 10.0
