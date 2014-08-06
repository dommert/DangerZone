# DangerZone Version 0.0.1
# Admin.py

import datetime
from flask import request, redirect
# TurboDuck
from flask_turboduck.admin import Admin, ModelAdmin, AdminPanel
from flask_turboduck.auth import BaseUser
from flask_turboduck.filters import QueryFilter
# DangerZone
from app import app, db
from auth import auth
from models import Movie, Person, Cast, User


admin = Admin(app, auth, branding='DangerZone')
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

class UserStatsPanel(AdminPanel):
    template_name = 'admin/user_stats.html'

    def get_context(self):
        last_week = datetime.datetime.now() - datetime.timedelta(days=7)
        signups_this_week = User.select().where(User.join_date > last_week).count()
        messages_this_week = Message.select().where(Message.pub_date > last_week).count()
        return {
            'signups': signups_this_week,
            'messages': messages_this_week,
        }


# --------- Admin --------------
# create a modeladmin for it
class UserAdmin(ModelAdmin):
    columns = ('username', 'email',)

    # Make sure the user's password is hashed, after it's been changed in
    # the admin interface. If we don't do this, the password will be saved
    # in clear text inside the database and login will be impossible.
    def save_model(self, instance, form, adding=False):
        orig_password = instance.password

        user = super(UserAdmin, self).save_model(instance, form, adding)

        if orig_password != form.password.data:
            user.set_password(form.password.data)
            user.save()

        return user


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
admin.register(User, UserAdmin)
admin.register(Movie, MovieAdmin)
admin.register(Person, PersonAdmin)
admin.register(Cast)

# Register AdminPanels
admin.register_panel('Movie', MoviePanel)
admin.register_panel('User Stats', UserStatsPanel)

admin.setup()
