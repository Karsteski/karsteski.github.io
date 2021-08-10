import os
import sys

sys.path.append(os.curdir)

try:
    from pelicanconf import *
except ImportError:
    sys.path.append(os.path.join(os.curdir, "docs"))
    from pelicanconf import *

SITEURL = "https://www.karsteski.com"

SITELOGO = SITEURL + "/images/profile-picture.jpg"
FAVICON = SITEURL + "/images/favicon.ico"

RELATIVE_URLS = False
