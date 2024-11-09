const wrapper = document.querySelector('.wrapper');
const registerLink = document.querySelector('.register-link');
const loginLink = document.querySelector('.login-link');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');

// Toggle to show the registration form and clear login inputs
registerLink.onclick = () => {
    wrapper.classList.add('active');
    loginForm.reset();  // Clear login form inputs
}

// Toggle to show the login form and clear registration inputs
loginLink.onclick = () => {
    wrapper.classList.remove('active');
    registerForm.reset();  // Clear registration form inputs
}

// Handle registration form submission
document.getElementById('registerForm').onsubmit = async function (event) {
    event.preventDefault();

    const data = {
        username: document.getElementById('username').value,
        email: document.getElementById('email').value,
        password: document.getElementById('password').value,
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log(result);
        alert(JSON.stringify(result));

    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
};
