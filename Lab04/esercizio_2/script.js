function getRadioCheckedValue(radioGroup) {
    for (option of radioGroup) {
        if (option.checked){
            return option.value;
        }
    }
}

function getCheckboxValues(checkBox) {
    var checked = []
    for (option of checkBox) {
        if (option.checked){
            checked.push(option.value)
        }
    }

    return checked;
}

function getSelectedValues(sel){
    return sel.options[sel.selectedIndex].value;
}

const registrationForm = document.getElementById('regForm');

registrationForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission
  
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const email    = document.getElementById('email').value;
    const gender   = getRadioCheckedValue(document.getElementsByName('gender'));
    const interests= getCheckboxValues(document.getElementsByName('interests'));
    const country  = getCheckboxValues(document.getElementsByName('country'));
  
    const params = {
      username: username,
      password: password,
      email:    email,
      gender:   gender,
      interests: interests,
      country:  country
    };

    // Use the Fetch API to make the POST request
    fetch("https://httpbin.org/post", {    // Start the network request to the specified URL
        // Specify the HTTP method as POST to send data to the server
        method: "POST",
        // Define metadata for the request
        headers: {
            // Inform the server that the data being sent is in JSON format
            "Content-Type": "application/json"
        },
        // Convert the JavaScript object 'params' into a JSON string for transmission
        body: JSON.stringify(params)
    })
    .then(response => {

        // Check if HTTP status is OK (200–299)
        if (!response.ok) {
            // Throwing makes the chain go to the catch()
            throw new Error("Error response: " + response.status);
        }

        return response.json();

    })
    .then(result => {

        // Assuming result.data is a JSON-string that needs parsing
        const data = JSON.parse(result.data);
        const responseUsername = data.username;

        /* Get the div for the response from the DOM
         * and add the success string   */
        document.getElementById("response").innerHTML = "Utente " + responseUsername + " creato!";
        document.getElementById('response').style.color = 'green';

    })
    .catch(error => {   

        /* Get the div for the response from the DOM
         * and add the success string   */
        document.getElementById("response").innerHTML = "Utente non creato!";
        document.getElementById('response').style.color = 'red';

        // Handle the error
        console.error("Fetch error: ", error);

    });
  });

