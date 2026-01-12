# Final Test 04

![Page 1](https://github.com/marchesinia187179/website-projects/blob/e4a377e596d3728aa7d90a26d2f365fe90b13760/FinalTest04/images/page1.png)
![Page 2](https://github.com/marchesinia187179/website-projects/blob/e4a377e596d3728aa7d90a26d2f365fe90b13760/FinalTest04/images/page2.png)
![React 2](https://github.com/marchesinia187179/website-projects/blob/e4a377e596d3728aa7d90a26d2f365fe90b13760/FinalTest04/images/react1.png)

## Description
1. Write two functions to read and return all videos from `video.csv` and all comments from `comments.csv`. The `video.csv` file contains the video code, name, and link, while `comments.csv` contains the video code and comment text. These functions must be called in `app.py`, and file loading must be implemented in a single part of the code.

2. Modify the `/index` route to render an `index.html` template that extends the base template. The template must display a table listing available videos, including the video name and the total number of comments associated with each video.

3. Make the video name in the table clickable. Clicking it should redirect the user to a dedicated page `/video/<video_code>` showing the video details. This page must include an embedded video player, the video name, the list of comments, and a button to return to `index.html`.

4. On the video detail page, add a textbox and an "Add" button. This button must call a Flask API via the POST method to add a new comment. The new comment, associated with the specific video code, must be saved into the `comments.csv` file.

5. Create two APIs:
   * One to return all comments in JSON format.
   * One to return only the comments linked to a specific video.

6. Create a `/react` route on the Flask side to render the `index_react.html` template for a React Single Page Application (SPA). All React-specific routes must use the `/react` prefix (e.g., `/react/videos`, `/react/detail`).

7. Create a React component `VideoList` to display a table showing the code and name of each video. This component should be associated with the route `/react/videos`.

8. In the `VideoList` component, insert a form above the table to add a new video. The form should take the name and video link as input. The video code must be generated automatically on the backend within a specific Flask API that saves the new video to `video.csv`.
