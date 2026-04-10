# analyse.ps1

# 1) Lancer le spider Scrapy -> articles.jsonl
scrapy runspider ./news_spider.py -O ./articles.jsonl

# 2) Lancer l'analyse Python -> rapport.txt + top_words.png
python ./analyse.py ./articles.jsonl
