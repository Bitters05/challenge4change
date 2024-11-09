document.getElementById('registerForm').onsubmit = async function (event) {
    event.preventDefault();

    const data = {
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/register', {  // Ensure this URL matches your backend server address
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        alert(result.message); // Notify the user of success or error

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
};
