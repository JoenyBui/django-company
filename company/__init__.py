__title__ = 'Django Company'
__version__ = '1.0.0'
__author__ = 'Joeny Bui'
__copyright__ = 'Copyright 2011-2016 Joeny Bui'

# Version synonym
VERSION = __version__


USER_COMPANY_ADMIN = 0
USER_WORKER = 1
USER_READONLY = 2
USER_NONE = 3

USER_PRIVELAGE = ((USER_COMPANY_ADMIN, 'Administrated Access'),
                  (USER_WORKER, 'Write Access'),
                  (USER_READONLY, 'View Access'),
                  (USER_NONE, 'No Access'))
