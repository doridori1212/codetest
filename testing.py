import math
class Solution:
    def reverse(self, x: int) -> int:
        if x <= -2**31 or x>=(2**31)-1:
            return 0
        if x == 0:
            return 0
        def get_digit(x):
            num = x
            cnt = 0
            while num != 0:
                num = int(num / 10)
                cnt +=1
            return cnt
        digit = get_digit(x)
        temp_list = []
        minus = False
        if x < 0:
            x *=-1
            minus = True
        for i in range(0, digit):
            temp = int((x%10**(i+1)) / 10**i)
            temp_list.append(temp)
        last_check = False
        result = 0
        cnt = 0
        for j in reversed(temp_list):
            if last_check == False:
                if j == 0:
                    last_check = False
                else:
                    last_check = True
                    result +=j*(10**cnt)
                    cnt +=1
            else:
                result += j * (10 ** cnt)
                cnt += 1
        if minus == True:
            result *=-1
        if result <= -2**31 or result>=(2**31)-1:
            return 0
        return result

class Solution2:
    def reverse(self, x: int) -> int:
        num =0
        a = 0
        while x:
            a = x % 10
            num = a + num * 10
            x = int(x/10)
        return num
print(Solution2.reverse(Solution2,1539))




