import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

# get long_description from docs/index.txt
#f = open(os.path.join(
#    os.path.dirname(os.path.abspath(__file__)), 'docs', 'index.txt'))
#long_description = f.read().strip()
#long_description = long_description.split('split here', 1)[1]
#f.close()

setup(
    name='pyfisheyes',
    version='0.1',
    description='Site System Operatein Data Analysis',
#    long_description=long_description,
#    Mako 0.4.1
    author='tonycai',
    author_email='tonycai321@gmail.com',
    url='http://tonynotes.com',
    install_requires=[
        "Pylons>=1.0",
        "SQLAlchemy==0.5.8",
        "Mako>=0.2.2,<=0.4.1",
        "FormBuild>=2.0.1,<=2.0.99",
        "AuthKit>=0.4.3,<=0.4.99",
        "textile>=2.1.4",
        "TurboMail>=3.0.3",
        "gp.fileupload>=1.0,<=1.0.99",        
    ],
    setup_requires=["PasteScript>=1.6.3"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'pyfisheyes': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors={'pyfisheyes': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', {'input_encoding': 'utf-8'}),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    keywords='pylons wsgi site system data analysis for ops-team',
    license='BSD',
    entry_points="""
    [paste.app_factory]
    main = pyfisheyes.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller

    [paste.filter_app_factory]
    gzip = pyfisheyes.lib.middleware:make_gzip_middleware

    [paste.filter_factory]
    gzip = pyfisheyes.lib.middleware:make_gzip_middleware_filter
    """,
    extras_require = {
        'MySQL': ["mysql-python>=1.2"],
        'PostgreSQL': ["psycopg2"],
    },

)
