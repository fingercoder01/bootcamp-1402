"""
دیکشنری بنویسید به اسم dict_main که ۳ عنصر داشته باشد و مقدار عنصر دوم یک لیستی باشد به اسم list_m که درون خودش ۵ عنصر دارد که عنصر ۳ ش یک ثاپلی هست به اسم tup_dicکه درون خودش یک دیکشنری به اسم vald_dict داره که ۳ تا عنصر دارد

در مرحله اول باید دیکشنری dict_main به صورت کامل پرینت شود
در مرحله دوم عنصر list_m که درون dict_man هست پرینت شود

در مرحله دوم عنصر ۲ list_m پرینت شود

در مرحله سوم عنصر ۳ list_m پرینت شود

در محله چهارم مقدار های vald_dict پرینت شود

در مرحله اخر کلیه پرینت های تمامی مرحله ها در یک خط پرینت شود به صورت رشته

"""
dict_main = {"m":12,45:[1,2,({"l":7,"y":66,55:"p"}),7,8],"f":6}
print(dict_main)
print(dict_main[45])
print(dict_main[45][1])
print(dict_main[45][2])
print(dict_main[45][2].values())