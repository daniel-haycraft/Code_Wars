
def generate_hashtag(s):
    if not s or len(s) >= 139:
        return False
    s = s.title()
    s = s.split(' ')
    checker = [str(lets) for lets in s if len(lets) > 0]
    x = ''.join(checker)
    return '#' + x
    
            

print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   " ))
print(generate_hashtag(""))