import threading
import secrets
import hashlib
import random
def enc(password):
               def get_pass_hash(string): #to take only numbers from the hash
                    st2=bytes(string, encoding= 'utf-8')
                    h = hashlib.new("SHA256")
                    h.update(st2)
                    hashstring= h.hexdigest()
                    final=""
                    for i in range(len(hashstring)):
                         if hashstring[i]>='0' and hashstring[i]<='9':
                              final= final+hashstring[i]
                    return final
                          
               def get_encrypted_lib (): #read lib.txt and put it in a string
                    string = ""
                    with open("lib.txt", "r") as file:
                         string =file.read()
                    return string.strip()

               def get_char (char): #this is used in decrypted_message function
                    ch =0
                    list1 = " "+"!"+'"'+"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
                    for i in range (len(list1)):
                         if char == list1[i]:
                              ch=i
                    return ch

               def get_decrypted_lib (lib,hash):
                    list1 = " "+"!"+'"'+"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
                    listlib =lib
                    newhashlist = []
                    newlist2 = []
                    for i in range (len(listlib)):
                         newhashlist.append(int( hash[i%len(hash)]))
                    for i in range(len(listlib)):
                         newlist2.append(listlib[i])
                    newchlist=[]
                    for i in range(len(listlib)):
                         newchlist.append(get_char(listlib[i]))
                    #newchlist
                    newmerjlist =[]
                    for i in range(len(newhashlist)):
                         hashchar = int(newhashlist[i])
                         char = int(newchlist[i])
                         newmerjlist.append((char - hashchar)%len(list1))
                    addresult =""
                    for i in range(len(newmerjlist)):
                         addresult= addresult +list1[newmerjlist[i]]
                    return addresult

               def get_char_number(lib,char):#this is used in encrypt_message() function
                    count=[]
                    result=""
                    for i in range(len(lib)):
                         if lib[i] == char:
                              count.append(str(i))
                    result = grandom(count)
                    return result

               def get_numbers(st,lib): #this is used in encrypt_message() function
                    str=""
                    for i in range(len(st)):
                         if i == 0:
                              str =get_char_number(lib,st[i])

                         else:
                              str = str +","+get_char_number(lib,st[i])
                    return str
               
               def grandom (list):
                    li1,li2,li3 ,li4,li5,li6 = ([],)*6
                    fli = []
                    for i in list:
                         if len(i)==1:
                              li1.append(i)
                         elif len(i)==2:
                              li2.append(i)
                         elif len(i)==3:
                              li3.append(i)
                         elif len(i)==4:
                              li4.append(i)
                         elif len(i)==5:
                              li5.append(i)
                         elif len(i)==6:
                              li6.append(i)
                    if len(li3) > 0:
                         fli.append(secrets.choice(li3))
                    if len(li5) > 0:
                         fli.append(secrets.choice(li5))
                    if len(li6) > 0:
                         fli.append(secrets.choice(li6))
                    if len(li4) > 0:
                         fli.append(secrets.choice(li4))
                    if len(li1) > 0:
                         fli.append(secrets.choice(li1))
                    if len(li2) > 0:
                         fli.append(secrets.choice(li2))
                    string = random.choice(fli)
                    return string
               
               def encrypt_message(string,lib): #this is the encryptor function
                    encryted_message = get_numbers(string,lib)
                    return encryted_message

               def enc_M_redd (string,decrypted_lib):
                    string_lib =decrypted_lib
                    string_alpha = "abcdefghijklmnopqrstuvwxyz"
                    numbers = "0123456789"
                    #take 10 diffirent letters ordered as decrypted lib and save it in sring_result
                    string_result=""
                    for i in range(len(string_lib)):
                         if string_lib[i] in string_alpha and string_lib[i]  not in string_result:
                              string_result = string_result + string_lib[i]
                         if len(string_result) == 10:
                              break
                     #take the other letters and save them in string_not_result
                    string_not_result = ""
                    for i in range(len(string_alpha)):
                         if string_alpha[i] not in string_result :
                              string_not_result = string_not_result + string_alpha[i]
                    ##get number of commas
                    No_comma = 0
                    for i  in range(len(string)) :
                         if string [i]==',':
                              No_comma = No_comma + 1
                    ##########get a list not result group ############
                    list_of_not_result = []
                    for i in range(0,len(string_not_result)):
                         list_of_not_result.append(string_not_result[i])
                    ##############take random comma represntation from prev list
                    comma_list = []
                    for i in range(0,No_comma):
                         comma_list.append(secrets.choice(list_of_not_result))
                    ##########save the final result in "final_result" variable
                    final_result =''
                    comma_counter = 0
                    for i in range (len(string)) :
                         if string[i] in numbers:
                              final_result = final_result + string_result[int(string[i])]
                         else:
                              final_result = final_result + str(comma_list[comma_counter])
                              comma_counter = comma_counter + 1
                    return final_result




               ########## THE SENARIO #########
               def run(message,password):
                    encrypted_lib = get_encrypted_lib () #read lib.txt and put it in a string
                    decrypted_lib = get_decrypted_lib (encrypted_lib,get_pass_hash(password))
                    encrypted_message = encrypt_message(message,decrypted_lib)
                    encoded_message = enc_M_redd(encrypted_message,decrypted_lib)
                    #####store to a file###
                    with open("cipher.txt", "a") as file:
                              file.writelines(encoded_message+"\n")
               def go_encrypt ():
                    string_ = ""
                    with open("plain.txt", "r") as file:
                         string_ =file.readlines()
                    for line in string_:
                         run(line.rstrip(),password)
                    
               t1 = threading.Thread(target = go_encrypt)
               t1.start()
enc('123')
     