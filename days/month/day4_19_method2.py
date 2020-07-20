class Solution:
    def addBinary(self, a: str, b: str) -> str:
        add = int(a,2)+int(b,2)
        empty=[]
        def decodeBinary(num:int):
            if num//2 == 0:
                empty.insert(0,1)
            else:
                empty.insert(0,num%2)
                decodeBinary(num//2)
        decodeBinary(add)
        return ''.join(map(str,empty))

if __name__=="__main__":
    output=Solution().addBinary('11','101')
    print(output)