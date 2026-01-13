# All in one

![Page 1](https://github.com/marchesinia187179/website-projects/blob/909425751d69d84ea18b98e1934669f02ef0d0a4/Lab07/images/page1.png)
![Page 2](https://github.com/marchesinia187179/website-projects/blob/909425751d69d84ea18b98e1934669f02ef0d0a4/Lab07/images/page2.png)
![Page 3](https://github.com/marchesinia187179/website-projects/blob/909425751d69d84ea18b98e1934669f02ef0d0a4/Lab07/images/page3.png)
![Page 4](https://github.com/marchesinia187179/website-projects/blob/909425751d69d84ea18b98e1934669f02ef0d0a4/Lab07/images/page4.png)
![Page 5](https://github.com/marchesinia187179/website-projects/blob/909425751d69d84ea18b98e1934669f02ef0d0a4/Lab07/images/page5.png)

### Exercise 1 - HTML Static
Creation of the basic structure of a Flask application with static HTML pages.

Main objectives:
- Initialize a Flask app in `app.py`.
- Create routes for `/`, `/about`, and `/contact`.
- Render static `.html` files for each route using `render_template`.

### Exercise 2 - Import from JSON
Displaying dynamic content by passing data from the backend to the frontend.

Features:
- Define a list of dictionaries in `app.py` representing team members.
- Pass the list to the `team.html` template.
- Use Jinja2 syntax to loop through and display member details.

### Exercise 3 - Import from CSV
Reading data from external files to populate the website.

- Implement a function to parse `library.csv` or `products.csv`.
- Ensure data is correctly formatted as a list of objects before being sent to the template.

### Exercise 4 - Templates
Using template inheritance to create a consistent layout across all pages.

- Create a `base.html` containing the navigation bar and footer.
- Use `{% extends "base.html" %}` and `{% block content %}` in child pages like `index.html` and `about.html`.

### Exercise 5 - Table from CSV
Building a dynamic table based on file content.

Functionality:
- Read event or product data from a CSV.
- Render an HTML table.
- Implement conditional messages like "No items available" if the file is empty.

### Exercise 6 - API & Form
Handling user input and creating backend endpoints.

- Create a POST API endpoint (e.g., `/api/book` or `/api/buy`).
- Update the CSV file based on form submissions.
- Implement a React-based SPA route under `/react` to fetch data from these APIs and update the UI in real-time.
