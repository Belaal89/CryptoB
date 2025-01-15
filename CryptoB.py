import threading
import secrets
import hashlib
import random
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.properties import ObjectProperty

Window.clearcolor=(100/255.0,0,1,1)
Window.size=(400,630)
class MainWindow(Screen):
     pass
class SecondWindow(Screen):#generates a random 1000065 letters and saves it in a file called lib.txt
     generate = ObjectProperty(None)
     back_win2 = ObjectProperty(None)
     def gen(self):
          
     

          def getst1():
               st1 = 'G'
               with open("result.txt", "w") as file:
                         file.write(st1)
               stringlist = [" ","!",'"','#',"$",'%',"&","'","(",")","*","+",",","-",".","/","0","1","2","3","4","5","6","7","8","9",":",
                             ";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U",
                             "V","W","X","Y","Z","[","\\","]","^","_","`","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
                             "q","r","s","t","u","v","w","x","y","z","{","|","}","~" ]
               digilist = [10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,
                           10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,
                           10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,
                           10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,
                           10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,10527,
                           10527,10527,10527,10527,10527]
               count=0
               collector =""
               while digilist != [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]:
                    rand = secrets.choice(stringlist)
                    if digilist[stringlist.index(rand)] != 0:
                         collector = collector + rand
                         count = count + 1
                         digilist[stringlist.index(rand)] = digilist[stringlist.index(rand)]-1
               st1 = 'D'
               with open("result.txt", "w") as file:
                         file.write(st1)
               return collector
        
          def run():
               
               st1 = getst1()
               with open("lib.txt", "w") as file:
                         file.write(st1)
               self.generate.text = "Generate"
               self.generate.disabled = False
               self.back_win2.disabled = False
          t1 = threading.Thread(target = run)
          t1.start()
          self.generate.text = "loading . . . "
          self.generate.disabled = True
          self.back_win2.disabled = True
     
               
          
               
          ###########
         
         
          
          
     pass
class ThirdWindow(Screen):#Eencryptor
     encrypt_button = ObjectProperty(None)
     back_win3 = ObjectProperty(None)
     def enc(self,password):
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
                         comma_list.append(random.choice(list_of_not_result))
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
                    self.encrypt_button.text = "Encrypt"
                    self.encrypt_button.disabled = False
                    self.back_win3.disabled = False
               t1 = threading.Thread(target = go_encrypt)
               t1.start()
               self.encrypt_button.text = "Loading . . ."
               self.encrypt_button.disabled = True
               self.back_win3.disabled = True
     pass
class FourthWindow(Screen):#Decryptor
     decrypt_button = ObjectProperty(None)
     password_input = ObjectProperty(None)
     back_win4 = ObjectProperty(None)
     def de_enc(self):
               
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
                    num =0
                    for i in range(len(newmerjlist)):
                         addresult= addresult +list1[newmerjlist[i]]
                    return addresult
               
               def decrypt_message(string,lib): #this is the encryptor function
                    list = string.split(",")
                    decrypted_message=""
                    for i in range(len(list)):
                         if list[i] !='' and int(list[i]) <= len(lib) :
                              decrypted_message = decrypted_message + lib[int(list[i])]
                    return decrypted_message

               def rev_M_redd (string,decrypted_lib):
                    '''To transform letters to numbers'''
                    string_lib = decrypted_lib
                    string_alpha = "abcdefghijklmnopqrstuvwxyz"
                    string_result = ""
                    #take 10 diffirent letters ordered as decrypted lib
                    for i in range(len(string_lib)):
                         if string_lib[i] in string_alpha and string_lib[i]  not in string_result:
                              string_result = string_result + string_lib[i]
                         if len(string_result) == 10:
                              break
                    #########################
                    #take the other letters and save them in string_not_result
                    string_not_result = ""
                    for i in range(len(string_alpha)):
                         if string_alpha[i] not in string_result :
                              string_not_result = string_not_result + string_alpha[i]
                    ##########################
                    string_final = ""
                    for i in range(len(string)):
                         if string[i] in string_result:
                              for u in range(len(string_result)):
                                   if string[i]== string_result[u] :
                                        string_final = string_final + str(u)
                                        break
                         else:
                              if string[i] in string_not_result:
                                   if len(string_final) >= 1 and string_final[-1] != ',':
                                        string_final = string_final +","
                         
                    return string_final

                    ##########START THE SENARIO #########

               def run_ ():
                    
                    with open("cipher.txt") as message :
                         Message = message.readlines()
                    list =[]
                    encrypted_lib = get_encrypted_lib () #read lib.txt and put it in a string
                    for line in Message :
                         if line !='':
                              list.append(line)
                    decrypted_lib = get_decrypted_lib (encrypted_lib,get_pass_hash(self.password_input.text))
                    final_res = ""
                    for i in range (len(list)):
                         Message_ = rev_M_redd (list[i].strip(),decrypted_lib)
                         decrypted_message = ""
                         decrypted_message = decrypted_message+decrypt_message(Message_,decrypted_lib)
                         final_res = final_res + decrypted_message + "\n"
                    #return final_res.strip()
                    with open("result.txt", "w") as file:
                              file.writelines(final_res)
                    self.decrypt_button.disabled = False
                    self.decrypt_button.text = "De-crypt"
                    self.back_win4.disabled = False
          ######################
               t1 = threading.Thread(target=run_)
               self.decrypt_button.disabled = True
               self.decrypt_button.text = "Loading . . ."
               self.back_win4.disabled = True
               t1.start()
     
               
               
               

     pass
class WindowManager(ScreenManager):
     pass
class FifthWindow(Screen):
     def Savetoplain (self,message):
          with open("plain.txt", "w") as file:
                         file.write(message)
     pass

kv = Builder.load_file('my.kv')

class MyMainApp(App):
    
    def build(self): 
        '''test'''
        string_1 = "my first android app !!"
        self.title=string_1
        return kv
if __name__=='__main__':
        MyMainApp().run()

