# N = int(input())
# data = list(map(int, input().split()))
# M = int(input())
# keys = list(map(int, input().split()))

# ans = []
# for key in keys:
#     if key in data:
#         ans.append('1')    # print(1, end='')

#     else:
#         ans.append('0')     # print(0, end='')
# print(''.join(ans))


# class person:
#     def __init__(self,name):
#         self,name = name
    
#     def hello(self):
#         print(f'{self.name} 안녕!')
# p1 = person('홍길동')
# p2 = person('유재석')

# def __del__(self):
    

# def __str__(self):
#     return f'이름: {self.name} - 나이: {self.age}' #형변환 리턴




def mydecorator(func):
    def wrapper(func, name):
        print('호출 전')
        func(name)    #함수호출
        print('호출 후')
    return wrapper

@mysdecorator        
def printhello(name):
    print(f'{name}님 환영합니다.')
    
    
printhello('이지은')