class MyAppRouter:
    def db_for_read(self, model, **hints):
        """
        Attempts to read models go to mysql database if available.
        """
        try:
            # Try to connect to the MySQL database
            with connections['mysql'].cursor() as cursor:
                return 'mysql'
        except OperationalError:
            # Fallback to the default database (SQLite)
            return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write models go to mysql database if available.
        """
        try:
            # Try to connect to the MySQL database
            with connections['mysql'].cursor() as cursor:
                return 'mysql'
        except OperationalError:
            # Fallback to the default database (SQLite)
            return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the same database.
        """
        db_list = ('default', 'mysql')
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that all models end up in the right database.
        """
        return True
