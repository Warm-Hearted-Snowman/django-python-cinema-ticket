// reserve_ticket.js
$(document).ready(function () {
    // Add hover event to show details on seat hover
    $('.seat').hover(function () {
        const tooltip = $(this).attr('title', `
            Row: ${$(this).data('row')}
            Column: ${$(this).data('column')}
            Status: ${$(this).data('status')}
            Price: ${$(this).data('price')}
        `);
        tooltip.tooltip('show');
    }, function () {
        $(this).tooltip('hide');
    });

    // Add click event to toggle selected class on seats
    $('input[name="selected_seats"]').change(function () {
        const seat = $(this).closest('.seat');
        seat.toggleClass('selected', this.checked);
    });
});
