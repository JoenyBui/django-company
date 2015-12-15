USER_COMPANY_ADMIN = 0
USER_WORKER = 1
USER_READONLY = 2
USER_NONE = 3

USER_PRIVELAGE = ((USER_COMPANY_ADMIN, 'Administrated Access'),
                  (USER_WORKER, 'Write Access'),
                  (USER_READONLY, 'View Access'),
                  (USER_NONE, 'No Access'))
