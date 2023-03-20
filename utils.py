print("Введите стоимость товара: ")
price = float(input())
print("Введите купюры внесенные в кассу: ")
cash = input().split()# разделяю значение по пробелу
num_list = list(map(int, cash)) #list() конвертирует объект map снова в список.
def calculate_ch(price, cash):
    print("Сумма внесенных купюр:", sum(num_list))
change = (sum(num_list)-price)
if change < price:
    print("Недостаточно внесенных средств")
print("Сдача: ", change)
banknotes = [5000, 1000, 500, 100, 50, 10, 5, 2, 1, 0.50, 0.10, 0.05, 0.01]
for i in banknotes:
     res, change = divmod(change, i) #divmod-функция деления,
             # которая принимает два числа и возвращает пару чисел(кортеж),
             # состоящую из их частного и остатка
     if res:
             print(f'{i} - {res}', "шт.")
if __name__ == "__main__":
   calculate_ch(price, cash)