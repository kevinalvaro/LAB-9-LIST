#program penghitung sebuah file txt
#by Kevin Alvaro Adianto

try:
    new=open("list.txt","x")
    new.close()
    file=open("list.txt","r")
except :
    file=open("list.txt","r")

teks=""
for i in file:
    teks=teks+i
teks=list(teks)
#=======================================
pembagi=''
kata=pembagi.join(teks)
kata=kata.split(" ")
banyak=len(kata)
print("Banyak kalimat per spasi adalah: ",banyak)

#========================================


jumlahhuruf=0
for i in teks:
    jumlahhuruf +=1
    if i == " ":
        jumlahhuruf -=1
print("Banyak huruf adalah: ",jumlahhuruf)
#=======================================

a,i,u,e,o=0,0,0,0,0

for huruf in teks:
    huruf=huruf.lower()
    if huruf == "a":
        a +=1
    elif huruf == "i":
        i +=1
    elif huruf == "u":
        u +=1
    elif huruf == "e":
        e +=1
    elif huruf == "o":
        o +=1
    else:
        continue

print("jumlah a: ",a)
print("jumlah i: ",i)
print("jumlah u: ",u)
print("jumlah e: ",e)
print("jumlah o: ",o)
