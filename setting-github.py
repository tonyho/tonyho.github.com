# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zhs'

SITENAME = "美是美的创造者"
AUTHOR = 'TonyHo'

DISQUS_SITENAME = 'tonyhoblog'
GITHUB_URL = 'http://tonyho.github.io'#github链接
SITEURL = 'http://tonyho.github.io'
GOOGLE_ANALYTICS = 'UA-54180446-1'#谷歌站点分析
TAG_FEED_ATOM  = 'feeds/%s.atom.xml'


PLUGIN_PATH = u"../pelican-plugins"

##PLUGINS = ["sitemap","gzip_cache"]
##PLUGINS = ["sitemap"]
##
#### 配置sitemap 插件
##SITEMAP = {
##    "format": "xml",
##    "priorities": {
##        "articles": 0.7,
##        "indexes": 0.5,
##        "pages": 0.3,
##    },
##    "changefreqs": {
##        "articles": "monthly",
##        "indexes": "daily",
##        "pages": "monthly",
##    }
##}

DEFAULT_PAGINATION = 10#默认每一页有多少篇文章

DEFAULT_CATEGORY ='misc'
OUTPUT_PATH = '.'
#需要把输出路径从默认的'output'改成根目录(your_id.github.com目录), 因为githubpage需要把index.html上传到repo的master分支的根目录才可以!
PATH = 'posts'#这个是指定放置.md/.rst文件的目录
STATIC_PATHS = ["static", ]

LINKS = (
	('IBM developerworks','http://www.ibm.com/developerworks/'),
	('Yocto docs','https://www.yoctoproject.org/documentation/current'),
	#('dofine', 'http://www.dofine.me'),
        #('farseerfc', "http://farseerfc.github.com/"),
        )#友情链接~

SOCIAL = (
        ('github', 'http://github.com/tonyho'),
        #('weibo', 'http://weibo.com/u/1132375127'),
        )#社交网络链接

#TWITTER_USERNAME = 'TonyHo'
SIDEBAR_CUSTOM = r"""


<br/><p><embed src="http://fm.xinli001.com/188/miniplayer.swf" quality="high" width="255" height="37" type="application/x-shockwave-flash"></embed></p>

<script type="text/javascript" src="http://www.douban.com/service/badge/48737245/?selection=latest&amp;picsize=small&amp;hideself=on&amp;show=collection&amp;n=9&amp;cat=book&amp;columns=3"></script>


<br/>
<iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" src="http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=2&ptype=1&speed=0&skin=1&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1132375127&verifier=b1fc848b&dpc=1"></iframe>


<!-- JiaThis Button BEGIN -->
<script type="text/javascript">
var jiathis_config = {data_track_clickback:'true'};
</script>
<script type="text/javascript" src="http://v3.jiathis.com/code_mini/jiathis_r.js?type=left&amp;uid=1676351" charset="utf-8"></script>
<!-- JiaThis Button END -->
<!-- UJian Button BEGIN -->
	<script type="text/javascript" src="http://v1.ujian.cc/code/ujian.js?type=slide"></script>
<!-- UJian Button END -->


<Script Language="JavaScript"> 
var timedate= new Date("nov 26,2012"); 
var now = new Date(); 
var date = now.getTime() - timedate.getTime(); 
var time = Math.floor(date / (1000 * 60 * 60 * 24)); 
if (time >= 0) ;
document.write("<p style='text-align: center'><strong><font style='color:green;font-size:36px;'><br/><br/>"+time +"</font>th</strong> running days <br/><strong> <br/> </strong></p>");
</Script>

"""

#GOOGLE_CUSTOM_SEARCH_SIDEBAR = "010418818026634312633:0kgxbuitfaa"

#SIDEBAR_CUSTOM = r"""
#<script type="text/javascript" src="http://www.douban.com/service/badge/48737245/?show=collection&amp;n=8&amp;columns=2&amp;hidelogo=yes" ></script>
#<li class="nav-header"><h4><i class="icon-list-alt"></i>Weibo</h4></li>
#<iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" src="http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=2&ptype=1&speed=0&skin=1&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1132375127&verifier=b1fc848b&dpc=1"></iframe>
#
#"""


# TWITTER_USERNAME = 'TonyHo'
 #SIDEBAR_CUSTOM = r"""
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
