'''
Make a task list with the following options: "add a task", "list the tasks", "undo option" (each time we call, this operation must undo the last action); "redo option" (each time we call, this operation must redo the last action)

[task1 , task2]
[task1] < - undo
[task, task2] < - redo

'''


def show_op(all_list):
    if not all_list:
        print('There is no task to list.')
        return

    print('Tasks: ')
    print()
    for i in all_list:
        print(i)
    print()

def do_undo(all_list, redo_list):
    if not all_list:
        print('There is no task to undo.')
        return
    
    task = all_list.pop()
    redo_list.append(task)
    print(f'The task {task} was removed from task list.')
    print()

def do_redo(all_list, redo_list):
    if not redo_list:
        print('There is no task to redo.')
        return
    
    task = redo_list.pop()
    all_list.append(task)

    print(f'The task {task} was added in task list.')

def do_add(task, all_list):
    task = task.strip()

    if not task:
        print('You dont type a task.')
        return

    all_list.append(task)
    print(f'You add {task} to your Task List.')


if __name__ == '__main__':
    all_list = []
    redo_list = []

    while True:
        print('Commands: Undo, Redo, and List')
        task = input('Type a task or [undo, redo, ls]: ')

        if task == 'ls':
            show_op(all_list)
            continue
        elif task == 'undo':
            do_undo(all_list, redo_list)
            continue
        elif task == 'redo':
            do_redo(all_list, redo_list)
            continue
    
        do_add(task, all_list)