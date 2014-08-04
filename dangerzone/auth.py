# DangerZone Version 0.0.1
# Auth.py

from flask_turboduck.admin import Admin

admin = Admin(app, auth)
# Register Admin Sections
admin.register(Movie) # Movies Class
admin.register(Person) # People Class
admin.register(Cast) # Cast

admin.setup()