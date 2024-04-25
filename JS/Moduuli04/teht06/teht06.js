 document.getElementById('searchForm').addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevent default form submission behavior

            const searchTerm = document.getElementById('searchTerm').value.trim();

            try {
                const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${encodeURIComponent(searchTerm)}`);
                const data = await response.json();
                displayJokes(data.result);
            } catch (error) {
                console.error('Error fetching Chuck Norris jokes:', error);
            }
        });

        function displayJokes(jokes) {
            const jokesContainer = document.getElementById('jokesContainer');
            jokesContainer.innerHTML = ''; // Clear previous jokes

            jokes.forEach(joke => {
                const article = document.createElement('article');
                const paragraph = document.createElement('p');
                paragraph.textContent = joke.value;
                article.appendChild(paragraph);
                jokesContainer.appendChild(article);
            });
        }