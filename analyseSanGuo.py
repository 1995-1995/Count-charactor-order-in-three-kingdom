from jieba import *
inp = open('Name.txt', 'r', encoding='utf-8')
text = inp.read()
words = lcut(text)
counts = dict()
for word in words:
    if len(word) == 1:
        continue
    elif word in ['诸葛', '诸葛亮', '孔明', '孔明曰']:
        counts['诸葛亮'] = counts.get('诸葛亮', 0) + 1
    elif word in ['曹操', '孟德', '丞相', '孟德曰']:
        counts['曹操'] = counts.get('曹操', 0) + 1
    elif word in ['刘备', '玄德', '玄德曰', '刘皇叔']:
        counts['刘备'] = counts.get('刘备', 0) + 1
    elif word in ['张飞', '翼徳', '三弟']:
        counts['张飞'] = counts.get('张飞', 0) + 1
    elif word in ['周瑜', '都督']:
        counts['周瑜'] = counts.get('周瑜', 0) + 1
    elif word in ['关羽', '云长', '关公']:
        counts['关羽'] = counts.get('关羽', 0) + 1
    elif word in ['赵云', '子龙']:
        counts['赵云'] = counts.get('赵云', 0) + 1
    elif word in ['吕布', '奉先']:
        counts['吕布'] = counts.get('吕布', 0) + 1
    else:
        counts[word] = counts.get(word, 0) + 1
        if word in ['意谓', '将军', '却说', '二人', '不可', '荆州', '天下', '如此','不能', '这里', '商议', '如何', '主公', \
                    '出自', '出自', '军士', '左右', '军马', '于是', '引兵', '不敢', '如何', '次日', '东吴', '大喜', '比喻', \
                    '形容', '不知', '今日', '陛下', '魏兵']:
            del counts[word]
listCounts = list(counts.items())
listCounts.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = listCounts[i]
    print('出现第{}的人是{},出现了{}次'.format(i+1, word, count))

