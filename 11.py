import requests
import math


def chances(all_data,char):
    #Βρισκω την πιθανοτητα καθε στοιχειου
    total=0
    for y in all_data:
        if y==char:
            total+=1
    return total/len(all_data)
    
def finding_entropy(all_data,hex_alphabet):
    entropy=0
    for char in hex_alphabet:
        per=chances(all_data,char)
        entropy-=(per*math.log(per,2))
    return entropy

#Στο πεδιο round οι αριθμοι αυξανονται κατα 1 αρα λαμβανω τον τελευταιο αριθμο και μετα βρισκω του 19 αλλους με αφαιρεση
for i in range(20):  
    link = "https://drand.cloudflare.com/public/latest"
    a = requests.get(link)
    data=a.json()
    hexdecnum=data["round"]


rounds=[]
for i in range(0,20):
    hexdecnum-=1
    rounds.append(hexdecnum)

print (rounds)

numbers=[]
for i in range(20):
    link = "https://drand.cloudflare.com/public/"+str(rounds)
    requests.get(link)
    data=a.json()
    numbers.append(data["randomness"])

all_data=""
hex_alphabet= ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
#Ολα τα στοιχεια τα οποια μπορει να λαβει μια δεξαδικη ακολουθια

for i in range(len(numbers)):
    all_data+=str(numbers[i])
#print(all_data)
#print(type(all_data))
print(finding_entropy(all_data,hex_alphabet))
