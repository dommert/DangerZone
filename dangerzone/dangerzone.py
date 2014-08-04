# DangerZone V0.0.1
# Example Movie-Actor App

# Creates a admin user
from auth import auth

auth.User.create_table(fail_silently=True)  # make sure table created.
admin = auth.User(username='admin', email='', admin=True, active=True)
admin.set_password('admin')
admin.save()