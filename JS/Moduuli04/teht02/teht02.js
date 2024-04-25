document.getElementById("searchForm").addEventListener("submit", async (event) => {
    event.preventDefault();
    const query = document.getElementById("query").value;
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${query}`);
        const data = await response.json();
        console.log("Search Result:", data);
    } catch (error) {
        console.error("Error:", error);
    }
});
