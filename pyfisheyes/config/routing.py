"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('home', '/', controller='home', action='index')
    
    map.connect('signout', '/signout', controller='account', action='signout')
    map.connect('signin', '/signin', controller='account', action='signin')
    map.connect('signinagain', '/signinagain', controller='account', action='signinagain')

    map.connect('template', '/template', controller='categories', action='index')
    map.connect('events', '/events', controller='events', action='list')
    map.connect('alert', '/alert', controller='alert', action='list')
    map.connect('contacts', '/contacts', controller='contacts', action='list')
    map.connect('devices', '/devices', controller='devices', action='list')
    map.connect('logstuffshow', '/logstuffshow', controller='logstuffshow', action='index')
    map.connect('speed', '/speed', controller='speed', action='index')
    
    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')
    
    map.connect('/{controller}/{action}/{id}/{page}')
   
    map.connect('/{controller}/{action}/{id}/{item}/{hostname}/{date1}/11.png')
    
    map.connect('/{controller}/{action}/{tid}/{datei}/{timei}')
   
    map.connect('/{controller}/{action}/{id}/{page}/{date}/{date2}')
    
    map.connect('/{controller}/{action}/{id}/{opt}/{date}/{date2}/1.png')
    #map.connect('/{controller}/{action}/{id}/{d}/1.png')
    map.connect('/{controller}/{action}/{id}/{opt}/{date}/{fsize}/2.png')
    map.connect('/{controller}/{action}/{id}/{dname}/{ditem}/{maxvalue}/12.png')
    
    #map.connect('/{controller}/{action}/{dname}')

    return map
