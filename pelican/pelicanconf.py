from datetime import datetime

AUTHOR = "Kareem Skinner"
SITEURL = "https://karsteski.com"
SITENAME = "Karsteski Website"
SITETITLE = "A KaStSk Website"
SITESUBTITLE = "Test for website"
SITEDESCRIPTION = "website test"
# SITELOGO = ''
# FAVICON = '/images/favicon.ico'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

ROBOTS = "index, follow"

THEME = "./Flex"
PATH = "content"
OUTPUT_PATH = ".."
TIMEZONE = "Canada/Eastern"

DISABLE_URL_HASH = True

# PLUGIN_PATHS = ['pelican-plugins']

# PLUGINS = ['i18n_subsites']

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
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
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US",
}

# STATIC_PATHS = []
# EXTRA_PATH_META_DATA = {}


COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

DISQUS_SITENAME = None
ADD_THIS_ID = ""

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
