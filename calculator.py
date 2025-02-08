print("ماشین‌حساب ساده")
num1 = float(input("عدد اول را وارد کنید: "))
operation = input("عملیات (جمع، تفریق، ضرب، تقسیم) را وارد کنید: ")
num2 = float(input("عدد دوم را وارد کنید: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "تقسیم بر صفر ممکن نیست!"
else:
    result = "عملیات نامعتبر است!"

print("نتیجه:", result)