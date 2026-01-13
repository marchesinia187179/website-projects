# Final Test 05

![Page 1](https://github.com/marchesinia187179/website-projects/blob/2dd931ce9dc3dde90020c4f316da1d8bfad5128c/FinalTest05/images/page1.png)
![Page 2](https://github.com/marchesinia187179/website-projects/blob/2dd931ce9dc3dde90020c4f316da1d8bfad5128c/FinalTest05/images/page2.png)
![Page 3](https://github.com/marchesinia187179/website-projects/blob/2dd931ce9dc3dde90020c4f316da1d8bfad5128c/FinalTest05/images/react1.png)

## Description
1. Write two functions to read and return all videogames from the `videogames.csv` file and all ratings from the `ratings.csv` file. The `videogames.csv` file contains columns for code, name, and company, while `ratings.csv` includes username, code, and rating. These functions must be called in `app.py`, and file loading must be implemented in a single part of the code.

2. Modify the `/index` route to render an `index.html` template that extends the base template. The template must display a table listing available videogames, showing the videogame name and the average of its associated ratings. If a videogame has no ratings, display "nessuna valutazione disponibile" (no ratings available).

3. Make the videogame name in the table clickable. Clicking it should redirect the user to a dedicated page `/videogame/<game_code>` showing the details of the corresponding game. This page must include the videogame name, the list of ratings, and a button to return to `index.html`.

4. On the videogame detail page, add two input fields for "username" and "valutazione" (rating). The rating must be a numeric field with values ranging from 1 to 10. Include an "Aggiungi" (Add) button that calls a Flask API via the POST method to add the new rating to the `ratings.csv` file, associated with the game's code.

5. Create two APIs:
   * One to return all ratings in JSON format.
   * One to return only the ratings linked to a single videogame.
   * These APIs should return a dictionary containing the data without the file column headers.

6. Create a `/react` route on the Flask side to render the `index_react.html` template for a React Single Page Application (SPA). All React-specific routes must use the `/react` prefix (e.g., `/react/videogames`, `/react/detail`).

7. Create a React component `VideogameList` to display a table showing the code and name of each videogame. This component should be associated with the route `/react/videogames`.

8. In the `VideogameList` component, insert a form above the table to add a new videogame. The form should take a name and a company as input. The game code must be generated automatically on the backend within a specific Flask API that saves the new videogame to `videogames.csv`.
