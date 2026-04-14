from app.models.task import Task

# 作成
def create_task(db, task, user_id: int):
    db_task = Task(
        title=task.title,
        #user_id=user_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


# 取得（これが重要）
def get_tasks(db, user_id: int):
    return db.query(Task).filter(Task.user_id == user_id).all()
