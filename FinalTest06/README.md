# Final Test 06

![Page 1]()
![Page 2]()
![React 1]()
![React 2]()

## Description
1. Write two functions to read and return all quizzes from the `quizzies.csv` file and all questions from the `questions.csv` file. The `questions.csv` file includes code, statement, four answers, and a list of correct answer indices. The `quizzies.csv` file includes code, name, and a list of question codes. These functions must be called in `app.py`, and file loading must be implemented in a single part of the code.

2. Modify the `/index` route to render an `index.html` template that extends the base template. The template should display a table of available quizzes. If no quizzes are found, show an appropriate message.

3. Make each quiz name clickable. When a user clicks on a quiz, redirect them to a dedicated page `/quiz/<quiz_code>` that shows the details of the quiz, including the list of questions associated with it, formatted clearly.

4. On the quiz detail page, implement the functionality to visualize the questions. Each question must display its statement and the four possible answers.

5. Create two APIs:
   * One to return all questions in JSON format.
   * One to return the details of a specific quiz and its associated questions based on the quiz code.

6. Create a `/react` route on the Flask side to render the `index_react.html` template for a React Single Page Application (SPA). All React-related routes must follow the `/react` prefix (e.g., `/react/questions`, `/react/new_questions`).

7. Create a React component `QuestionList` to display the list of all possible questions in a table showing the code and statement for each. This component must also include an "Add Question" button and be associated with the `/react` route.

8. The "Add Question" button must navigate to a `NewQuestion` component under the route `/react/new_questions`. This component should contain a form to add a new question, allowing the user to input the statement, the four answers, and specify which ones are correct. The new question must be saved into the `questions.csv` file.
