from redminelib import Redmine
from redminesetup import *

redmine = Redmine(REDMINE_URL, key=API_KEY, version=VERSION)
for project in redmine.project.all():
    print(project.name)
