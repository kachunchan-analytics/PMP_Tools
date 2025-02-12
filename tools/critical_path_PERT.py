import networkx as nx
import matplotlib.pyplot as plt

def create_project_network():
    """
    Create a directed graph representing the project network.

    Returns:
    G (networkx.DiGraph): Directed graph representing the project network
    """
    while True:
        try:
            print("Enter the tasks (separated by commas):")
            print("For example, if you have tasks A, B, and C, enter 'A, B, C'.")
            tasks = input().split(',')
            tasks = [task.strip() for task in tasks]
            if not tasks:
                raise ValueError("No tasks entered")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    G = nx.DiGraph()
    G.add_nodes_from(tasks)

    while True:
        try:
            print("Enter the dependencies (in the format 'task_id dependent_task_id relationship', separated by commas):")
            print("For example, if task A has a Finish-to-Start (FS) dependency with task B, enter 'A B FS'.")
            print("If task C has a Start-to-Start (SS) dependency with task D, enter 'C D SS'.")
            print("If task E has a Finish-to-Finish (FF) dependency with task F, enter 'E F FF'.")
            dependencies = input().split(',')
            dependencies = [tuple(dependency.split()) for dependency in dependencies]
            if not dependencies:
                raise ValueError("No dependencies entered")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

    for dependency in dependencies:
        G.add_edge(dependency[0], dependency[1])

    # Allow multiple dependencies per task
    while True:
        print("Do you want to add more dependencies? (yes/no)")
        response = input().lower()
        if response == 'yes':
            while True:
                try:
                    print("Enter the additional dependencies (in the format 'task_id dependent_task_id relationship', separated by commas):")
                    additional_dependencies = input().split(',')
                    additional_dependencies = [tuple(dependency.split()) for dependency in additional_dependencies]
                    if not additional_dependencies:
                        raise ValueError("No additional dependencies entered")
                    break
                except ValueError as e:
                    print(f"Error: {e}. Please try again.")
            for dependency in additional_dependencies:
                G.add_edge(dependency[0], dependency[1])
        elif response == 'no':
            break
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

    return G


def calculate_critical_path(G):
    """
    Calculate the critical path using the CPM method.

    Args:
    G (networkx.DiGraph): Directed graph representing the project network

    Returns:
    critical_path (list): List of task IDs in the critical path
    """
    critical_path = []
    for node in nx.topological_sort(G):
        if nx.out_degree(G, node) == 0:
            critical_path.append(node)
    return critical_path

def calculate_task_durations():
    """
    Get task durations from the user.

    Returns:
    task_durations (dict): Dictionary of task durations, where each key is a task ID and each value is the duration
    """
    while True:
        try:
            print("Enter the task durations (in the format 'task_id duration', separated by commas):")
            print("For example, if task A has a duration of 5 days, enter 'A 5'.")
            task_durations_input = input().split(',')
            task_durations = {}
            for task_duration in task_durations_input:
                task, duration = task_duration.split()
                task_durations[task] = int(duration)
            if not task_durations:
                raise ValueError("No task durations entered")
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
    return task_durations

def calculate_earliest_start_time(G, task_durations):
    """
    Calculate the earliest start time for each task using the CPM method.

    Args:
    G (networkx.DiGraph): Directed graph representing the project network
    task_durations (dict): Dictionary of task durations, where each key is a task ID and each value is the duration

    Returns:
    earliest_start_times (dict): Dictionary of earliest start times, where each key is a task ID and each value is the earliest start time
    """
    earliest_start_times = {}
    for node in nx.topological_sort(G):
        earliest_start_time = 0
        for predecessor in G.predecessors(node):
            earliest_start_time = max(earliest_start_time, earliest_start_times[predecessor] + task_durations[predecessor])
        earliest_start_times[node] = earliest_start_time
    return earliest_start_times

def calculate_latest_finish_time(G, task_durations, earliest_start_times):
    """
    Calculate the latest finish time for each task using the CPM method.

    Args:
    G (networkx.DiGraph): Directed graph representing the project network
    task_durations (dict): Dictionary of task durations, where each key is a task ID and each value is the duration
    earliest_start_times (dict): Dictionary of earliest start times, where each key is a task ID and each value is the earliest start time

    Returns:
    latest_finish_times (dict): Dictionary of latest finish times, where each key is a task ID and each value is the latest finish time
    """
    latest_finish_times = {}
    for node in nx.topological_sort(G)[::-1]:
        latest_finish_time = float('inf')
        for successor in G.successors(node):
            latest_finish_time = min(latest_finish_time, latest_finish_times[successor] - task_durations[node])
        latest_finish_times[node] = latest_finish_time
    return latest_finish_times

def calculate_slack_time(earliest_start_times, latest_finish_times, task_durations):
    """
    Calculate the slack time for each task using the CPM method.

    Args:
    earliest_start_times (dict): Dictionary of earliest start times, where each key is a task ID and each value is the earliest start time
    latest_finish_times (dict): Dictionary of latest finish times, where each key is a task ID and each value is the latest finish time
    task_durations (dict): Dictionary of task durations, where each key is a task ID and each value is the duration

    Returns:
    slack_times (dict): Dictionary of slack times, where each key is a task ID and each value is the slack time
    """
    slack_times = {}
    for task in earliest_start_times:
        slack_time = latest_finish_times[task] - earliest_start_times[task] - task_durations[task]
        slack_times[task] = slack_time
    return slack_times

def plot_project_network(G):
    """
    Plot the project network diagram.

    Args:
    G (networkx.DiGraph): Directed graph representing the project network
    """
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=12)
    plt.show()

def main():
    G = create_project_network()
    task_durations = calculate_task_durations()
    critical_path = calculate_critical_path(G)
    earliest_start_times = calculate_earliest_start_time(G, task_durations)
    latest_finish_times = calculate_latest_finish_time(G, task_durations, earliest_start_times)
    slack_times = calculate_slack_time(earliest_start_times, latest_finish_times, task_durations)

    print("Critical Path:", critical_path)
    print("Earliest Start Times:", earliest_start_times)
    print("Latest Finish Times:", latest_finish_times)
    print("Slack Times:", slack_times)

    plot_project_network(G)

if __name__ == "__main__":
    main()
