#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from src.lib.parser_tools import ParserTools
from src.lib.talkpython_parser.content.talkpython_article import TalkPythonArticle


class BaseParser(ParserTools):
    def __init__(self, content):
        self.dom = BeautifulSoup(content, 'lxml')
        self.article_parser = TalkPythonArticle()

    def get_answer_list(self):
        answer_list = []
        self.article_parser.set_dom(self.dom)
        answer_list.append(self.article_parser.get_info())
        return answer_list

    def get_extra_info(self):
        u"""
        e.g. base info of Yiibai
        :return:
        """
        pass