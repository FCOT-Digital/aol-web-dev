# 18 - Create records

* Create new records in a database so that your web app can store information.
* Update records in a database so that your web app can change information.
* Continue to use AI coding tools in a responsible and efficient manner.

---

## Predict & Run

1. Open these files in your editor:
    * [18_resource_signup.py](../webdev/18_resource_signup.py)
    * [18_signup.html](../webdev/static/18_signup.html)
    * [18_signup.js](../webdev/static/18_signup.js)
1. What will this code do?
    * *Your answer here.*
1. Run the code in Python.
1. How did you check it had worked?
    * *Your answer here.*
1. Was your prediction correct?
    * *Your answer here.*

---

## Inspect

1. Look at lines 6 & 7 of [18_resource_signup.py](../webdev/18_resource_signup.py). What, exactly, does each line do?
    * *Your answer here.*
1. Outline each step of the flow of data from the user to the database. Include filenames and line numbers in your answer.
    1. The user knows their email and what they'd like to be called. They enter this information into the form on the webpage. (18_signup.html:12-20)
    * *Keep going...*
1. Outline each step of the flow of data from the database to the user. Include filenames and line numbers in your answer.
    * *Your answer here.*

---

## Debug

1. What tool can you use to work out whether the data is being sent to the server correctly?
    * *Your answer here.*
1. For each of the steps in your data flow, add a line of code that will print out the data at that point in the flow. This is a common way of debugging a multi-stage process.

---

## Adapt

1. Research how to update a record in a database using SQL.
    * *The SQL command to update a record*
    * *The HTML method to update a record*
1. Add another form so that a user can update their `given_name` if they know their `email`. You will need to add a new route to your Flask app, and a new function to handle the update. You will also need to add a new HTML form and JavaScript code to send the update request to the server.