# Django Task Management Application

This is a Django-based application to manage tasks, employees, and projects. It allows users to create, read, update, and delete tasks, employees, and projects, as well as calculate task delays based on specified start and end dates.

## Models

### Employee
Represents an employee in the system.
- `first_name`: The first name of the employee (CharField).
- `last_name`: The last name of the employee (CharField).

### Project
Represents a project in the system.
- `name`: The name of the project (CharField).

### Task
Represents a task assigned to an employee within a project.
- `id_employee`: Foreign key linking to an `Employee`.
- `id_project`: Foreign key linking to a `Project`.
- `description`: A description of the task (CharField).
- `date_start`: The start date of the task (DateField).
- `estimate_time`: The estimated time to complete the task in days (IntegerField).
- `status`: The status of the task (CharField).

## Views

### `index`
Handles the generation of a task report based on a date range and task status.

#### Method: `POST`
- Expects `date_start` and `date_end` as form data.
- Converts the dates from strings to `datetime.date` objects.
- Retrieves tasks with status 'In Progress' and start dates within the specified range.
- Calculates the estimated end date and delay for each task.
- Renders the tasks in the `index.html` template.

### `employee`
Handles creating and listing employees.

#### Method: `POST`
- Creates a new employee using `first_name` and `last_name` from form data.
- Renders the list of employees in the `empleados.html` template.

### `project`
Handles creating and listing projects.

#### Method: `POST`
- Creates a new project using `name` from form data.
- Renders the list of projects in the `proyectos.html` template.

### `task`
Handles creating and listing tasks.

#### Method: `POST`
- Creates a new task using `description`, `date_start`, `estimate_time`, `status`, `employee_id`, and `project_id` from form data.
- Renders the list of tasks, employees, and projects in the `tareas.html` template.

### `delete_employee`
Handles deleting an employee.

#### Method: `GET`
- Deletes an employee by `id`.
- Renders the updated list of employees in the `empleados.html` template.

### `delete_project`
Handles deleting a project.

#### Method: `GET`
- Deletes a project by `id`.
- Renders the updated list of projects in the `proyectos.html` template.

### `delete_task`
Handles deleting a task.

#### Method: `GET`
- Deletes a task by `id`.
- Renders the updated list of tasks, employees, and projects in the `tareas.html` template.

### `update_task`
Handles updating a task.

#### Method: `POST`
- Updates a task by `id` using form data.
- Renders the updated list of tasks, employees, and projects in the `tareas.html` template.

### `update_employee`
Handles updating an employee.

#### Method: `POST`
- Updates an employee by `id` using form data.
- Renders the updated list of employees in the `empleados.html` template.

### `update_project`
Handles updating a project.

#### Method: `POST`
- Updates a project by `id` using form data.
- Renders the updated list of projects in the `proyectos.html` template.

## Templates

### `index.html`
Displays a form to input `date_start` and `date_end` for generating task reports and displays the results in a table format.

### `empleados.html`
Displays a list of employees and a form to add new employees.

### `proyectos.html`
Displays a list of projects and a form to add new projects.

### `tareas.html`
Displays a list of tasks, employees, and projects and a form to add new tasks.

### `edit_task.html`
Displays a form to edit an existing task.

### `edit_employee.html`
Displays a form to edit an existing employee.

### `edit_project.html`
Displays a form to edit an existing project.

## Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/task-management-app.git
    cd task-management-app
    ```

2. Create a virtual environment and install dependencies:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Apply database migrations:
    ```sh
    python manage.py migrate
    ```

4. Run the development server:
    ```sh
    python manage.py runserver
    ```

5. Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
