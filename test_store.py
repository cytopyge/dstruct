import store
opslag = store.Store()

opslag.saveValue({'port1': 'leeg'})
print(opslag.getValue("port1"))
