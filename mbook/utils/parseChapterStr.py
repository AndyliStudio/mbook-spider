import re
from mbook.utils.chinese2num import chinese2num

def parseChapterStr(str):
  result = None
  chapterReg1 = re.compile(r'第?[零一二两三叁四五六七八九十百千万壹贰叁肆伍陆柒捌玖拾佰0-9]+章?[\.、：: -]*[^\n]+')
  chapterReg2 = re.compile(r'[零一二两三叁四五六七八九十百千万壹贰叁肆伍陆柒捌玖拾佰0-9]+')
  if chapterReg1.match(str):
    searchResult = chapterReg2.search(str)
    if searchResult:
      result = {
        'num': chinese2num(searchResult.group(0)),
        'name': re.sub(r'^.*章?[、\.：\s:-]+', '', str)
      }
  
  return result

if __name__ == '__main__':

    test_data = [u'第三章 无敌',
                 u'第三章、 无敌',
                 u'第3章 无敌',
                 u'3、无敌',
                 ]

    for str in test_data:
        print(parseChapterStr(str))
