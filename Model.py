class Model:
    def __init__(self, t, c = ""):
        self.tag = t
        self.cid = c
        self.children = []
        self.data = ""

    def __str__(self):
        op = self.tag
        for c in self.children:
            op += f"\n   {c}"
        return op

    def add(self, child):
        self.children.append(child)
    
    def html(self):
        op = "<" + self.tag
        if self.cid != "": op += ' class="' + self.cid + '"'
        op += ">"
        for c in self.children:
            op += "\n" + c.html()
        return op + f"\n</{self.tag}>"

class Property:
    def __init__(self):
        pass
