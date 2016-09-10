
from random import choice
from string import ascii_lowercase, digits
from server.models import Game

def generate_random_name(length=16, chars=ascii_lowercase+digits, split=4, delimiter='-'):
    
    name = ''.join([choice(chars) for i in xrange(length)])
    
    if split:
        name = delimiter.join([name[start:start+split] for start in range(0, len(name), split)])
    
    try:
        Game.objects.get(name=name)
        return generate_random_name(length=length, chars=chars, split=split, delimiter=delimiter)
    except Game.DoesNotExist:
        return name;