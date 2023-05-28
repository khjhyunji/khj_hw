print('=============')
print('회원가입 창입니다.')
print('=============')

register=False

while not register:
    print('회원가입을 하시겠습니까? \n y:진행   n:취소')
    register_input=input('>> ')
    register_input=register_input.lower()

    if register_input=='y':
        register=True
        print('=============')
        print('회원가입이 진행됩니다.')
        print('=============')

    elif register_input=='n':
        register=True
        print('=============')
        print('회원가입이 취소됩니다.')
        print('=============')
        exit()
        
    else:
        print('=============')
        print('입력값을 확인해주세요')
        print('=============')


users=[]
while True:

    user={}
    username=input('ID:')
    while True:
        password=input('PW:')
        password_confirm=input('PW 확인용 재입력:')
        if password==password_confirm:
            break
        else:
            print('비밀번호가 일치하지 않습니다.')
    name=input('이름:')
    while True:
        birth_date=input('생년월일 여섯자리를 입력하시오.:')
        if len(birth_date)==6:
            break
        else:
            print('다시 입력하시오.')

    email=input('이메일을 입력하시오:')

    user['username']=username
    user['password']=password
    user['name']=name
    user['birth_date']=birth_date
    user['email']=email

    users.append(user)
    print(user)

    print('==============')
    print(f"{user['name']}님 가입되셨습니다.")
    print('==============')

    print('추가 회원가입을 하시겠습니까? \n y:진행   n:취소')
    register_another_input=input('>> ')
    register_another_input=register_another_input.lower()

    if register_another_input=='y':
        pass
    elif register_another_input=='n':
        exit()
    else:
        print('재입력하시오.')