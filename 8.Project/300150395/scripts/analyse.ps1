# scripts/analyse.ps1

# 1) Lancer le spider Scrapy -> data/articles.jsonl
scrapy runspider ./scripts/news_spider.py -O ./data/articles.jsonl

# 2) Lancer l'analyse Python -> output/rapport.txt + output/top_words.png
python ./scripts/analyse.py ./data/articles.jsonl
