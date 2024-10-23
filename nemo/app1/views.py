import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json

# ESP32 device information (replace with actual details)
ESP32_IP = '192.168.27.170'  # Update with your ESP32 IP
ESP32_FEED_ENDPOINT = f'http://{ESP32_IP}/feed'

# Home view to render the HTML page
def home(request):
    return render(request, 'index.html')

# Feed Now View
@csrf_exempt
def feed_now(request):
    if request.method == 'POST':
        try:
            # Send HTTP request to ESP32 to trigger feeding
            response = requests.get(ESP32_FEED_ENDPOINT)
            print(response)
            if response.status_code == 200:
                return JsonResponse({'message': 'Feeding now!'}, status=200)
            else:
                return JsonResponse({'message': 'Failed to feed. Try again!'}, status=500)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'message': f'Error communicating with ESP32: {e}'}, status=500)

# Schedule Feeding View
@csrf_exempt
def schedule_feeding(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        feeding_time = data.get('time')

        if not feeding_time:
            return JsonResponse({'message': 'No time specified'}, status=400)

        try:
            # Here you could integrate logic to schedule feeding at the specified time.
            # For now, we will simulate that the ESP32 will receive the command at that time.
            # In real-life implementation, you could use Django-celery or a cron job to schedule this.

            # Convert scheduled time to a Python time object for logging or validation purposes
            feed_time = timezone.datetime.strptime(feeding_time, '%H:%M').time()

            # Simulate scheduling (you can replace this with actual logic using Celery or similar)
            return JsonResponse({'message': f'Feeding scheduled at {feed_time}'}, status=200)

        except Exception as e:
            return JsonResponse({'message': f'Error scheduling feed: {e}'}, status=500)
