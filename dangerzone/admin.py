# DangerZone Version 0.0.1
# Admin.py

import datetime
from flask import request, redirect
# TurboDuck
from flask_turboduck.admin import Admin, ModelAdmin, AdminPanel
from flask_turboduck.filters import QueryFilter
# DangerZone
from app import app, db
import auth
from models import Movie, Person, Cast, User


# ------- Panels ------------

# Movie Panel
class MoviePanel(AdminPanel):
    template_name = 'admin/movie.html'

    def get_urls(self):
        return (
            ('/create/', self.create),
        )

    def create(self):
        if request.method == 'POST':
            if request.form.get('message'):
                Movie.create(
                    title=request.form['title'],
                    release=request.form['release'],
                    description=request.form['description'],
                    poster=request.form['poster']
                )
        next = request.form.get('next') or self.dashboard_url()
        return redirect(next)

    def get_context(self):
        return {
            'movie_list': Movie.select().order_by(Movie.created.desc()).paginate(1, 3)
        }

admin = Admin(app, auth, branding='DangerZone')

# --------- Admin --------------

# Person Admin
class PersonAdmin(ModelAdmin):
    columns = ('fname', 'lname', 'sex',)
    exclude = ('created',)


# Movie Admin
class MovieAdmin(ModelAdmin):
    columns = ('title', 'description', 'release', 'poster')
    exclude = ('created',)



#auth.register_admin(admin)
# Register Admin
admin.register(Movie, MovieAdmin)
admin.register(Person, PersonAdmin)
admin.register(Cast)
#admin.register(User)

# Register AdminPanels
admin.register_panel('Movie', MoviePanel)

