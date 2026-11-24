import numpy as np
import matplotlib.pyplot as plt
months=["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
asad=[30,50,70,96,25,63,52,88,64,99,12,21]
eyas=np.random.randint(10,100,12)
khaqan=np.random.randint(10,100,12)
bacha=np.random.randint(10,100,12)
baber=np.random.randint(10,100,12)
salman=np.random.randint(10,100,12)
plt.plot(months,asad,label="asad",marker="o")
plt.plot(months,eyas,label="eyas")
plt.plot(months,khaqan,label="khaqan")
plt.plot(months,bacha,label="bacha")
plt.plot(months,baber,label="baber")
plt.plot(months,salman,label="salman")
plt.legend()
plt.grid()
plt.title("Students_monthly report")
plt.xlabel("Months")
plt.ylabel("Number of Students")
plt.savefig("students_monthly.png")
plt.show()