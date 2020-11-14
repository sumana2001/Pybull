import requests
import sys
from bs4 import BeautifulSoup


class Translator:

    def start(self):
        self.accept()
        req_obj_list = self.connect()
        for req_obj in req_obj_list:
            self.formatting(req_obj=req_obj)

    @staticmethod
    def except_handler(lang=None, issue='other'):
        if issue == 'len_input':
            print('Unexpected number of input', file=sys.stderr)
        elif lang is not None:
            print("Sorry, the program doesn't support", lang, file=sys.stderr)
        else:
            print('Input the number from 1-13', file=sys.stderr)

        exit()

    def __init__(self, src_lang=None, trans_lang=None, word=''):
        self.src_lang = src_lang
        self.trans_lang = trans_lang
        self.word = word
        self.lang_list = [
            'Arabic', 'German', 'English', 'Spanish',
            'French', 'Hebrew', 'Japanese', 'Dutch',
            'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish'
        ]
        self.lang_ind = 0
        if trans_lang:
            self.lang_ind = 1 if not trans_lang == 'Arabic' else 0

    def accept(self):
        sys_arg = sys.argv
        if not any([len(sys_arg) == 1, len(sys_arg) == 4]):
            self.except_handler(issue='len_input')

        if len(sys_arg) == 1:
            print("Hello, welcome to the translator. Translator supports: ")

            for no, lang in enumerate(self.lang_list):
                print(no + 1, '. ', lang, sep='')
            src_lang = int(input('Type the number of your language: '))  # to be translated
            trans_lang = int(input(
                    'Type the number of language you want to translate to or "0" to translate to all languages:'))
            if not all([0 < src_lang < 13, 0 <= trans_lang < 13]):
                self.except_handler()
            word = input('Type the word you want to translate:')

        else:
            src_lang_st = sys_arg[1]
            trans_lang_st = sys_arg[2]
            word = sys_arg[3]

            if src_lang_st.capitalize() not in self.lang_list:
                self.except_handler(src_lang_st)
            if not any([trans_lang_st.capitalize() in self.lang_list, trans_lang_st == 'all']):
                self.except_handler(trans_lang_st)

            src_lang = self.lang_list.index(src_lang_st.capitalize()) + 1

            if trans_lang_st == 'all':
                trans_lang = 0
            else:
                trans_lang = self.lang_list.index(trans_lang_st.capitalize()) + 1

        if trans_lang != 0:
            self.__init__(src_lang=self.lang_list[src_lang-1], trans_lang=self.lang_list[trans_lang-1], word=word)
        else:
            self.__init__(src_lang=self.lang_list[src_lang-1], word=word)

    def url_gen(self):
        src_low = self.src_lang.lower()

        if self.trans_lang is not None:
            trans_lower = self.trans_lang.lower()
            return [f'https://context.reverso.net/translation/{src_low}-{trans_lower}/{self.word}', ]

        if self.trans_lang is None:
            url_list = []
            for trans_l in self.lang_list:
                if self.src_lang == trans_l:
                    continue
                else:
                    url = f'https://context.reverso.net/translation/{src_low}-{trans_l.lower()}/{self.word}'
                    url_list.append(url)
            return url_list

    def connect(self):
        user_agent = 'Mozilla/5.0'
        url_list = self.url_gen()
        req_obj_list = []

        try:
            for url in url_list:
                req_obj = requests.get(url, headers={'User-Agent': user_agent})
                req_obj_list.append(req_obj)

        except requests.exceptions.ConnectionError as e:
            print('Something wrong with your internet connection', file=sys.stderr)

        return req_obj_list

    def parse(self, req_obj):
        parser = 'html.parser'
        data = req_obj.content
        soup = BeautifulSoup(data, parser)
        try:
            words = soup.find(id='translations-content').text.split()
            trans_mod = 'trg rtl arabic' if self.lang_ind == 0 else 'trg ltr'
            examples = [x.text.strip() for x in soup.find_all(class_=['src ltr', trans_mod])]
            return words, examples

        except AttributeError:
            print('Sorry, unable to find', self.word, file=sys.stderr)
            exit()

    def formatting(self, req_obj):  
        words, examples = self.parse(req_obj=req_obj)
        no_word = no_examples = 5  # Number of output
        final_lang = self.trans_lang

        if self.src_lang == self.lang_list[self.lang_ind]:
            self.lang_ind += 1

        if self.trans_lang is None:
            no_examples = no_word = 1
            final_lang = self.lang_list[self.lang_ind]

        print(f'{final_lang} Translations:')
        print(*words[:no_word], sep='\n', end='\n\n')

        print(f'{final_lang} Examples:')
        i = 0
        for _ in range(no_examples):
            print(examples[i])
            print(examples[i+1], '\n')
            i += 2

        self.save_2_file(final_lang=final_lang, words=words, examples=examples, no_word=no_word)
        self.lang_ind += 1

    def save_2_file(self, final_lang, words, examples, no_word):
        file_name = self.word+'.txt'
        with open(file_name, 'a', encoding='utf-8') as file_out:
            file_out.write(f'{final_lang} Translations:\n')
            print(*words[:no_word], file=file_out, sep='\n', end='\n\n')

            file_out.write(f'{final_lang} Examples:\n')
            i = 0
            for _ in range(no_word):
                file_out.write(examples[i])
                file_out.write('\n')
                file_out.write(examples[i + 1])
                file_out.write('\n\n')
                i += 2
                file_out.write('\n')


if __name__ == '__main__':
    obj = Translator()
    obj.start()
