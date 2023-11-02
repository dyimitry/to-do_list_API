from cele.producer import get_tasks_status_false
from cele.tasks import worker

# нужен список задач producer

result = get_tasks_status_false()
for task in result:
    worker(task)
