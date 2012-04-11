from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'My New App'
settings.subtitle = 'powered by web2py'
settings.author = 'you'
settings.author_email = 'do.robert@gmail.com'
settings.keywords = ''
settings.description = ''
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '60876f23-d379-4132-9324-9fd168b7873a'
settings.email_server = 'localhost'
settings.email_sender = 'you@example.com'
settings.email_login = ''
settings.login_method = 'local'
settings.login_config = ''
settings.plugins = []
