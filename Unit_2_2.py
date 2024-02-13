def maxTasks(tasks,workers,pills, trength):
    tasks.sort(reverse=True)
    workers.sort(reverse=True)
    tasks_completed=0
    used_workers=[False]*len(workers)
    for task_strength in tasks:
        for i,worker_strength in enumerate(workers):
            if not used_workers[i] and worker_strength>=task_strength:
                tasks_completed+=1
                used_workers[i]=True
                break
    for i, worker_strength in enumerate(workers):
        if not used_workers[i] and pills>0:
            if worker_strength+strength>=tasks[-1]:
                tasks_completed+=1
                pills-=1
    return tasks_completed
tasks=[3,5,7,10]
workers=[10,7,5,3]
pills=2
strength=2
print("\nMaximum number of tasks completed = ",maxTasks(tasks,workers,pills,strength))