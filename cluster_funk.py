"""This code calculates the number of total number of ifected over time, given a R0 which the rate its spreading and t0 which is the initially infected"""
__author__ = str("730203430")

R0: float = input("Enter R0.")
t0: int = input("Enter initially infected.")
t1: int = round(int(t0)*float(R0))
t2: int = round(int(t1)*float(R0))
t3: int = round(int(t2)*float(R0))
t4: int = round(int(t3)*float(R0))
total1: int = int(t0)+int(t1)
total2: int = int(t2)+int(total1)
total3: int = int(t3)+int(total2)
total4: int = int(t4)+int(total3)
##print("Enter R0: "+R0)
##print("Enter t0 Cluster Size: "+t0)
print("t1 - New: "+str(int(t1))+" - Total: "+str(total1))
print("t2 - New: "+str(int(t2))+" - Total: "+str(total2))
print("t3 - New: "+str(int(t3))+" - Total: "+str(total3))
print("t4 - New: "+str(int(t4))+" - Total: "+str(total4))