# Mini Task Tracker

A menu-based Python program that manages a to-do list and saves it to a JSON file, so tasks are still there the next time the program runs.

Built for AI Engineering, Week 1, Day 2.

## Features

- **Add** a task (stored as Pending)
- **View** a numbered list showing Pending or Done
- **Complete** a task by its number
- **Delete** a task by its number
- **Save and load**: tasks are saved to `tasks.json` with `json.dump()` after every change and loaded with `json.load()` at startup
- **Error handling**: empty titles, invalid menu choices, invalid task numbers, and a missing (or unreadable) `tasks.json`

## How to run

### In Google Colab
1. Upload `mini_task_tracker.py` using the Files panel on the left.
2. In a code cell, run:
   ```python
   %run mini_task_tracker.py
   ```
3. Type your choices in the input box under the cell.

Note: Colab files are temporary. To keep `tasks.json`, download it or save it to Google Drive. To test reloading, run the program again in the same active runtime.

### On your computer
```
python mini_task_tracker.py
```

## Sample session

```
--- TASK TRACKER ---
1. Add
2. View
3. Complete
4. Delete
5. Exit
Choice: 1
Task title: Read notes
Task added.
Choice: 2
1. Read notes [Pending]
Choice: 3
Task number: 1
Task completed.
Choice: 2
1. Read notes [Done]
```

## Files

- `mini_task_tracker.py`: the complete program
- `tasks.json`: created automatically when the first task is saved
