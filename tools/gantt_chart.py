import plotly.express as px
import pandas as pd

def create_gantt_chart(tasks, start_dates, end_dates, task_names):
    """
    Create a Gantt chart using Plotly.

    Args:
        tasks (list): List of task IDs
        start_dates (list): List of start dates for each task
        end_dates (list): List of end dates for each task
        task_names (list): List of task names

    Returns:
        fig (plotly.graph_objs.Figure): Gantt chart figure
    """
    df = pd.DataFrame({
        'Task': tasks,
        'Start': start_dates,
        'Finish': end_dates,
        'Task Name': task_names
    })

    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Task Name")
    fig.update_layout(title="Gantt Chart", xaxis_title="Date", yaxis_title="Task")

    return fig

def get_tasks_from_user():
    """
    Prompt user to input task IDs, start dates, end dates, and task names.

    Returns:
        tasks (list): List of task IDs
        start_dates (list): List of start dates for each task
        end_dates (list): List of end dates for each task
        task_names (list): List of task names
    """
    num_tasks = int(input("Enter the number of tasks: "))

    tasks = []
    start_dates = []
    end_dates = []
    task_names = []

    for i in range(num_tasks):
        task_id = input(f"Enter task ID {i+1}: ")
        start_date = input(f"Enter start date for task {i+1} (YYYY-MM-DD): ")
        end_date = input(f"Enter end date for task {i+1} (YYYY-MM-DD): ")
        task_name = input(f"Enter task name for task {i+1}: ")

        tasks.append(task_id)
        start_dates.append(start_date)
        end_dates.append(end_date)
        task_names.append(task_name)

    return tasks, start_dates, end_dates, task_names

def main():
    tasks, start_dates, end_dates, task_names = get_tasks_from_user()
    fig = create_gantt_chart(tasks, start_dates, end_dates, task_names)
    fig.show()

if __name__ == "__main__":
    main()
