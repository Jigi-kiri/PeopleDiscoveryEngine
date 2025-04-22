document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.getElementById('searchForm');
    const searchQuery = document.getElementById('searchQuery');
    const resultsDiv = document.getElementById('results');
    const explanationDiv = document.getElementById('explanation');

    const API_URL = 'http://localhost:8000';

    searchForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const query = searchQuery.value.trim();
        if (!query) return;

        try {
            // Show loading state
            resultsDiv.innerHTML = '<p>Searching...</p>';
            explanationDiv.innerHTML = '';

            // Send search request to backend
            const response = await fetch(`${API_URL}/search`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query }),
            });

            if (!response.ok) {
                throw new Error('Search failed');
            }

            const data = await response.json();
            displayResults(data);
        } catch (error) {
            console.error('Error:', error);
            resultsDiv.innerHTML = '<p class="error">Sorry, something went wrong. Please try again.</p>';
        }
    });

    function displayResults(data) {
        // Display AI explanation
        explanationDiv.innerHTML = `<p>${data.explanation}</p>`;

        // Display matched profiles
        if (!data.matches || data.matches.length === 0) {
            resultsDiv.innerHTML = '<p>No matches found.</p>';
            return;
        }

        resultsDiv.innerHTML = data.matches.map(profile => `
            <div class="profile-card">
                <h3>${profile.name}</h3>
                <p class="bio">${profile.bio}</p>
                <div class="interests">
                    ${profile.interests.map(interest => 
                        `<span class="interest-tag">${interest}</span>`
                    ).join('')}
                </div>
                <p class="vibe">${profile.vibe}</p>
            </div>
        `).join('');
    }

    // Add example query on input field click
    searchQuery.addEventListener('click', () => {
        if (!searchQuery.value) {
            searchQuery.value = 'Find me artists who love hiking and talk like Tarantino';
        }
    });
});