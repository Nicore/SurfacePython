def Solution(A, B) -> int:
    # identify the maximum possible maximum stick length
    maxStick = (A + B) // 4
    while maxStick > 0:
        # confirm if both A and B can be divided into portions equal to max stick length
        check = (A // maxStick) + (B // maxStick)
        if check == 4:
            return maxStick
        else:
            # if not, then reduce the maximum stick length by 1 until we reach 0
            maxStick -= 1
    
    return 0

x = Solution(1,8)
print(x)
print(Solution(1,2))
print(Solution(13,11))
print(Solution(10,21))
