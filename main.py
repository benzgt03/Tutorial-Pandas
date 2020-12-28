import matplotlib
import numpy as np

matplotlib.use("TkAgg")  # Do this before importing pyplot!
import pandas as pd  # import libary ต่างๆที่จะใช้

# เตรียมข้อมูลสำหรับไว้ใช้
datal = [20, 155, 52, 'liew']
datab = [20, 165, 55, 'benz']  # สร้าง List
benzs = np.array(datab)  # แปลงเป็น Array
idx = ['age', 'height', 'weight', 'name']
benzserie = pd.Series(benzs, idx)  # Arrayแปลงเป็น Series
liewserie = pd.Series(datal, idx)  # List แปลงเป็น Series
print(benzserie)
print(liewserie)
# Asean_serie = pd.Series()

datasum = list(zip(datab, datal))  # นำlist ทั้งสองตัวมารวมกัน
cols = ['benz_profile', 'liew_profile']
dataf = pd.DataFrame(datasum, columns=cols, index=idx)  # สร้างData frame
print(dataf)
random = np.random.randn(5, 4)

# Dataframeแบบเจาะลึกลงไปแต่ละcolumn,row
df = pd.DataFrame(random, index='A B C D E'.split(),
                  columns=['W', 'X', 'Y', 'Z'])  # ทำให้ดูสองแบบกรณีใช้split กับไม่ใช้split
print(df)
dfcolumnW = df[['W']]  # เอาแค่Column W ได้ทั้งสองแบบ
# dfcolumnW = df.W
print(dfcolumnW)
df.drop('A', axis=0, inplace=True)  # เอา Row A ออกไป
del df['W']  # เอา Column W ออกไป
print(df)
locationc = df.loc['C']  # เข้าถึงข้อมูลที่ Row C
print(locationc)
ilocationz = df.Z  # เข้าถึงข้อมูลที่Column Z เรียกตรงๆได้เลยไม่ต้องใช้loc
print(ilocationz)
locaitionby = df.loc['B', 'Y']
print("locationRowb ColumnY =", locaitionby)  # โชวเลขตำแหน่ง row b และ column y

# Condition df

Conddf = df > 0  # บอกว่าค่าไหนมากกว่า0 ในdataframeแล้วreturn มาเป็น boolean
print(Conddf)
Conddf1 = df[df > 0]  # filter ค่าในdf >0
print(Conddf1)
conddfx = df[df['X'] > 0]  # conddition ให้โชวแค่เงื่อนไขที่ x>0
print(conddfx)
conndfxy = df[df['X'] > 0][['X', 'Y']]  # ให้โชว แค่ Column x,y ในเงื่อนไขที่ x>0
print(conndfxy)
connddand = df[(df['X'] > 0) & (df['Y'] > 0)]  # ใช้เงื่อนแค่ให้โชวได้แค่กรณีที่ x>0 และ y>0
print(connddand)

# Dict to dataframe
df1 = pd.DataFrame(
    {'A': 'a b c d'.split(), 'B': 'benz gt 03 con'.split(), 'C': 'A W S D'.split()})  # ใช้split สร้างdata
print(df1)
# missing data
df2 = pd.DataFrame({'R1': ['a', np.nan, np.ones(2), 'd', 'd1'], 'R2': ['q', 'r', 's', np.nan, 'd2'],
                    'R3': ['w', 'x', 'y', 'z', 'a']})  # np.nan = ค่าที่หายไป np.one= ป้อนค่า1เข้าไป
print(df2)
print('ตารางหลังดรอปด้วยrow =', df2.dropna(axis=0))  # drop row ที่มี nan ออก
print('ตารางหลังดรอปด้วยcolumn =', df2.dropna(axis=1))  # drop column ที่มี nan ออก
print('ตารางหลังดรอปด้วยrow และ ถ้ามีnan 2 ค่าขึ้นไปจะไม่เอา =', df2.dropna(axis=0, thresh=2))
df2_fullfill = df2.fillna(value='m')
print("df2fullfill =", df2_fullfill)  # นิยมเติม missing data ด้วยmeanของค่าแต่ละค่าแต่ในที่นี้เราเติมm

df3 = pd.DataFrame({'R1': [1, np.nan, 4, 2, 3], 'R2': [2, 4, 6, np.nan, 8], 'R3': [7, 8, 9, 1, 11]})
print(df3)
df3_fullfillR1 = df3.R1.fillna(value=df3.R1.mean())
print(df3_fullfillR1)  # จะเติมด้วยmeanของcolumn R1
df3_fullfillall = df3.fillna(value=df3.mean())
print(df3_fullfillall)  # จะเติมแต่ละช่องด้วยmean แต่ละcolumn
# Group By
df4 = pd.DataFrame({'University': 'a b c b a c'.split(), 'Faculty': 'CO ME EE CE BME CI'.split(),
                    'Grade': '1.5 3.4 2.1 1.8 1.6 4'.split()}, index=[1, 2, 3, 4, 5, 6])
