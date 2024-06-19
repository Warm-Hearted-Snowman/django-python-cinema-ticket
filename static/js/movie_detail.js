document.addEventListener("DOMContentLoaded", function() {
    const cinemaCards = document.querySelectorAll('.cinema-card');

    cinemaCards.forEach(card => {
        card.addEventListener('click', function() {
            const cinemaId = this.getAttribute('data-cinema-id');
            const accordionContainer = document.querySelector(`#accordionCinema${cinemaId}`);

            // Hide all other accordions
            document.querySelectorAll('.accordion-container').forEach(container => {
                if (container !== accordionContainer) {
                    container.style.display = 'none';
                }
            });

            // Toggle the current accordion
            if (accordionContainer.style.display === 'none' || accordionContainer.style.display === '') {
                accordionContainer.style.display = 'block';
            } else {
                accordionContainer.style.display = 'none';
            }
        });
    });

    const accordionHeaders = document.querySelectorAll('.accordion-header');

    accordionHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const collapseElement = this.nextElementSibling;
            collapseElement.classList.toggle('show');
        });
    });
});