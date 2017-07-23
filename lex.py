
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
        print "Ops", i, token

        if token == None:
            raise Expection()

        (cat, lexeme) = token

        if cat == "EOF":
            return True

        # First of Ops -> |Re
        if cat == "|":
            next()
            return Re()
        # First of Ops -> *
        elif cat == "*":
            next()
            return True
        # First of Ops -> |
        elif cat == "|":
            next()
            return True
        # First of Ops -> Re
        elif cat == "Lit" or cat == "(":
            return Re()

        # Follow of Ops -> Lambda
        elif cat == ")":
            return True
        else:
            return False


    def Re():
        token = get()
        print "Re", token

        if token == None:
            raise Expection

        (cat, lexeme) = token

        # if cat == "EOF":
            # return True

        # First of Re -> rOps
        if cat == "Lit":
            next()
            return Ops()
        # First of Re -> (Re)
        elif cat == "(":
            next()
            if Re():
                (cat, lexeme) = get()
                if cat == ")":
                    next()
                    return True

        return False



    return Re()

cases = [
    "a",
    "(a)",
    "(aa)",
    "a|(cde)*a+",
    "((((aaa))))",
]

for (i, c) in enumerate(cases):
    print "%s: %s \n" % (i, c)
    print parse(lex(c))
    print "\n"

