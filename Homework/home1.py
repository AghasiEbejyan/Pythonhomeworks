#---------------EX1---------------------------------------------
# def func(a:int,b:int,c:int)-> list[int]:
#     list = []
#     for i in range(a,b+1,c):
#         list.append(i)
        
#     return list

# print(func(a=int(input('number start---> ')),b = int(input('ending number---> ')),c = int(input('steps---> '))))        



#--------------------EX2------------------------------------------
# def func(list):
#     list1 = []
#     while len(list) !=1:
#         list1.append(list[0]*list[1])
#         del list[0]
#         continue
#     return list1
# print(func(list = [3,7,12,5,20,0]))    




#--------------------EX3-----------------------------------------
# def func(sentence,list):
    
    
#     return sentence

# print(func(sentence='_, we have a _.'),list=['Ashot','Problem'])



#--------------------EX4----------------------------------
# list = ['anymore', 'raven', 'me', 'communicate']
# list.sort(key = len)
# print(len(list[0])*len(list[-1]))



#------------------------EX5-----------------------------
# tiv = int(input('Enter number---->  '))
# list = [21, -9, 15, 2116, -71, 33]
# print(list.index(tiv)) # lriv pahanjy chstacvec




#-----------------------------EX6------------------------------
# def func(tiv):
#     dict = {}
#     for i in range(1,tiv+1):
#         dict.setdefault(i)
#         dict[i] = i*i
        
#     return dict

# print(func(tiv=int(input('Enter number---->  '))))