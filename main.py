#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    if len(list1) == len(list2):
        lm = []
        for l in range(0, len(list1)):
            lm.append(list1[l] * list2[l])
        mm = sum(lm)     
        return mm
    else:
        return "Error"

if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    l1 = input()
    l2 = input()
        
    one = []
    two = []
    for i in range(len(l1)):
        one.append(int(l1[i]))
    for i in range(len(l2)):
        two.append(int(l2[i]))

    a = sum_of_products(one, two)
    
    print(a)
