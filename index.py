"""
۱ - در اولین مرحله طبق استاندارد کارکتر نویسی کد زیر رو بشکنید
۲ - محتوای کلید shiraz پرینت شود
۳ - محتوای کلید yazd پرینت شود
۴ - محتوای کلید shiraz1 پرینت شود
۵ - محتوای کلید yazd1 پرینت شود
۶ - عنصر ۳ ام کلید shiraz در کنار عنصر سوم کلید yazd با هم پرینت شود
۷ - در اخر عنصر OK و عنصر woman در کنار هم پرینت شود

"""




factory = {'shiraz':['ali','reza','mina','sadegh',{'shiraz1':['admin1',{'secority':('uni',[7878,3454,5679,'OK'])},'admin3']}],'yazd':['raha','yegane','sara','mina',{'yazd1':['manager1',{'sec':('class',[1090,2049,3120,'woman'])},'admin3']}]}


factory = {"shiraz":["ali","raza","mina","sadegh"\
    ,{"shiraz1":["admin1",{"secority":("nui",[7878,3454,5697,"ok"])},"admin3"]}],"yazd":\
    ["raha","yegane","sara","mina",{"yazd1":["manager1",{"sec":("class", \
    [1090,2049,3120,"woman"])},"admin3"]}]}



print(factory.keys("shiraz"))
print(factory.keys("yazd"))

print(factory.keys("shiraz1"))
print(factory.keys("yazd1"))
print(factory["shiraz"][2],factory['yazd'][2])
print(factory["shiraz"][0][5:3],factory["yazd"][0][5:3])
