
# class cases_router(object):
#
#     def db_for_read(self, model, **hints):
#         if model._meta.app_label == 'cases':
#             return 'default'
#         return None
#
#     def db_for_write(self, model, **hints):
#         if model._meta.app_label == 'cases':
#             return 'default'
#         return None
#
#     def allow_relation(self, obj1, obj2, **hints):
#         return None
#
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         print("hello")
#         if app_label == 'cases':
#             return db == 'default'
#         elif db == 'default':
#             return False
#         return False
from django.conf import settings
class cases_router(object):

    def db_for_read(self, model, **hints):
        return settings.DB_Mapping.get(model._meta.app_label, 'default')

    def db_for_write(self, model, **hints):
        return settings.DB_Mapping.get(model._meta.app_label, 'default')

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label in settings.DB_Mapping.keys() or db in settings.DB_Mapping.values():
            return True
        else:
            return None
