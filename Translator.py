pirate = {}
pirate['sir'] = 'matey'
pirate['hotel'] = 'fleabag inn'
pirate['student'] = 'swabbie'
pirate['boy'] = 'matey'
pirate['madam'] = 'proud beaty'
pirate['professor'] = 'foul blaggart'
pirate['restaurant'] = 'galley'
pirate['your'] = 'yer'
pirate['excuse'] = 'arr'
pirate['students'] = 'swabbies'
pirate['are'] = 'be'
pirate['lawyer'] = 'foul blaggart'
pirate['the'] = 'th`'
pirate['restroom'] = 'head'
pirate['my'] = 'me'
pirate['hello'] = 'avast'
pirate['is'] = 'be'
pirate['man'] = 'matey'

sentence = input('Your sentence in English: ')
pi_sentence = [] 
translate = sentence.split()

for trans in translate:
    if trans in pirate:
        pi_sentence.append(pirate[trans])
    else:
        pi_sentence.append(trans)
print(' '.join(pi_sentence))