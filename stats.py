input_ = int(input('No. of inputs '))
nums1 = []
nums2 = []
nums3 = []
# creating empty lists so can be appended later
done = False

while not done and input_ >= 1:
    # if var 'done' is true it exits but if it is false it goes on until we reach the end
    curr = int(input("what number are we adding. (0 to exit)"))
    if curr == 0:
        are_done = True
    elif 150 < curr < 160:
        nums1.append(curr)
    elif 160 < curr < 170:
        nums2.append(curr)
    elif 170 < curr < 180:
        nums3.append(curr)
    else:
        print("wrong input, try again")
        input_ += 1
    input_ -= 1

print(f'150-160 is {nums1}')
print(f'160-170 is {nums2}')
print(f'170-180 is {nums3}')