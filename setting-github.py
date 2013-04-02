# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zhs'

SITENAME = "Beauties are the creator of beauties"
AUTHOR = 'TonyHo'

DISQUS_SITENAME = 'tonyhoblog'
GITHUB_URL = '<http://tonyho.github.io>'#github链接
SITEURL = '<http://tonyho.github.com>'
GOOGLE_ANALYTICS = 'UA-30756331-1'#谷歌站点分析
TAG_FEED_ATOM  = 'feeds/%s.atom.xml'

DEFAULT_PAGINATION = 10#默认每一页有多少篇文章

DEFAULT_CATEGORY ='misc'
OUTPUT_PATH = '.'
#需要把输出路径从默认的'output'改成根目录(your_id.github.com目录), 因为githubpage需要把index.html上传到repo的master分支的根目录才可以!
PATH = 'posts'#这个是指定放置.md/.rst文件的目录

LINKS = (('dofine', '<http://www.dofine.me>'),
         ('farseerfc', "<http://farseerfc.github.com/>"),
         )#友情链接~

SOCIAL = (
          ('github', '<http://github.com/tonyho>'),
          )#社交网络链接
          #~ ('twitter', '<http://twitter.com/farseerfc>'),
          #~ ('facebook', '<http://www.facebook.com/farseerfc>'),
          #~ ('weibo', '<http://weibo.com/farseerfc>'),
          #~ ('renren', '<http://www.renren.com/farseer>'),

#这个是farseerfc同学自己加的, 可以显示他的新浪微博内容, 有微博的话可以把这些加上~
#~ TWITTER_USERNAME = 'farseerfc'
#~ SIDEBAR_CUSTOM = r"""
#~ <li class="nav-header"><h4><i class="icon-list-alt"></i>Weibo</h4></li>
#~ <iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" 
#~ src="<http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=1&ptype=1&speed=0&skin=2&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1862842353&verifier=b193b9de&dpc=1>">
#~ </iframe>
#~ """

#google自定义搜索(大概是站内搜索吧)
#~ GOOGLE_CUSTOM_SEARCH_SIDEBAR = "001578481551708017171:axpo6yvtdyg"
#~ GOOGLE_CUSTOM_SEARCH_NAVBAR = "001578481551708017171:hxkva69brmg"
# how to make html :
# 1. Clone and Install the theme : 
#	https://github.com/CNBorn/pelican-themes
#	pelican-themes -i /download_dir/pelican-themes/cnborn/
# 2. pelican -s setting-github.py -t bootstrap 
