# Final Test 02

![Page 1]()
![Page 2]()

## Description
1. Write a function that returns all events present in the `events.csv` file. The file contains the following columns: event code, event name, sport, date, location, and available seats.

2. Modify the `/index` route to render an `index.html` template that extends the base template. The template must display a table with the available sporting events. If there are no events, show the message "Nessun evento disponibile".

3. Make every row of the table clickable. When a user clicks on an event, redirect them to a dedicated page `/event/<event_code>` that shows the details of the event corresponding to the code, formatted in a clear and readable way.

4. On the event page, add a button to book a seat for the event. The button must call a Flask API `/api/book/<event_code>` via the POST method. Reduce the number of available seats in the `events.csv` file by one. Handle any errors, such as sold-out seats, by showing appropriate messages to the user.

5. Create two APIs:
   * One to return all events in JSON format.
   * One to return the details of a single event based on the event code.

6. Create a `/react` route on the Flask side to render the `index_react.html` template to build a SPA with React. All routes set up with React must fall under the `/react` path (e.g., `/react/event_detail`, `/react/book`, etc.).

7. Create a React component `EventList` to display the list of events in a table similar to the one in point 3. Unlike the previous table, each row must have a button to book a seat, which triggers a confirmation before performing the action. Update the available seats in real-time.

8. Make the event name clickable in the React table to navigate to a `/react/event/:id` route. Use an `EventDetail` component to display the details of the selected event.
