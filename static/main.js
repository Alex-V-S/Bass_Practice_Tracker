document.addEventListener("DOMContentLoaded", () => {
    fetch('/api/techniques')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('techniques-list');
            
            data.forEach(technique => {
                const listItem = document.createElement('li');
                
                // Inject the name and category from the database
                listItem.innerHTML = `
                    <strong>${technique.name}</strong> 
                    <span>(${technique.category})</span>
                `;
                
                list.appendChild(listItem);
            });
        })
        .catch(error => console.error('Error fetching techniques:', error));

        //New form submission handler
        const form = document.getElementById('add-technique-form');

        form.addEventListener('submit', (e) => {
            //Prevents page from hard-refreshing
            e.preventDefault();

            const name = document.getElementById('technique-name').value;
            const category = document.getElementById('technique-category').value;

            // Send the POST request to Flask
            fetch('/api/techniques', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name: name, category: category })
            })
            .then(response => response.json())
            .then(data => {
                //Refresh the page automatically to show the newly added technique
                location.reload();
            })
            .catch(error => console.error('Error adding technique:', error));
        })
});