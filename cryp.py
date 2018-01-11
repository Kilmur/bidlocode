#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import Tkinter as tk

dict1 = {u"е": "aa", u"д": "ab", u"г": "ac",u"в": "ad",u"б": "ae",u"а": "af",
         u"ж": "ba", u"р": "bb", u"л": "bc",u"т": "bd",u"е": "be",u"с": "bf", 
         u"з": "ca", u"в": "cb", u"й": "cc",u"и": "cd",u"?": "ce",u"о": "cf",
         u",": "da", u"э": "db", u"ю": "dc",u"я": "dd",u" ": "de",u".": "df",
         u"к": "ea", u"ь": "eb", u"ы": "ec",u"щ": "ed",u"ш": "ee",u"ч": "ef",
         u"л": "fa", u"т": "fb", u"у": "fc",u"ф": "fd",u"х": "fe",u"ц": "ff",
         u"м": "ja", u"с": "jb", u"р": "jc",u"п": "jd",u"о": "je",u"н": "jf",}

dict2 = {"aa": u"е", "ab": u"д", "ac": u"г","ad": u"в","ae": u"б","af": u"а",
         "ba": u"ж", "bb": u"р", "bc": u"л","bd": u"т","be": u"е","bf": u"с",
         "ca": u"з", "cb": u"в", "cc": u"й","cd": u"и","ce": u"?","cf": u"о",
         "da": u",", "db": u"э", "dc": u"ю","dd": u"я","de": u" ","df": u".",
         "ea": u"к", "eb": u"ь", "ec": u"ы","ed": u"щ","ee": u"ш","ef": u"ч",
         "fa": u"л", "fb": u"т", "fc": u"у","fd": u"ф","fe": u"х","ff": u"ц",
         "ja": u"м", "jb": u"с", "jc": u"р","jd": u"п","je": u"о","jf": u"н",}

def func1(event):
	get1 = tex1.get('1.0', tk.END)  # Считывание с поля зашифровки 
	list1 = []
	for n in get1:                  # Подбор значения по ключу и добавление в list1
		x1 = dict1.get(n, "df")
		list1.append(x1)

	list2 = []	                    # Шифрование каждого значения из list1
	for i in list1:                 # и занесение в list2
		for j in i:
			if j == "a":
				x = random.choice(["E", "N", "Q", "Z"])
				list2.append(x)
			elif j == "b":
				x = random.choice(["B", "G", "R"])
				list2.append(x)
			elif j == "c":
				x = random.choice(["F", "L", "T"])
				list2.append(x)
			elif j == "d":
				x = random.choice(["A", "O", "X"])
				list2.append(x)
			elif j == "e":
				x = random.choice(["C", "H", "V"])
				list2.append(x)	
			elif j == "f":
				x = random.choice(["I", "P", "S"])
				list2.append(x)
			elif j == "j":
				x = random.choice(["D", "K", "M", "Y"])
				list2.append(x)
	str1 = "".join(list2)                     # Объединение списка в строку
	tex3.delete(1.0, tk.END)                  # Очистка поля tex3
	tex3.insert(1.0, str1)                    # Вставка str1 в поле для копирования
	

def func2(event):                         # Из XKDKFC -> ['a', 'b', 'j', 'd', ...]
	get2 = tex2.get(1.0, tk.END)
	list3 = []
	for i2 in get2:
		if i2 in ["E", "N", "Q", "Z"]:
			list3.append("a")
		elif i2 in ["B", "G", "R"]:
			list3.append("b")
		elif i2 in ["F", "L", "T"]:
			list3.append("c")
		elif i2 in ["A", "O", "X"]:
			list3.append("d")
		elif i2 in ["C", "H", "V"]:
			list3.append("e")
		elif i2 in ["I", "P", "S"]:
			list3.append("f")
		elif i2 in ["D", "K", "M", "Y"]:
			list3.append("j")

	list4 = []                        # Из ['a', 'b', 'j', 'd', ...]
	while len(list3) != 0:            # в ['ab', 'jd', ...]
		for i3 in list3:	
			res = list3[0]+list3[1]
			list4.append(res)
			del list3[0]
			del list3[0]

	list5 = []                        # Из ['ab', 'jd', ...] -> ['п', 'и', ...]
	for s in list4:
		x2 = dict2.get(s, ".")
		list5.append(x2)

	str2 = "".join(list5)            # Объединение текста и вывод 
	tex3.delete(1.0, tk.END)
	tex3.insert(1.0, str2)
	

root = tk.Tk()
root.maxsize(width=550, height=500)
root.minsize(width=550, height=500)

tex1 = tk.Text(root, width=50, height=5, font="Arial 14", wrap=tk.WORD)
tex2 = tk.Text(root, width=50, height=5, font="Arial 14", wrap=tk.WORD)
tex3 = tk.Text(root, width=50, height=5, font="Arial 14", wrap=tk.WORD)

but1 = tk.Button(root, text="Зашифровать", bg="red", fg="white")
but2 = tk.Button(root, text="Раcшифровать", bg="green", fg="white")

lab = tk.Label(root, width=67, height=3, text='Введите текст в форму ниже маленькими русскими буквами,\n дополняя символом "?", запятой, точкой и пробелом')

but1.bind("<Button-1>", func1)
but2.bind("<Button-1>", func2)

tex3.pack()
lab.pack()
tex1.pack()
but1.pack()
tex2.pack()
but2.pack()
root.mainloop()

