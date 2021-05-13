# Decryption 1 - Caesar's Cipher

plainnya=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q",
          "R","S","T","U","V","W","X","Y","Z"," "]
ciphernya=["11","22","32","41","31","21","23","24","34","33","43","42","51","52","53",
           "12","13","14","44","54","35","25","15","45","55","Z"," "]

bil_huruf=[]
sente=input("Sentence :")

for i in range(len(sente)):
    for j in range(len(ciphernya)):
        if (sente[i]==" "):
            bil_huruf.append(26)
            break
        
        if i==len(sente)-1:
            break
        else:            
            sentenya=sente[i]+sente[i+1]
            if ciphernya[j]==sentenya:
                bil_huruf.append(j)

print("Result :")
for k in range(len(bil_huruf)):    
    print(plainnya[bil_huruf[k]],end=" ")  

print("\n")       
   
            
        
