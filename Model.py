class Model:
    def __init__(self, t, c = ""):
        self.tag = t
        self.cid = c
        self.children = []

    def __str__(self):
        if len(self.children) == 0: return self.tag
        return self.tag + "\n  " + "\n  ".join(self.children)

    def add(self, child):
        self.children.append(child)


class Html(Model):
    def __init__(self, t, c):
        super.__init__(t,c)

    def 
