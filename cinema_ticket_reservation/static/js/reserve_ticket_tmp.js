const container = document.querySelector('.seat-container');
const seats = document.querySelectorAll('.seat:not(.occupied)');
const count = document.getElementById('count');
const price = document.getElementById('price');

const updateSelectedSeatsCount = () => {
  const selectedSeats = document.querySelectorAll('.seat.selected');
  const selectedSeatsCount = selectedSeats.length;
  const ticketPrice = 10;  // Example ticket price, this should be dynamic based on your pricing logic

  count.innerText = selectedSeatsCount;
  price.innerText = selectedSeatsCount * ticketPrice;
};

container.addEventListener('click', (e) => {
  if (e.target.classList.contains('seat') && !e.target.classList.contains('occupied')) {
    e.target.classList.toggle('selected');
    const checkbox = e.target.querySelector('input[type="checkbox"]');
    if (checkbox) {
      checkbox.checked = !checkbox.checked;
    }
    updateSelectedSeatsCount();
  }
});

updateSelectedSeatsCount();
