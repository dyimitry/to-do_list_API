from cele.producer import get_tasks_status_false
from cele.worker import worker

# нужен список задач producer
result = get_tasks_status_false()
for i in result:
    print(worker(i))