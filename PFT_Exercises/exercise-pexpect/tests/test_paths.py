class HappyPath:
    questions = ('Installation path \[\/opt\/esconfs\]:',
                 'Full or light installation \[Full\/Light\]:',
                 'Deploy web server  \[Y\/N\]:',
                 'On which port \[80\]:',
                 'Admin user account \[admin\]:',
                 'Admin acount password \[\]:',
                 'Backup previous data \[Y\/N\]:',
                 'Backup path \[~\/esconfs_backup\/\]:',
                 'Install with these setting \[Y\/N\]:')

    answers = ('/opt/esconfs',
               'Full',
               'Y',
               '80',
               'admin',
               'secret',
               'Y',
               '\n',
               'Y')


class UnhappyPath:
    questions = ('Installation path \[\/opt\/esconfs\]:',
                 'Full or light installation \[Full\/Light\]:',
                 'Deploy web server  \[Y\/N\]:',
                 'On which port \[80\]:',
                 'Admin user account \[admin\]:',
                 'Admin acount password \[\]:',
                 'Backup previous data \[Y\/N\]:',
                 'Backup path \[~\/esconfs_backup\/\]:',
                 'Install with these setting \[Y\/N\]:')

    answers = ('/opt/esconfs',
               'Full',
               'Y',
               '8080',
               'admin',
               'secret',
               'Y',
               '\n',
               'Y')
