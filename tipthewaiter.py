def tip(total,tippercentage):
    
    totalbill=total+total*tippercentage/100
    totalbill=round(totalbill,2)
    print(f"please pay Rupees{totalbill}")

amt=int(input("enter the total amount:--"))
tipper=int(input("enter the tip percentage:--"))
tip(amt,tipper)
 
 