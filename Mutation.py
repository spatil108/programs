def mutate_string(string, position, character):
    s = string
    p = position
    c = character
    s = s[:p]+c+s[p+1:]
    return s

if __name__ == '__main__':
    s = input("Enter String")
    i, c = input("Enter number and character").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

"""Replace the character case on the number entered"""
