tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def mark_done(index):
    tasks[index]["done"] = True

def show_tasks():
    for i, t in enumerate(tasks):
        status = "Done" if t["done"] else "Pending"
        print(f"{i + 1}. {t['task']} - {status}")

add_task("Finish assignment")
add_task("Learn Git")
mark_done(0)
show_tasks()
