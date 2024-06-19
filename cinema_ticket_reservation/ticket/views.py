from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from cinema.models import Hall, Seat
from django.views.decorators.http import require_POST

from ticket.models import Ticket


@login_required(login_url='account:login')
def reserve_ticket(request, schedule_id):
    schedule = get_object_or_404(Hall, Schedule_ID=schedule_id)
    if request.method == 'POST':
        selected_seats = request.POST.getlist('selected_seats')

        invalid_seats = Seat.objects.filter(schedule=schedule, Seat_ID__in=selected_seats, status='Booked')
        if invalid_seats.exists():
            return render(request, 'error_page.html',
                          {'error_message': 'One or more selected seats are not available for booking.'})

        for seat_id in selected_seats:
            Seat.book_seat(seat_id, schedule)

        new_ticket = Ticket.objects.create(
            schedule_id=schedule,
            user=request.user,
            time_on_reserve=datetime.now()
        )
        new_ticket.seats.set(selected_seats)
        new_ticket.save()

        return redirect('ticket:detail', ticket_id=new_ticket.Ticket_ID)

    available_seats = Seat.objects.filter(schedule_id=schedule, status='قابل خرید').order_by('row', 'column')
    organized_seats = {}
    for seat in available_seats:
        row = seat.row
        if row not in organized_seats:
            organized_seats[row] = []
        organized_seats[row].append(seat)

    return render(request, 'reserve_ticket.html', {
        'schedule': schedule,
        'available_seats': organized_seats.values(),
        'hall': schedule
    })


def reservation_success(request, ticket_id):
    ticket = get_object_or_404(Ticket, Ticket_ID=ticket_id)
    selected_seats = ticket.seats.all()
    schedule = ticket.schedule_id
    return render(request, 'reservation_success.html',
                  {'schedule': schedule, 'selected_seats': selected_seats, 'ticket': ticket})


@require_POST
def cancel_ticket(request):
    ticket_id = request.POST.get('ticket_id')
    try:
        ticket = get_object_or_404(Ticket, Ticket_ID=ticket_id)
        ticket.cancel()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})
