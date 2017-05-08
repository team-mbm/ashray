
class child_labour_router(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'child_labour_association':
            return 'child_labour_association'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'child_labour_association':
            return 'child_labour_association'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'child_labour_association':
            return db == 'child_labour_association'
        elif db == 'child_labour_association':
            return False
        return False
