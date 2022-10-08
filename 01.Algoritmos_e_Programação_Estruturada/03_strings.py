#---- Operadores ----
s = 'abc'
s == 'abc'
# True
t = 'def'
s < t 
# True
s + t 
# True
s + t 
# 'abcdef'
s * t 
# ERRO
s * 2
# 'abcabc'
ch = 'b'
ch in s
# True
ch is str('b')
# True
s = 'abcd'
len(s)
# 4
s[0]
# 'a'
s[3]
# 'd'
s[len(s)]
# ERRO!
s[-1]
# 'd'
s[-2]
# 'c'
s[-5]
# ERRO

# ---- Indexação ----
s = 'abcd'
s[0:2]
# 'ab'
s[-4:-2]
# 'ab'
s[:3]
# 'abc'
s[-1:]
# 'd'

# ---- Métodos ----
s.find(p) #retorna o índice em que a substring p aparece em s
s.count(p) #retorna a frequencia em que a substring p aparece  em s
s.replace(p,q) #substitui a substring p pela substring q em s
s.capitalize() #substitui primeiro caractere de s em maiúscula
s.upper() #substitui todos os caracteres de s em minúscula
s.strip() #remove espaços em branco em excesso
