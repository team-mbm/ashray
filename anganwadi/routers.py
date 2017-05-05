class child_labour_router(object):

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'anganwadi':
            return 'anganwadi'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'anganwadi':
            return 'anganwadi'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'anganwadi':
            return db == 'anganwadi'
        elif db == 'anganwadi':
            return False
        return False
