from datetime import datetime

AUTHOR = "Kareem Skinner"
SITEURL = "http://localhost:8000"
SITENAME = "Karsteski.com"
SITETITLE = "Kareem Skinner"
SITESUBTITLE = "Programmer. B.Sc. Chemistry"
SITEDESCRIPTION = "Kareem Skinner's personal website and blog :)"
SITELOGO = SITEURL + "/images/profile-picture.jpg"
FAVICON = SITEURL + "/images/favicon.ico"
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

STATIC_PATHS = ['images/about', 'images']

# ROBOTS = "index, follow"

THEME = "./Flex"
PATH = "content"
OUTPUT_PATH = "../"
TIMEZONE = "Canada/Eastern"

DISABLE_URL_HASH = True

DEFAULT_LANG = "en"
LOCALE = "en_CA"

DATE_FORMATS = {
    "en_CA": "%d %B, %Y",
}

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

SOCIAL = (
    ("github", "https://github.com/Karsteski"),
    ("linkedin", "https://www.linkedin.com/in/kareemskinner/")
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html")
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_CA",
}

# EXTRA_PATH_META_DATA = {}


COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

DISQUS_SITENAME = None
ADD_THIS_ID = ""
THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

# For testing purposes. Uses .less instead .css
USE_LESS = False
