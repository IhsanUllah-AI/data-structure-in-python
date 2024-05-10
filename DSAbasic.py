#data structure is building block or raw metrial of any software programe(hash ,graph,tree,array,stack,linkedlist)ther are container for storing data
#good programer is one who choose  right DSA for a problem
#if i store stock price of mangoes for 6 day 
#question and answer what was price at day 3 and day 5 used list DS
stock_price=[230,320,270,290,200,240]
day3=stock_price[2]
day5=stock_price[4]
print("day 3 price=",day3," day 5 price=",day5)
#if i change question what was price on 9 may and 6 may
#now i will save at in dictionary DS
stock_price={
    'may 5':230,
    'may 6':320,
    'may 7':270,
    'may 8':290,
    'may 9':200,
    'may 10':240,
}
price_9_may=stock_price['may 9']
price_6_may=stock_price['may 6']
print("9 may price=",price_9_may," 6 may price=",price_6_may)

#big O notation is used to measure how running time or space requirement grow for your program as input grow
#running time is no of step during execution of program
def summ(a,b):
    return a+b
a=10
b=20
print(summ(a,b))
#suppose if size is 100 take less time and if size increase to 1000 take more time if we represnt in graph
#will show linear function(relation) time=a*n+b we remove constant as well coeffeucent so big O= O(n) is order of n 
#example
def get_square(numb):
    square_numb=[]
    for n in numb: #n is index for numb
        square_numb.append(n*n) #will put at end 
    return square_numb
numbers=[4,5,6,7,8]
sq=get_square(numbers)
print("square of numbers=",numbers ," is =",sq)
#here my list size is 5 it do 5 iteration if its 5 million   it do 5M iteration in loop size increase no of computaion increase so order of growth is  O(n)

#2nd case
#if we increase program size but time almost remain constant  if we represnet on graph will give constant funcion time =a
#order of growth big O=O(1)
#binary search complexity is O(logn)
#if no of element is 8 no of ietratin =3  how? log2^8=log2^2^3=3*log2^2=3*1=3


