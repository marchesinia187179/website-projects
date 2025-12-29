document.addEventListener("submit", function(event) {
    checkForm(event);
});

function checkForm(event) {
    let validForm = true;

    // Check the email
    const email = document.getElementById("email").value;
    if (!email.endsWith("gmail.com") && !email.endsWith("yahoo.it")) {
        event.preventDefault(); // Prevent the form from actually sending/refreshing
        document.getElementById("error-email").innerHTML = "L'email deve finire con gmail.com oppure yahoo.it!";
        validForm = false;
    }

    // Check the phone number
    const phone = document.getElementById("phone").value;
    if (phone.length != 10) {
        event.preventDefault();
        document.getElementById("error-phone").innerHTML = "Il numero di telefono deve essere di 10 cifre!";
        validForm = false;
    }

    // Check the password
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm-password").value;
    if (password != confirmPassword) {
        event.preventDefault();
        document.getElementById("error-password").innerHTML = "La password di conferma deve essere uguale alla password inserita!";
        validForm = false;
    }

    // Validity message
    if (validForm == true) {
        window.alert("Il form è stato inviato");
    }
}