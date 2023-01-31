from app import app
from config import db
from routes import app_route,functions

app.app_context().push()
db.create_all()

app_route.index()
app_route.add()
app_route.delete()
app_route.get_id()
app_route.update_user()

functions.add_user()
functions.get_all()
functions.get_user_by_id(id)
functions.delete_user()
functions.update()

if (__name__ == '__main__'):
    app.run()