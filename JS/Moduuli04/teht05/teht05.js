     document.getElementById('fetchJokeBtn').addEventListener('click', async () => {
            try {
                const response = await fetch('https://api.chucknorris.io/jokes/random');
                const data = await response.json();
                const joke = data.value;
                console.log('Chuck Norris Joke:', joke);
            } catch (error) {
                console.error('Error fetching Chuck Norris joke:', error);
            }
        });