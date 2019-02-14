# -*- coding: utf-8 -*-
from translate import Translator

translator= Translator(to_lang="German")
translation = translator.translate("Good Morning!")
print translation

translator2= Translator(to_lang="English")
translation2 = translator2.translate("你好!")
print translation2

#替换单词时忽略大小写
import re
sourceline  = re.compile("Tutor", re.IGNORECASE)

Replacedline  = sourceline.sub("Tutor","Tutorialyiibai has the best tutorials for learning.")
print("Tutorialyiibai has the best tutorials for learning.")
print (Replacedline)