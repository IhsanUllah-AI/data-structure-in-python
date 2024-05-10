#if i store stock price of mangoes for 6 day 
#question and answer what was price at day 3 and day 5 used list DS
#index start with zero
stock_price=[230,320,270,290,200,240]
day3=stock_price[2]
day5=stock_price[4]
print("day 3 price=",day3," day 5 price=",day5)
#if how acces to 2 and 4 suppose stock price index start from 0*005000 each numb is 4 byte  2nd one is 0*005004
#if we write inside it find like this index=0*005000+2*sizeof(integer)
#look up index order is O(1) so big O is constant for it

#on what day price was 290
#now we acces with value not through index 
for n in  range(len(stock_price)):
    if stock_price[n]==290:
        day=n+1
        break
print("290 day=",day)
#look of by value is O(n)  it will look for all value till end 