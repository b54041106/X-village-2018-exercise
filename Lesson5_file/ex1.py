f = open('note.txt', 'w+')

date = input('輸入日期:')
event = input('輸入事件:')
description = input('輸入心得:')

f.write(date)
f.write(event)
f.write(description)

f.close()
