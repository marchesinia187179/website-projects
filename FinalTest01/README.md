# Final Test 01
![Page 1](https://github.com/marchesinia187179/website-projects/blob/ee7cf5a329e1b15386a37cb115237dd1b2815570/FinalTest01/images/page1.png)
![Page 2](https://github.com/marchesinia187179/website-projects/blob/ee7cf5a329e1b15386a37cb115237dd1b2815570/FinalTest01/images/page2.png)
![Page 3](https://github.com/marchesinia187179/website-projects/blob/ee7cf5a329e1b15386a37cb115237dd1b2815570/FinalTest01/images/page3.png)
## Description
1. Write two functions to read and return:
   - all books present in the `library.csv` file.
   - all reviews present in the `reviews.csv` file.

   Note: These functions must be called where necessary in `app.py` to retrieve the list of books and reviews. File loading must be implemented in a single part of the code.

2. Display a table in `index.html` containing the list of books, if present. If the file is empty or missing, display the message "Nessun libro trovato" (No books found).

3. Make each book clickable and render a book detail page using a dynamic route with the product code (e.g., `/libro/<book_code>`). Display a page with the book details in a clean format.

4. On the detail page, insert a form below the book details to submit a review. The code for the new review must be generated on the backend. The new review must be stored in the `reviews.csv` file.

5. Create two APIs:
   - One API to return all entered books.
   - One API to return all reviews associated with a single book based on the book code passed in the URL.

6. In the `index_react.html` template, create a React component `BookList` to render a table of books similar to the one in point 2. A form for adding a book must be inserted above the table. Associate this component with the `/react` route.

7. Make the book code in each table clickable to navigate to the `/react/book/:id` route. This route must be associated with a `BookDetail` component that shows the book details similarly to the page in point 3. Below the book details, the reviews associated with it must also be displayed.
