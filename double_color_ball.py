import random


blues = [1,2,3,4,5,6,7,8,9,10,11,12,\
         13,14,15,16,17,18,19,20,21,\
         22,23,24,25,26,27,28,29,30,\
         31,32,33,34,35]

red_ball = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

while input('ANY KEY = GO ON , ENTER = STOP : '):

    items_choice = random.sample(blues, 6)

    the_red =random.sample(red_ball, 1)

    items_sort2 = items_choice[:]

    items_sort2.sort()

    print ('您本次随机选择的双色球是：',items_sort2,'+',the_red)
