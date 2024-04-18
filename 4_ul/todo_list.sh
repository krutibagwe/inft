#!/bin/bash

TODO_FILE="todo_list.txt"

# Display usage instructions
usage() {
    echo "Usage: $0 [option] [argument]"
    echo "Options:"
    echo "  add     <task>     Add a new task"
    echo "  remove  <task#>    Remove a task"
    echo "  list               List all tasks"
    echo "  help               Display usage"
}

# Add a new task
add_task() {
    task="$*"
    echo "$task" >> "$TODO_FILE"
    echo "Task added: $task"
}

# Remove a task
remove_task() {
    task_number="$1"
    sed -i "${task_number}d" "$TODO_FILE"
    echo "Task $task_number removed"
}

# List all tasks
list_tasks() {
    echo "To-Do List:"
    nl -w2 -s') ' "$TODO_FILE"
}

# Main script logic with if-else
if [ "$1" == "add" ]; then
    shift
    add_task "$*"
elif [ "$1" == "remove" ]; then
    shift
    remove_task "$1"
elif [ "$1" == "list" ]; then
    list_tasks
elif [ "$1" == "help" ] || [ -z "$1" ]; then
    usage
else
    echo "Invalid option. Use '$0 help' for usage."
fi
