import asyncio
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from asgiref.sync import sync_to_async
from books.models import Book
from rides.models import Ride


class Command(BaseCommand):
    help = 'Task that runs every day'

    def handle(self, *args, **kwargs):
        asyncio.run(self.run())

    async def run(self):
        rides = await sync_to_async(self.get_rides)()

        if not rides:
            print("No rides to delete.")
            return

        await sync_to_async(self.delete_bookings)(rides)

        await sync_to_async(rides.delete)()
        print(f"Deleted rides and their bookings.")

    @staticmethod
    def get_rides():
        cutoff_date = datetime.now().date() - timedelta(days=2)
        return Ride.objects.filter(ride_date__lt=cutoff_date) or None

    @staticmethod
    def delete_bookings(rides):
        ride_ids = rides.values_list('id', flat=True)
        Book.objects.filter(ride_id__in=ride_ids).delete()


if __name__ == "__main__":
    Command().handle()
