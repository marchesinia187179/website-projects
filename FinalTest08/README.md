# Final Test 08

![Page 1](https://github.com/marchesinia187179/website-projects/blob/66b2a1e2423ac1fd2c094a3b29ece74e307c7cd8/FinalTest08/images/page1.png)
![Page 2](https://github.com/marchesinia187179/website-projects/blob/66b2a1e2423ac1fd2c094a3b29ece74e307c7cd8/FinalTest08/images/page2.png)
![React 1](https://github.com/marchesinia187179/website-projects/blob/66b2a1e2423ac1fd2c094a3b29ece74e307c7cd8/FinalTest08/images/react1.png)
![React 2](https://github.com/marchesinia187179/website-projects/blob/66b2a1e2423ac1fd2c094a3b29ece74e307c7cd8/FinalTest08/images/react2.png)

## Description
1. Write two functions to read and return all courses from the `courses.csv` file and all bookings from the `bookings.csv` file. The `courses.csv` file contains fields for ID, name, instructor name, day of the week, hours, and total places. The `bookings.csv` file contains ID, course ID, first name, and last name. These functions must be called in `app.py` to retrieve the data.

2. Modify the `/index` route to render an `index.html` template that extends the base template. The template must display a table with the list of available courses, showing the course name, instructor, day, and time. If no courses are available, display the message "Nessun corso disponibile".

3. Make each course name clickable. When a user clicks on a course, redirect them to a dedicated page `/course/<course_id>` that shows all the details of the selected course and the list of people who have booked it. This page must also include a button to return to `index.html`.

4. On the course detail page, add a form for booking a spot. The form should take the user's first name and last name as input. When the "Prenota" (Book) button is clicked, call a Flask API via the POST method to save the new booking in `bookings.csv`. Ensure the system checks if there are still available spots (total places minus current bookings) and shows an appropriate error message if the course is full.

5. Create two APIs:
   * One to return all courses in JSON format.
   * One to return all bookings associated with a specific course ID.

6. In the `index_react.html` template, create a React component `CourseList` to render a table of courses similar to the one in point 2, but also displaying the total number of spots. This component should be associated with the route `/react/courses`.

7. In the `CourseList` component, insert a button labeled "Aggiungi nuovo corso" (Add new course). Clicking this button should redirect the user to a `/react/add_course` route associated with an `AddCourseForm` component.

8. The `AddCourseForm` component must render a form to input new course details. Upon successful submission, the new course ID must be generated on the backend, the data saved to `courses.csv`, and a green confirmation message or red error message should be displayed to the user.
