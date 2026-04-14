from app.db.session import engine
from app.models import task, user

task.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)
