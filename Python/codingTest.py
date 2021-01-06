# vending machine
def view(D):

    d = ['콜라','사이다','식혜','옥수수수염차','레쓰비']

    for i in range(5):
        value = D.get(d[i])
        if value[0] <= 0 :
            value[2] = 'X'
        
    print("************Vending Machine****************")
    print("콜라\t","사이다\t","식혜\t","옥수수수염차\t","레쓰비")
    coke = D.get('콜라')
    v1 = coke[2]
    x1 = coke[0]
    cider = D.get('사이다')
    v2 = cider[2]
    x2 = cider[0]
    sikhye = D.get('식혜')
    v3 = sikhye[2]
    x3 = sikhye[0]
    corn = D.get('옥수수수염차')
    v4 = corn[2]
    x4 = corn[0]
    letsbe = D.get('레쓰비')
    v5 = letsbe[2]
    x5 = letsbe[0]

    print("구매가능여부>>")
    print(v1,"\t",v2,"\t",v3,"\t\t",v4,"\t",v5)
    print("수량>>")
    print(x1,"\t",x2,"\t",x3,"\t\t",x4,"\t",x5)


def put(drink, n, drinks):
    if drink in drinks:
        drinks[drink][0] += n


def buy(money, drinks):
    d = ['콜라','사이다','식혜','옥수수수염차','레쓰비']
    a = {}

    while True:
        ask =  input("계속 구매하시겠습니까?(yes 또는 no 입력/no 입력 시 잔액 반환): ")
        if ask == 'no':
            print("잔액 : ",money)
            break
        
        elif money <= 0:
            break
        else:
            for i in range(5):
                value = drinks.get(d[i])
                if value[1] <= money:
                    a[d[i]] = 'ON'
                else:
                    a[d[i]] = 'OFF'

            print("**************************현황****************************")
            print(d[0],": ",a.get(d[0])," ",d[1],": ",a.get(d[1])," ",d[2],": ",a.get(d[2])," ",d[3],": ",a.get(d[3])," ",d[4],": ",a.get(d[4]))

            drink = input("구매할 음료: ")
            value = drinks.get(drink) 
            if value[0] > 0:
                value[0] -= 1
                money -= value[1]
                print(drink," 구매 완료")
                print("남은 수량: ",value[0])
                print("잔액: ",money)
            else:
                print("수량이 없어 구매할 수 없습니다.")
    
        
#main          

drinks = { '콜라':[3, 500, 'O'], '사이다':[3, 600, 'O'], '식혜':[3,700, 'O'],
           '옥수수수염차' : [3, 800, 'O'], '레쓰비': [3, 1000, 'O']}

while True:
    view(drinks)
    num = int(input("1.음료 채우기   2.구매   3.종료"))

    if num == 3:
        print("종료")
        break

    elif num == 1:
        drink = input("채워넣을 음료를 입력하세요(콜라,사이다,식혜,옥수수수염차,레쓰비): ")
        n = int(input("채워넣을 음료의 수량을 입력하세요: "))
        put(drink, n, drinks)

    elif num == 2:
        money = int(input("돈을 넣어주세요: "))
        buy(money, drinks)