print(df4)
Group_ByU = df4.groupby('University')  # group by university หาค่า max ,min คนที่อยู่มหาลัยเดียวกัน
print(Group_ByU.min())
print(Group_ByU.max())

df5 = pd.DataFrame({'Company': ['1', '2', '3', '1', '2'],
                    'name': ['new', 'guy', 'bew', 'nut', 'boss'],
                    'score': [11, 12, 11, 13, 12]}, index=[1, 2, 3, 4, 5])
print(df5)
Group_ByC = df5.groupby('Company')  # group by company หาmean คนที่อยู่บริษัทเดียวกัน
print(Group_ByC.mean())
print(Group_ByC.std())
print(df5.groupby(['Company', 'name']).mean())  # group by two column แล้วหา mean ของcolumnที่เหลือ
print(Group_ByC.describe())  # อธิบายทุกอย่าง count mean std min percentile

# การJoinแบบConcatenate

df6 = pd.DataFrame({'Company': ['A', 'B', 'C', 'D', 'E'],
                    'name': ['new', 'guy', 'bew', 'nut', 'boss'],
                    'score': [11, 12, 11, 13, 12]}, index=[1, 2, 3, 4, 5])
df7 = pd.DataFrame({'Company': ['F', 'G', 'H', 'I', 'J'],
                    'name': ['nan', 'qan', 'hu', 'am', 'kan'],
                    'score': [10, 17, 9, 8, 11]}, index=[6, 7, 8, 9, 10])
df8 = pd.DataFrame({'Company': ['K', 'L', 'M', 'N', 'O'],
                    'name': ['ew', 'yat', 'wut', 'tan', 'ss'],
                    'score': [11, 12, 11, 13, 12]}, index=[11, 12, 13, 14, 15])
concat1 = pd.concat([df6, df7], axis=0)  # concat สองตารางแนวRow
print(concat1)
concat2 = pd.concat([df6, df7, df8], axis=0)  # concat สามตารางแนวRow
print(concat2)
concat3 = pd.concat([df6, df7, df8], axis=1)  # concat สามตารางแนวcolumn
print(concat3)

# การjoin แบบ Merge

leftdf = pd.DataFrame({'Key': ['k1', 'k2', 'k3', 'k4', 'k5'], 'Company': ['A', 'B', 'C', 'D', 'E'],
                       'name': ['new', 'guy', 'bew', 'nut', 'boss'],
                       'score': [11, 12, 11, 13, 12]}, index=[1, 2, 3, 4, 5])
rightdf = pd.DataFrame({'Key': ['k1', 'k2', 'k3', 'k4', 'k5'], 'Company': ['F', 'G', 'H', 'I', 'J'],
                        'name': ['nan', 'qan', 'hu', 'am', 'kan'],
                        'score': [10, 17, 9, 8, 11]}, index=[6, 7, 8, 9, 10])
# inner join
print(pd.merge(leftdf, rightdf, how='inner', on='Key'))
# left join
print(pd.merge(leftdf, rightdf, how='left', on='Key'))
# right join
print(pd.merge(leftdf, rightdf, how='right', on='Key'))

dfnp = leftdf['name'].unique()  # แปลงเป็นnumpy array
print("numpyarraydf =", dfnp)
print("number =", leftdf['name'].nunique())  # ดูจำนวนตัวที่อยู่ในnumpy array


# apply function to df
def plusx(x):
    x = x + 20
    return x


print(plusx(5))  # ตัวอย่างฟังชั่นบวกเลขธรรมดา
print(leftdf['score'].apply(plusx))  # นำข้อมูลไปเข้า function
print(leftdf['name'].apply(len))  # สามารถใส่ฟังชั่นที่มีอยู่แล้วได้ด้วย (ฟังชั่นlen คือนับตัวอักษรจำนวนstring)
print(leftdf['score'].sort_values())  # sort ฟังชั่นเรียงลำดับ
print(leftdf['score'].isnull())  # เช็คว่าเท่ากับnullไหม
print(leftdf.columns)  # เช็คcolumn
print(leftdf.index)  # เช็คindex

# import and export data
premier = pd.read_csv("C:\\Users\\Admin\\Desktop\\PortGT03\\footballpremier.csv")  # ทดลองเปิดdata set ที่เป็นCSV
print(premier)
df6.to_csv('benzex.csv')  # บันทึก df6 ลงใน benzex.csv
benzex = pd.read_csv(
    "C:\\Users\\Admin\\PycharmProjects\\pythonProject3\\benzex.csv")  # ลองนำกลับมาเปิดอ่านดูว่าเหมือนไหม
print(benzex)
writer = pd.ExcelWriter('benzcel.xlsx')  # สร้างไฟล์excel
benzex.to_excel(writer)  # นำข้อมูลในbenzex ไปใส่
writer.save()
# กรณี read ก็ใช้.read_excel
