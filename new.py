# try:
#     num = int(input('100으로 나눌 값을 입력해:'      ))
#     print(100 / num)
# except ValueError:
#     print('숫자를 입력하라니까') #except (ValueError, ZeroDivisionError)가능 이 둘은 계층관계없음
# except ZeroDivisionError:
#     print('왜 0을 입력하는거야?')
# except:
#     print('에러가 발생했다')


# try:
#     num = int(input('100으로 나눌 값을 입력해:'      ))
#     print(100 / num)
# except BaseException:
#     print('숫자를 입력하라니까') #BaseException 이 상위 클래스라 제로디비젼은 죽음.
# except ZeroDivisionError:
#     print('왜 0을 입력하는거야?')
# except:
#     print('에러가 발생했다')

