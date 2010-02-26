from repoze.bfg.configuration import Configurator
from repoze.zodbconn.finder import PersistentApplicationFinder
from rfd.models import appmaker

def app(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
    zodb_uri = settings.get('zodb_uri')
    zcml_file = settings.get('configure_zcml', 'configure.zcml')
    if zodb_uri is None:
        raise ValueError("No 'zodb_uri' in application configuration.")

    finder = PersistentApplicationFinder(zodb_uri, appmaker)
    def get_root(request):
        return finder(request.environ)
    config = Configurator(root_factory=get_root, settings=settings)
    config.begin()
    config.load_zcml(zcml_file)
    config.end()
    return config.make_wsgi_app()
