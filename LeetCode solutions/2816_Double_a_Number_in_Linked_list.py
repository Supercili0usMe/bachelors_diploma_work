def doubleIt(head: list):
        stack, current = [], head
        while current:
            stack.append(current.pop())
        
        current = stack.pop(0) * 2 
        switch = 0
        if current // 10 > 0:
            switch = 1
            current = current % 10
        res_list = [current]

        while stack:
            current = stack.pop(0) * 2
            new_current = current % 10 + switch
            res_list.append(new_current)
            if current // 10 > 0:
                switch = 1
            else:
                switch = 0

        if not stack and switch == 1:
             res_list.append(switch)
        return res_list[::-1]

print(doubleIt([1,8,9]))
print(doubleIt([9,9,9]))