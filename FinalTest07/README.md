# Final Test 07

![Page 1]()
![Page 2]()
![React 1]()
![React 2]()

## Description
1. Write two functions to read and return all places from the `places.csv` file and all itineraries from the `itineraries.csv` file. The `places.csv` file contains columns for place ID, name, category, municipality, image link, and price. The `itineraries.csv` file contains the itinerary ID, name, duration, and a list of place IDs. These functions must be called in `app.py`, and file loading must be implemented in a single part of the code.

2. Modify the `/index` route to render an `index.html` template that extends the base template. The template should display a list or table of the available places or itineraries as specified in the project structure.

3. Make the elements in the table clickable. When a user clicks on an item, redirect them to a dedicated page (e.g., `/place/<place_id>` or `/itinerary/<itinerary_id>`) that shows the corresponding details formatted in a clear and readable way.

4. Implement functionality to view specific itinerary details. For a selected itinerary, display its name, duration, and the list of places included. For each place in the itinerary, show its specific details such as category and price.

5. Create two APIs:
   * One to return all places in JSON format.
   * One to return the details of a specific itinerary, including the data of all places contained within it, based on the itinerary ID.

6. Create a `/react` route on the Flask side to render the `index_react.html` template for a React Single Page Application (SPA). All React-specific routes must use the `/react` prefix (e.g., `/react/place`, `/react/itinerary`).

7. Create a React component `ItineraryList` to display the list of itineraries in a table showing the name, duration, and the total price (calculated as the sum of the prices of the places included in the itinerary). This component must also include a "Crea Itinerario" (Create Itinerary) button or link and be associated with the route `/react/itineraries`.

8. The "Crea Itinerario" button must lead to a `NewItinerary` component containing a form to add a new itinerary. The form must allow the user to select from the places available in `places.csv`. The new itinerary ID must be generated automatically on the backend within a specific Flask API that saves the entry to `itineraries.csv`.