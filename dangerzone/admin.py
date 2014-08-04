# DangerZone Version 0.0.1
# Admin.py

import datetime
from flask import request, redirect

from flask_turboduck.admin import Admin, ModelAdmin, AdminPanel
from flask_turboduck.filters import QueryFilter

from app import app, db
from auth import auth
from models import User, Movie, Person, Cast


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
            'movie_list': Movie.select().order_by(Movie.created_date.desc()).paginate(1, 3)
        }


admin = Admin(app, auth, branding='DangerZone')


class MovieAdmin(ModelAdmin):
    columns = ('title', 'description', 'release', 'poster')
    exclude = ('created',)

class MessageAdmin(ModelAdmin):
    columns = ('user', 'content', 'pub_date',)
    foreign_key_lookups = {'user': 'username'}
    filter_fields = ('user', 'content', 'pub_date', 'user__username')


auth.register_admin(admin)
admin.register(Relationship)
admin.register(Message, MessageAdmin)
admin.register(Note, NoteAdmin)
admin.register_panel('Notes', NotePanel)
admin.register_panel('User stats', UserStatsPanel)