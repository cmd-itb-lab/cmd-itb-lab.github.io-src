#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'cmd-itb-lab'
SITENAME = 'CMD ITB LAB'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('ITB', 'https://itb.ac.id/'),
         ('Teknik Fisika ITB', 'http://python.org/'),
        )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DELETE_OUTPUT_DIRECTORY = True

#DEFAULT_PAGINATION = 1

#USE_FOLDER_AS_CATEGORY = True

# Name your content directory posts
#ARTICLE_PATHS = ['posts']

#ARTICLE_URL = 'blog/{slug}/'
#ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
#ARTICLE_ORDER_BY = 'date'

MENUITEMS = (
  ('Home', '/'),
  ('Contact', '/contact.html'),
  ('Members', '/members.html'),
  ('Research', '/research-topics.html'),
  ('Publications', '/publications.html'),  
)

DISPLAY_PAGES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['html', 'images']

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ["render_math"]