# CrawlBot

번개장터
```
# www.robotstxt.org/ 
# Allow crawling of all content 
User-agent: * 
Disallow: 
Crawl-delay: 1 
# Google Search Engine Sitemap Sitemap: https://s3.ap-northeast-2.amazonaws.com/bunsitemap/production/sitemap.xml.gz
```

당근마켓
```
# See http://www.robotstxt.org/robotstxt.html for documentation on how to use the robots.txt file

User-agent: *
Disallow: /ad/*
Disallow: /admin

Sitemap:https://www.daangn.com/sitemap.xml
```

중고나라
```
User-agent: *
Disallow: 
Allow: /
```

헬로마켓
```
# robots.txt file for Hellomarket

User-agent: *
Disallow: /
Allow : /$

User-agent: Googlebot
User-agent: Googlebot-Video
Allow: /

User-agent: NaverBot
Allow: /
Disallow: /*.gif$
Disallow: /*.jpg$
Disallow: /*.png$

User-agent: Daumoa
Allow: /
Disallow: /*.gif$
Disallow: /*.jpg$
Disallow: /*.png$

User-agent: Bingbot
Allow: /
Disallow: /*.gif$
Disallow: /*.jpg$
Disallow: /*.png$

User-agent: Yeti
Allow: /
Disallow: /*.gif$
Disallow: /*.jpg$
Disallow: /*.png$

User-agent: Twitterbot
Allow: /
Disallow: /*.gif$
Disallow: /*.jpg$
Disallow: /*.png$

User-agent: yandexBot
Disallow: /

User-agent: AhrefsBot
Disallow: /

User-agent: Baiduspider
User-agent: Baiduspider-mobile
User-agent: Baiduspider-video
User-agent: Baiduspider-image
Disallow: /

User-agent: Ezooms
Disallow: /

User-agent: Yandex
User-agent: YandexBot
User-agent: YandexMobileBot
User-agent: YandexVideo
User-agent: YandexWebmaster
User-agent: YandexSitelinks
Disallow: /

# DL Sitemap
Sitemap: https://www.hellomarket.com/sitemap.xml

# Item sitemaps
Sitemap: https://www.hellomarket.com/hellomarket-sitemap-set.xml
```

셀잇

셀잇에서 등록한 상품 제외
```
User-Agent: *
Sitemap: https://www.withsellit.com/sitemap.xml
Disallow: /products/261896
Disallow: /products/351384
Disallow: /products/129455
```

다나와
```
# robots.txt for http://dmall.danawa.com/

User-agent: *
Disallow: /sale/
Disallow: /rank/
Disallow: /free/
Disallow: /exchange/
Disallow: /buy/
Disallow: /v2/
```

사용한 package

```
requests
datetime
os
pymongo
bs4
```


crontab
