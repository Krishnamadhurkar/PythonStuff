
import re
# def helper(x):
#     arr = list(x)
#     summ = 0
#     print(arr)
#     for e in range(0,len(arr):)
#         while arr[e] != '+' or arr[e] != '-':
#             temp_string = ''
#             temp_string.append(arr[e])
#         if arr[e] == '+':
#             plus = int(tempstring)
#             summ = summ + plus
#             temp_string = ""
#         elif arr[e] == '-':
            



#     return summ
 
# print(helper("2+2"))
# print(helper("20+15-5"))


def helper(x):
    arr = re.split(r' +|- ', x)
    print(arr)

helper("20+15-5")