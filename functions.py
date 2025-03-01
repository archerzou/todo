"""
todos.py

This module provides functionality to manage a to-do list. It allows
users to add, remove, and display tasks stored in a text file.
"""

FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items."""
    with open(filepath, "r", encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todos_arg)

if __name__ == '__main__':
    print('Hello world')
