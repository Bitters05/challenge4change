const wrapper = document.querySelector('.wrapper');
const registerLink = document.querySelector('.register-link');
const loginLink = document.querySelector('.login-link');
const loginForm = document.getElementById('loginForm');
const registerForm = document.getElementById('registerForm');

// Toggle to show the registration form and clear login inputs
registerLink.onclick = () => {
    wrapper.classList.add('active');
    loginForm.reset();  // Clear login form inputs
};

// Toggle to show the login form and clear registration inputs
loginLink.onclick = () => {
    wrapper.classList.remove('active');
    registerForm.reset();  // Clear registration form inputs
};

// Handle registration form submission
registerForm.onsubmit = async function (event) {
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

        const result = await response.json();
        if (response.ok) {
            alert(result.message);  // Alert user for successful registration
            // Initiate redirect
            initiateRedirect();
        } else {
            alert(result.message || 'Registration failed.');  // Show error message
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
};

// Handle login form submission
loginForm.onsubmit = async function (event) {
    event.preventDefault();

    const data = {
        username: document.getElementById('loginUsername').value,
        password: document.getElementById('loginPassword').value,
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        const result = await response.json();
        if (response.ok) {
            alert(result.message);  // Alert user for successful login
            // Initiate redirect
            initiateRedirect();
        } else {
            alert(result.message || 'Login failed.');  // Show error message
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    }
};

// Function to handle page redirection with fade-out effect
function initiateRedirect() {
    document.body.classList.add('redirecting');  // Add redirecting class to body for fade-out effect

    setTimeout(() => {
        // Redirect to the target page after the fade-out effect
        window.location.href = "page.html";  // Change this to your target URL
    }, 500); // Delay the redirect to let the fade-out effect complete
}
