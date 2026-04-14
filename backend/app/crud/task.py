from app.models.task import Task

def create_task(db, task, user_id: int):
    db_task = Task(
        title=task.title,
        user_id=user_id
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task
