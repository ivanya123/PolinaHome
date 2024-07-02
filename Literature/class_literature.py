import re


class Literature:
    #Ванечка очень злой
    def __init__(self, str_from_bibtex):
        self.title = None
        self.author = None
        self.journal = None
        self.year = None
        self.volume = None
        self.pages = None
        self.url = None
        self.list_authors = None
        self.main_author = None
        self.processing_str(str_from_bibtex)

    @staticmethod
    def autors_in_gost_str(list_authors):
        for index_el, author in enumerate(list_authors):
            # Удаляем ведущие и замыкающие пробелы из имени автора
            list_author_names = author.split(' ')
            first_name = list_author_names.pop(0)
            list_author_names.append(first_name)
            list_authors[index_el] = ' '.join(list_author_names).strip(' ,')
        return ', '.join(list_authors)

    @staticmethod
    def processing_author_str(author_str):
        match = re.search(r'[A-ZА-Я]{2}', author_str)

        def repl_for_belousov(m) -> str:
            string = '.'.join(list(m.group(0))) + '.'
            return string

        if match:
            return re.sub(r'[A-ZА-Я]{2,}', repl_for_belousov, author_str)

        pattern = r'(?<!^)\b\w+?\b'

        def repl(m) -> str:
            return f'{m.group(0)[0]}.'

        author_str = re.sub(pattern, repl, author_str).replace('-', ' ')
        return author_str

    def processing_str(self, str_from_bibtex) -> None:
        lines = [elem.strip() for elem in str_from_bibtex.splitlines()]
        for line in lines:
            if line.startswith('title'):
                self.title = line.split('=')[1].strip('{},')
            if line.startswith('author'):
                self.author = line.split('=')[1].strip('{},')
                self.list_authors = [self.processing_author_str(elem.strip()) for elem in self.author.split('and')]
                self.main_author = self.list_authors[0]
            if line.startswith('journal'):
                self.journal = line.split('=')[1].strip('{},')
            if line.startswith('year'):
                self.year = line.split('=')[1].strip('{},')
            if line.startswith('volume'):
                self.volume = line.split('=')[1].strip('{},')
            if line.startswith('pages'):
                self.pages = line.split('=')[1].strip('{},').replace('--', '-')
            if line.startswith('number'):
                self.number = line.split('=')[1].strip('{},')

    def __str__(self):
        return f'{self.title} {self.author} {self.journal} {self.year} {self.volume} {self.pages} {self.url}'

    def gost_literature(self):
        # Wang, M. A novel solid oxide electrochemical oxygen pump for oxygen therapy /
        # M. Wang, K. M. Nowicki, J. T. S. Irvine //
        # Journal of The Electrochemical Society. – 2022. – Т. 169. – №. 6. – P. 064509.
        return (f'{self.main_author} {self.title} / '
                f'{self.autors_in_gost_str(self.list_authors)} // '
                f'{self.journal}. - {self.year}. -T {self.volume}. - №. {self.number}. -P. {self.pages}.')


if __name__ == '__main__':
    string_literature = """
    @article{xu2018high,
      title={High oxide ion conduction in molten Na2W2O7},
      author={Xu, Jungu and Li, Yanchang and Wang, Jiehua and Bao, Hongliang and Wang, Jianqiang and Zhu, Changli and Ye, Lingting and Xie, Kui and Kuang, Xiaojun},
      journal={Advanced Electronic Materials},
      volume={4},
      number={12},
      pages={1800352},
      year={2018},
      publisher={Wiley Online Library}
    }
    """

    second = """@article{belousov2017highly,
  title={A highly conductive electrolyte for molten oxide fuel cells},
  author={Belousov, VV and Fedorov, SV},
  journal={Chemical Communications},
  volume={53},
  number={3},
  pages={565--568},
  year={2017},
  publisher={Royal Society of Chemistry}
}"""

    literature = Literature(second)
    print(literature.list_authors)
    print(literature.gost_literature())
