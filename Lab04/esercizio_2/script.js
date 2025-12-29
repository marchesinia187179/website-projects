function getRadioCheckedValue(radioGroup) {
    for (option of radioGroup) {
        if (option.checked){
            return option.values;
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


form.addEventListener('submit', function(event) {
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

    // Check if HTTP status is OK (200–299)

    // Throwing makes the chain go to the catch()
        
    // Assuming result.data is a JSON-string that needs parsing
      

    // Handle the error
      
  });
  
