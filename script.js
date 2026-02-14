
     // 3. Collect form data
    const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        date: document.getElementById('date').value,
        time: document.getElementById('time').value
    };

    /** * 4. Connection Logic
     * If using Nginx as a reverse proxy (recommended), use "/api/reserve"
     * If connecting directly to the App Server, use "http://<APP_PRIVATE_IP>:5000/api/reserve"
     */
    const APP_SERVER_URL = "/api/reserve";

    try {
        const response = await fetch(APP_SERVER_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        // 5. Handle success or error messages
        if (response.ok) {
            status.innerText = "✓ " + (result.message || "Reservation successful!");
            status.style.color = "#4BB543"; // Success Green
            document.getElementById('bookingForm').reset(); // Clear the form
        } else {
            status.innerText = "✕ " + (result.error || "Failed to save reservation.");
            status.style.color = "#ff3333"; // Error Red
        }

    } catch (err) {
        // 6. Handle network/connection errors
        status.innerText = "✕ Error: Cannot reach the server. Check your AWS Security Groups.";
        status.style.color = "#ff3333";
        console.error("Connection Error:", err);
    } finally {
        // 7. Reset button state
        submitBtn.innerText = "Book Now";
        submitBtn.disabled = false;
    }
});
