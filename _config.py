# -*- coding: utf-8 -*-

######################################################################
# This is the main Blogofile configuration file.
# www.Blogofile.com
######################################################################

######################################################################
# Basic Settings
#  (almost all sites will want to configure these settings)
######################################################################
## site_url -- Your site's full URL
# Your "site" is the same thing as your _site directory.
#  If you're hosting a blogofile powered site as a subdirectory of a larger
#  non-blogofile site, then you would set the site_url to the full URL
#  including that subdirectory: "http://www.yoursite.com/path/to/blogofile-dir"
site.url = "http://localhost:8080"

#### Blog Settings ####
blog = controllers.blog

## blog_enabled -- Should the blog be enabled?
#  (You don't _have_ to use blogofile to build blogs)
blog.enabled = True

## blog_path -- Blog path.
#  This is the path of the blog relative to the site_url.
#  If your site_url is "http://www.yoursite.com/~ryan"
#  and you set blog_path to "/blog" your full blog URL would be
#  "http://www.yoursite.com/~ryan/blog"
#  Leave blank "" to set to the root of site_url
blog.path = ""

## blog_name -- Your Blog's name.
# This is used repeatedly in default blog templates
blog.name = "mindtrove"

## blog_description -- A short one line description of the blog
# used in the RSS/Atom feeds.
blog.description = "Collecting ideas since 1980"

## blog_timezone -- the timezone that you normally write your blog posts from
blog.timezone = "US/Eastern"

blog.disqus.name = 'mindtrove'
blog.disqus.enabled = True
blog.post_excerpts.enabled = True
blog.post_excerpts.word_length = 25
blog.posts_per_page = 10