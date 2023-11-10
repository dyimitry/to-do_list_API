from notification.producer import get_tasks_status_false
from notification.tasks import worker

# нужен список задач producer
result = get_tasks_status_false()
for task in result:
    worker.apply_async(args=(task,))
    # result = worker.delay(task)
