def f():
    print('f() 실행')
    raise Exception('예외 발생')
    print('f() 끝')

def g():
    print('g() 시작')
    f()
    print('g() 끝')
     
def h():
    print('h() 시작')
    try:
        g()
    except:                         #해당 행에서의 except가 f()에서의 예외를 종료시킴
        print('잡았다 !')
    print('h() 끝')

h()
print('종료')




