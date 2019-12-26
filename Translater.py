from Model import Model

model = Model("html")
body = Model("body")
body.add(Model("h1"))
body.add(Model("p"))
body.add(Model("div", "hello"))
model.add(body)

print(model.html())
