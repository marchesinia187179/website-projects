# Final Test 03

![Page 1]()
![Page 2]()
![React 1]()

## Description
1. Write a function to read and return all products from the `products.csv` file. The file includes columns for product code, name, category, price, availability, and description. This function must be called in `app.py` to retrieve the product list.

2. Modify the `/index` route to render an `index.html` template that extends the base template. The template should display a table of available products. If no products exist, show the message "Nessun prodotto disponibile". The table should only display the product name, price, and an "Esaurito" (Out of Stock) label in a separate column if the product is unavailable.

3. Make each product name clickable. Clicking a name should redirect the user to a dedicated page `/product/<product_code>` displaying all product details in a clean format. This page must also include a button to return to the `index.html` page.

4. Add a "Buy" button to the product detail page. This button must call a Flask API `/api/buy/<product_code>` using the POST method. The action should decrease the product's availability in the `products.csv` file by one. Handle errors, such as out-of-stock scenarios, with appropriate user messages.

5. Create two APIs:
   * One to return all products in JSON format.
   * One to return the details of a single product as a dictionary based on its product code.

6. Create a `/react` route in Flask to render the `index_react.html` template for a React-based Single Page Application (SPA). All React routes must use the `/react` prefix (e.g., `/react/product_detail`).

7. Create a React component `ProductList` to display the product list in a table similar to the one described in point 2, but without the clickable name requirement.

8. Add a filter form to the `ProductList` component consisting of an input field and a button. If the field contains text, the table should only show products with names containing that string. If the field is empty, the table should show all products.
