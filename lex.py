
# TODO
# - Formalize the Grammar, First and Follow
# - Create an ast!

def lex(s):
    tokens = []
    for c in s:
        if c == "*":
            tokens.append(("*", "*"))
        elif c == "+":
            tokens.append(("+", "+"))
        elif c == "(":
            tokens.append(("(", "("))
        elif c == ")":
            tokens.append((")", ")"))
        else:
            tokens.append(("Lit", c))

    tokens.append(("EOF", ""))
    return tokens


print lex("a")
print lex("aa")
print lex("a|b|c")
print lex("(a)")
print lex("a(b)")
print lex("(a|b)")
print lex("(a|b)*")



# Start grammar symbol

def parse(tokens):
    data = {
        'i': 0,
        'tree': ('Re', [])
    }

    tree = []

    def get():
        i = data['i']
        print "-Get %s" % (i)
        if i >= len(tokens):
            return None
        else:
            return tokens[i]

    def next():
        data['i'] += 1



    def Ops():
        token = get()
        print "Ops", token

        if token == None:
            raise Expection()

        (cat, lexeme) = token

        # First of Ops -> |Re
        if cat == "|":
            tree.append(('|', 'Re'))
            print "=> |, Re"
            next()
            return Re()
        # First of Ops -> *
        elif cat == "*":
            tree.append(('*'))
            print "=> *"
            next()
            return True
        # First of Ops -> +
        elif cat == "+":
            tree.append(('+'))
            print "=> +"
            next()
            return True
        # First of Ops -> Re
        elif cat == "Lit" or cat == "(":
            tree.append(('Re',))
            print "=> Re"
            return Re()

        # Follow of Ops
        elif cat == ")":
            tree.append(('Lamda',))
            print "=> Lamda"
            return True

        # Follow of Ops
        elif cat == "EOF":
            return True
        else:
            return False


    def Re():
        token = get()
        print "Re", token

        if token == None:
            raise Expection

        (cat, lexeme) = token

        if cat == "EOF":
            return True

        # First of Re -> rOps
        if cat == "Lit":
            tree.append(('Lit', 'Ops'))
            print "=> r, Ops"
            next()
            return Ops()
        # First of Re -> (Re)Ops
        elif cat == "(":
            tree.append(('(', 'Re', ')', 'Ops'))
            print "=> (, Re, ), Ops"
            next()
            if Re():
                (cat, lexeme) = get()
                if cat == ")":
                    next()
                    return Ops()

        return False



    return (Re(), tree)

cases = [
    "a",
    "(a)",
    "(aa)",
    "a|(cde)*a+",
    "((((aaa))))",
]

for (i, c) in enumerate(cases):
    print "%s: %s \n" % (i, c)
    (res, tree) = parse(lex(c))
    print "Is Accepted: %s" % res
    for n in tree:
        print n
    print "\n"

