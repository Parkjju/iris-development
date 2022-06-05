import pandas as pd


# your project absolute path
path = r"C:\Users\dabin\Desktop\2021-2022 휴학\멋사 10기\iris_44"

model = pd.read_pickle(path + "/new_model.pkl")

print(model)

print(model.__dict__)


# print(model[1])

print(str(model))

print(model._y)

print(model._x)
