class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        left_ops = []
        for i, e in enumerate(s):
            if(e == "*"):
                stars.append(i)
            elif(e == "("):
                left_ops.append(i)
            else:
                if(left_ops):
                    left_ops.pop()
                elif(stars):
                    stars.pop()
                else:
                    return False
        
        if(left_ops):
            while(left_ops):
                if(stars and stars[-1]>left_ops[-1]):
                    left_ops.pop()
                    stars.pop()
                else:
                    return False
        return True