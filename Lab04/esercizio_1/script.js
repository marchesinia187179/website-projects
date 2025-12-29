var button = document.getElementById('button');

button.onclick = function () {

    // 1. Make a GET request using Fetch API
    fetch("https://jsonplaceholder.typicode.com/posts")
    .then(response => {

        // Check if the response is OK (status 200-299)
        if (!response.ok) {
            throw new Error("Error request: " + response.status);
        }

        // 2. Use a promise to convert it to JSON fileConvert the response to JSON
        return response.json();
    })
    .then(data => {     // 3. Use a promise to create HTML for each post

        // 3.a Select the post container from the DOM
        const postsContainer = document.getElementById("postsContainer");

        // 3.b Iterate over the posts and create HTML elements
        for (let i = 0; i < data.length; i++) {

            // Create a div component to contain the post title and body
            var divPost = document.createElement("div");
            divPost.className = "post";

            // Create a title getting the post title from the data
            var titlePost = document.createElement("h4");
            titlePost.innerHTML = `Post ${i + 1}: ${data[i].title} `;

            // Create a description getting the post body from the data
            var bodyPost = document.createElement("p");
            bodyPost.innerHTML = data[i].body;

            // Append the post title and body to the div component
            divPost.appendChild(titlePost);
            divPost.appendChild(bodyPost);

            // Append the div component to the posts container
            postsContainer.appendChild(divPost);
        }

    })
    .catch(error => {   // 4. Use a promise to handle any errors

        // Select the post container from the DOM
        const postsContainer = document.getElementById("postsContainer");

        // Add an error text in red
        postsContainer.innerHTML = "Error getting posts!";
        postsContainer.style.color = "red";

    });

};
