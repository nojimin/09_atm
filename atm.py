receipts = [(2000, 3000), (-1000, 2000), (5000, 7000)] # 영수증을 저장할 리스트
balance = 3000  #현재 잔액을 보여주세요

while True:
    num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)").strip()
    if not(num.isdigit()):
        print("숫자만 입력해주세요!")
        continue
    if num == '1' or num == '2':
        while True:
            amount = input(f"{'입금' if num == '1' else '출금'}하실 금액을 입력해주세요.").strip()  # strip() 없어도 문제없음, 숫자 입력시에만 형변환, 덤으로 -도 입력 안됨
            if amount.isdigit(): # 문자형 숫자일 경우만.
                amount = int(amount)
            else:
                print("숫자만 입력해주세요!")
                continue

            초과_여부 = False

            if num == '2':
                # amount = min(balance, amount) # 두 값을 비교해서 작은 값을 반환
                if amount > balance :
                    amount = balance
                    초과_여부 = True
                amount = -amount
            
            balance += amount
            거래_정보 = (amount, balance)
            receipts.append(거래_정보)
            # receipts.insert(len(receipts), 거래_정보)
            
            if(초과_여부 == True):
                print(f"************************\n영수증\n****\n출금 가능한 금액을 초과하여 현재 잔액 만큼만 출금합니다!\n****\n출금: {abs(amount)}원. \n현재 잔액은 {balance}원입니다.\n****\n************************")
            else:
                print(f"************************\n영수증\n****\n{'입금' if num == '1' else '출금'}: {abs(amount)}원. \n현재 잔액은 {balance}원입니다.\n****\n************************")
            break
    if num == '3':
        print("현재 잔액:", balance)
        if receipts:
            print("모든 거래 내역 (최근 거래순)")
            for i in reversed(receipts):
                print(f"{'입금' if i[0] > 0 else '출금'} : {abs(i[0])}, 잔액 : {i[1]}")
            print("***************************")
        else:
            print("출력할 거래 내역이 없습니다.")
    if num == '4':
        print(f"서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.")
        break