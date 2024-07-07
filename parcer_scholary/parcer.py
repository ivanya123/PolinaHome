# -*- coding: utf-8 -*-
from scholarly import scholarly, ProxyGenerator, MaxTriesExceededException
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')

pg = ProxyGenerator()
success = pg.FreeProxies()
scholarly.use_proxy(pg)

with open('Lit.txt', 'r') as f:
    list_lit = f.readlines()
k = 0


def parcer_main():
    try:
        search = scholarly.search_pubs('A novel solid oxide electrochemical oxygen pump for oxygen therapy')
        try:
            article = next(search)
            return article
        except StopIteration:
            print("No results found")
            return parcer_main()
    except MaxTriesExceededException:
        print("Max tries exceeded, retrying after a pause...")
        time.sleep(30)  # Пауза перед повторной попыткой
        return parcer_main()


article = parcer_main()
bibtex_entry = scholarly.bibtex(article)

# Печать bibtex
print(bibtex_entry)

# Запись bibtex в файл с кодировкой utf-8
with open('output.bib', 'w', encoding='utf-8') as f:
    f.write(bibtex_entry)
