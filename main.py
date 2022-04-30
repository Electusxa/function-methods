### APPEND EXAMPLE ###
dersler=['fizik ','ingilizce','matematik','türk dili ve edebiyatı','coğrafya','kimya']
print(dersler)
dersler.append('almanca')
print(dersler)


### EXTEND EXAMPLE ###
#dersler=['fizik ','ingilizce','matematik','türk dili ve edebiyatı','coğrafya','kimya']
print(dersler)
dersler2=['sosyal etkinlikler','din']
dersler.extend(dersler2)
print(dersler)


### İNSERT EXAMPLE  ###
#dersler=['fizik ','ingilizce','matematik','türk dili ve edebiyatı','coğrafya','kimya']
print(dersler)
dersler.insert(2,'almanca')
print(dersler)


### REMOVE EXAMPLE  ###
#dersler=['fizik ','ingilizce','matematik','türk dili ve edebiyatı','coğrafya','kimya']
print(dersler)
dersler.remove('matematik')
print(dersler)


### POP EXAMPLE  ###
#dersler=['fizik ','ingilizce','matematik','türk dili ve edebiyatı','coğrafya','kimya']
print(dersler)
dersler.pop(1)
print(dersler)


### CLEAR EXAMPLE ###
#dersler=['fizik ','ingilizce','matematik','türk dili ve edebiyatı','coğrafya','kimya']
print(dersler)
dersler.clear()
print(dersler)


### İNDEX EXAMPLE ###
#dersler=['fizik ','ingilizce','matematik','türk dili ve edebiyatı','coğrafya','kimya']
print(dersler)
print(dersler.index('coğrafya'))


### COUNT EXAMPLE ###
#dersler=['fizik ','ingilizce','matematik','türk dili ve edebiyatı','coğrafya','kimya','kimya']
print(dersler)
print(dersler.count('kimya'))


### SORT | REVERSE EXAMPLE ###
#dersler=['fizik ','ingilizce','matematik','türk dili ve edebiyatı','coğrafya','kimya','kimya']
print(dersler)
dersler.sort()
print(dersler)
dersler.reverse()
print(dersler)

notlar=[123,124,125,99,88,7,6,53,4]
print(notlar)
notlar.sort()
print(notlar)
notlar.reverse()
print(notlar)


### COPY EXAMPLE ###
#dersler=['fizik ','ingilizce','matematik','türk dili ve edebiyatı','coğrafya','kimya','kimya']
print(dersler)
dersler2=dersler.copy()
print(dersler2)

