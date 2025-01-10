receipts = [] # 영수증을 저장할 리스트
balance = 3000  #현재 잔액을 보여주세요

while True:
    num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)")
    if num == '4':
        break
    if num == '1':
        deposit_amount = int(input("입금하실 금액을 입력해주세요 : "))
        balance = balance + deposit_amount # balance += deposit_amount
        receipts.append('입금', deposit_amount, balance)
        print(f'{deposit_amount}원 입금이 완료되었습니다. 현재 잔액은 {balance}원 입니다.')
    if num == '2':
        withdraw_amount = int(input("출금하실 금액을 입력해주세요 : "))
        withdraw_amount = min(balance, withdraw_amount)
        balance -= withdraw_amount
        receipts.append('출금', withdraw_amount, balance)
        print(f'{withdraw_amount}원 출금이 완료되었습니다. 현재 잔액은 {balance}원 입니다.')

print(f"서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.")