import requests

link = "https://drand.cloudflare.com/public/latest"
a = requests.get(link)
data=a.json()
x=data["round"]
#print(x)
#print(type(x))


rounds=[]  
for i in range(1,101):
    x-=1
    rounds.append(x)

#print(rounds)
#print(type(rounds))
hex_data=""
numbers=[]
for i in range(len(rounds)):
    link="https://drand.cloudflare.com/public/"+str(rounds[i])
    a=requests.get(link)
    data=a.json()
    numbers.append(data["randomness"])
    


for i in range(len(rounds)):
    hex_data+=str(numbers[i])
#print(hex_data)
#print(type(hex_data))

#print("Enter the Hexadecimal Number: ", end="")
hnum = hex_data

bnum = ""
chk = 0
hlen = len(hnum)
i = 0
while i<hlen:
    if hnum[i] == '0':
        bnum += "0000"
    elif hnum[i] == '1':
        bnum += "0001"
    elif hnum[i] == '2':
        bnum += "0010"
    elif hnum[i] == '3':
        bnum += "0011"
    elif hnum[i] == '4':
        bnum += "0100"
    elif hnum[i] == '5':
        bnum += "0101"
    elif hnum[i] == '6':
        bnum += "0110"
    elif hnum[i] == '7':
        bnum += "0111"
    elif hnum[i] == '8':
        bnum += "1000"
    elif hnum[i] == '9':
        bnum += "1001"
    elif hnum[i] == 'a' or hnum[i] == 'A':
        bnum += "1010"
    elif hnum[i] == 'b' or hnum[i] == 'B':
        bnum += "1011"
    elif hnum[i] == 'c' or hnum[i] == 'C':
        bnum += "1100"
    elif hnum[i] == 'd' or hnum[i] == 'D':
        bnum += "1101"
    elif hnum[i] == 'e' or hnum[i] == 'E':
        bnum += "1110"
    elif hnum[i] == 'f' or hnum[i] == 'F':
        bnum += "1111"
    else:
        chk = 1
        break
    i = i+1


#print(" Binary Value = ", bnum)
def max_consecutive_0(bnum): 
     return  max(map(len,bnum.split('1')))
def max_consecutive_1(bnum): 
     return  max(map(len,bnum.split('0')))
print("biggest sequence of 0 ",max_consecutive_0(bnum))
print("biggest sequence of 1 ",max_consecutive_1(bnum))
