#/var/www/confgen/confgen.wsgi
#!/usr/bin/python
import sys
sys.path.insert(0,"/var/www/sleibo/") #Dadurch findet Python die App im PATH

from webseite import app as application