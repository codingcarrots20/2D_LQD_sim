import random
f = open("demofile.txt", "a")




for i in range(0,10):
    f.write(str(random.randint(0,16))+"\n"+ str(random.randint(0,16))+"\n")
    f.write(str(random.uniform(-12,12))+"\n"+str(random.uniform(-12,12))+"\n")

f.close()


print("done")
