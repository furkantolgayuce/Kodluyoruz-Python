import pandas as pd

df = pd.DataFrame(
    [8.0,9.5,11.0],
    columns= ["Fiyat"],
    index=['Türk Kahvesi', 'Americano', 'Latte']
    )

df = df.apply(lambda x: x*0.8)

print(df)
