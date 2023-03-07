# # 1
# n = str(input("문자열을 입력해주세요"))
# print(sum(string == "e" for string in n))

# 2
# sum = 0
# n = str(input("문자열을 입력해주세요"))
# modul = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U")
# for string in n:
#     if string in modul:
#         sum += 1
# print(sum)

#3
# dict_variable = {
#     "이름": "정우영",
#     "생년": "2000",
#     "회사": "하이퍼그로스",
# }
# if "나이" not in dict_variable:
#     dict_variable["나이"] = "24"
# print(dict_variable)

# # 4
# dict_variable ={}
# name = input("이름을 입력하세요")
# number = input("핸드폰 번호를 입력하세요")
# location = input("거주지를 입력하세요")
# dict_variable["이름:"] = name
# dict_variable["핸드폰번호:"] = number
# dict_variable["거주지:"] = location
#########################################
# if "이름" not in dict_variable:
#     dict_variable["이름:"] = name
# if "핸드폰번호" not in dict_variable:
#     dict_variable["핸드폰번호:"] = number
# if "거주지" not in dict_variable:
#     dict_variable["거주지:"] = location
#########################################
# for key in dict_variable:
#     print(key, dict_variable[key])

#5
# name = input("이름을 입력하세요")
# number = input("전화번호를 입력하세요")
# emile = input("이메일을 입력하세요")
# location = input("거주지를 입력하세요")
# user = {
#     name: {
#         "전화번호": number,
#         "이메일": emile,
#         "거주지": location
#     }
# }
# print(user)


string = input("문자열을 입력하세요")
tmp = {}
for char in string:
    try: tmp[char] += 1
    except: tmp[char] = 1
# print(tmp)
for i in tmp:
    print(i, tmp[i])

