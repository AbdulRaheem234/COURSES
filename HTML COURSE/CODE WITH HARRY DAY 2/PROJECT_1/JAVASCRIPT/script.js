// Input focus & blur effect
const searchInput = document.querySelector('.search-box input');
const searchButton = document.querySelector('.search-box button');

searchInput.addEventListener('focus', () => {
  searchInput.style.borderColor = '#ff5e5e';
});

searchInput.addEventListener('blur', () => {
  searchInput.style.borderColor = '#ccc';
});

// Simulate a search interaction
searchButton.addEventListener('click', () => {
  const query = searchInput.value.trim();
  if (query.length > 0) {
    alert(`Searching for: "${query}"...`);
  } else {
    alert("Please enter something to search!");
  }
});
