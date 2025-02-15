import math  # برای انجام محاسبات ریاضی

print("ماشین‌حساب پیشرفته")
print("عملیات موجود: +، -، *، /، ** (توان)، % (باقی‌مانده)، √ (ریشه‌گیری)")
print("برای خروج، 'exit' را وارد کنید.")

while True:
    operation = input("\nعملیات را وارد کنید: ")

    if operation.lower() == "exit":
        print("خروج از برنامه... 👋")
        break  # خروج از حلقه

    if operation == "√":  # عملیات ریشه‌گیری فقط یک عدد نیاز دارد
        num = float(input("عدد مورد نظر را وارد کنید: "))
        if num >= 0:
            result = math.sqrt(num)
        else:
            result = "عدد منفی ریشه ندارد!"
    else:
        num1 = float(input("عدد اول را وارد کنید: "))
        num2 = float(input("عدد دوم را وارد کنید: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2 if num2 != 0 else "تقسیم بر صفر ممکن نیست!"
        elif operation == "**":
            result = num1 ** num2
        elif operation == "%":
            result = num1 % num2 if num2 != 0 else "محاسبه باقی‌مانده بر صفر ممکن نیست!"
        else:
            result = "عملیات نامعتبر است!"

    print("نتیجه:", result)
