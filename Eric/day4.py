#Day4-check passport fields
#NOTE! I added a line to the end of the input, as my code reads the empty line as when to count a passport, so it needs it.
import re

f=open("input_day4.txt")
lines=f.readlines() #read in each line
f.close()
#print("lines\n",lines)
length=0
passpt=[]
for row in lines:
    passpt.append(str(row))  #move into new list for easier manipulation
#print("pspt\n",pspt)

length=len(passpt)
def counter(pspt):
    valid=0
    count=0
    passport=" "
    num=0
    inv=0
    num=0
    eyrc=" "
    byrc=" "
    iyrc=" "
    hgtc=" "
    hclc=" "
    eclc=" "
    pidc=" "
    temp=" "
    lis=[]
    i=0
    val=0

    for row in pspt:
#       print("The row is:",row)
        temp=""
        if(row!='\n'):

#           print("this works")
            #print(row)
            passport=passport+row
            #passport=passport.replace(r'\n','-')
            #passport=passport.replace(r'\r','-')
           

            #temp=re.sub((\r),'-',passport)


            #print("passport:",passport)
            
            lis=passport.split(":")
            #print("list:",lis)

            for row in lis:
                row=row.replace('\n',' ')
                #print("attempt:",row)
                temp=temp+str(row)
                #printi("temp",temp)
            #print("or this:",temp)
            passport=temp

        else:
#           print("this also works")
            #passport.replace("\n","-") 
            print("the passport is:",passport)
        #since it is now the end of the passport, we will check if the things are present:
            num=num+1
            ecl=passport.find("ecl")
#           print("ecl:",ecl)
            pid=passport.find("pid")
#           print("pid",pid)
            eyr=passport.find("eyr")
            hcl=passport.find("hcl")
            byr=passport.find("byr")
            iyr=passport.find("iyr")
            hgt=passport.find("hgt")
            cid=passport.find("cid")

            
            #now the if to report it:
        
            #if any but cid are -1, return whether valid
        
            if(ecl==-1 or pid == -1 or eyr ==-1 or hcl ==-1 or byr == -1 or iyr ==-1 or hgt ==-1):
                inv=inv+1
                print("This passport is invalid! Go home!","count is:",inv)

            else:

#Part2:check for valid information:
#byr=1920-2002
#iyr=2010-2020
#eyr=2020-2030
#hgt=150cm-193cm or 59in-76in
#hcl=# followed by 6 characters, 0-9 or a-f
#ecl=amb,blu,brn,gry,grn,hzl,oth
#pid=9 digits, including leading 0s
#cid=ignore
                print("ECL:",ecl,"PID:",pid,"EYR:",eyr,"HCL:",hcl,"BYR:",byr,"IYR:",iyr,"HGT:",hgt,"CID:",cid)
                #byrc=passport.split(":")
                #print("content:",byrc)
                #attempted this, but wasn't getting anywhere...
                
                byrc=re.findall('(?<=byr)\d{4}',passport)
                print("BYRC:",byrc)
                if not byrc:
                    inv+=1
                    clean()
                    continue


                iyrc=re.findall('(?<=iyr)\d{4}',passport)
                print("IYRC:",iyrc)
                if not iyrc:
                    inv+=1
                    clean()
                    continue
                
                eyrc=re.findall('(?<=eyr)\d{4}',passport)
                print("EYRC:",eyrc)
                if not eyrc:
                    inv+=1
                    clean()
                    continue

                hgtc=re.findall('\d+(?=cm)',passport)
                if not hgtc:
                    hgtc=re.findall('\d+(?=in)',passport)
                print("HGTC:",hgtc)
                
                hclc=re.findall('(?<=hcl#)\w+',passport)
                print("HCLC:",hclc)
                if not hclc: 
                    inv+=1
                    clean()
                    print(hclc)
                    continue

                eclc=re.findall('(?<=ecl)(amb|blu|brn|gry|grn|hzl|oth)',passport)
                print("ECLC:",eclc)
                if not eclc:
                    eclc="-"
                    inv+=1
                    clean()
                    continue
                
                pidc=re.findall('(?<=pid)\d{9}',passport)
                print("PIDC:",pidc)
                if not pidc:
                    #print("uhoh",pidc)
                    #pidc="-"
                    inv+=1
                    clean()
                    continue



#now do the checks on each:

                if(int(byrc[0])>=1920 and int(byrc[0])<=2002): 
                    val+=1
                    print("byrc",val)
                if(int(iyrc[0])>=2010 and int(iyrc[0])<=2020): 
                    val+=1
                    print("iyrc",val)
                if(int(eyrc[0])>=2020 and int(eyrc[0])<=2030): 
                    val+=1
                    print("eyrc:",val)
                if(len(str(hgtc[0]))==3):#if the length is 5, then 
                    if(int(hgtc[0])>=150 and int(hgtc[0])<=193):
                        val+=1
                        print("hgtc cm",val)
                    else:
                        inv+=1
                        clean()
                        continue
                else:
                    if(int(hgtc[0])>=59 and int(hgtc[0])<=93):
                        print("hgtc",hgtc)
                        val+=1
                        print("hgtc in",val)
                    else:
                        inv+=1
                        clean()
                        continue

                if(len(hclc[0])==6):#the length==6, so take whatever, will need to check for 
                    hclc=re.findall('(?<=hcl#)([a-f]|[0-9])',passport)
                    print("HCLC:",hclc)
                    #print("check this!",hclc)
                    if hclc:
                        val+=1
                        print("hclc",val)
                    else:
                        inv+=1
                        clean()
                        print(hclc)
                        continue
                    
                if(len(str(eclc[0]))==3):
                    val+=1
                    print("eclc",val)
            #    print(pidc[0])
                if(len(str(pidc[0]))==9):
                    val+=1
                    print("pidc",val)
                else:
                    inv+=1
                    clean()
                    print(pidc)
                    continue

            #   print("val:",val)
                




                if((val%7)==0):
                    valid=valid+1
                print("This passport is valid! Go on through!","Number of valid is:",valid)
                #ecl=0,pid=0,eyr=0,hcl=0,byr=0,iyr=0,hgt=0,cid=0


            #print("no longer this passport:",passport)
            passport=" "
            eyrc=" "
            byrc=" "
            iyrc=" "
            hgtc=" "
            hclc=" "
            eclc=" "
            pidc=" "
        num=num+1
        print("num",num)
        if(num==250): break

    print("The number of passports is",num)
    print("the number valid is:",valid)
    print("the number invalid is:",inv)

def clean():
    passport=" "
    eyrc=" "
    byrc=" "
    iyrc=" "
    hgtc=" "
    hclc=" "
    eclc=" "
    pidc=" "





counter(passpt)

def bulkcomment():
    """
    num=num+1
    if(num==5):break


    if(row!=""):
        passport=passport+row
        print("This passport is:",passport)
    else:
        print("This passport WAS:",passport)
        passport=""
        print("Passport now:",passport,"!")
        
    ecl=passport.find("ecl")
    print(ecl)
    pid=passport.find("pid")
    print(pid)
    eyr=passport.find("eyr")
    hcl=passport.find("hcl")
    byr=passport.find("byr")
    iyr=passport.find("iyr")
    hgt=passport.find("hgt")
    cid=passport.find("cid")

    print("ECL:",ecl,"PID:",pid,"EYR:",eyr,"HCL:",hcl,"BYR:",byr,"IYR:",iyr,"HGT:",hgt,"CID:",cid)
    #if any but cid are -1, return whether valid
    if(ecl==-1 or pid == -1 or eyr ==-1 or hcl ==-1 or byr == -1 or iyr ==-1 or hgt ==-1):
        inv=inv+1
        print("This passport is invalid! Go home!","count is:",inv)
        continue
    else:
        valid=valid+1
        print("This passport is valid! Go on through!","Number of valid is:",valid)
#        ecl=0,pid=0,eyr=0,hcl=0,byr=0,iyr=0,hgt=0,cid=0
        continue

    print("The number of passports is",count)
    print("the number valid is:",valid)
    print("the number invalid is:",inv)

                    eyrc=eyrc+passport[eyr+4]+passport[eyr+5]+passport[eyr+6]
                #print("EYR Content:",eyrc)
                byrc=byrc+passport[byr+4]+passport[byr+5]+passport[byr+6]+passport[byr+7]
                #print("BYR Content:",byrc)
                iyrc=iyrc+passport[iyr+4]+passport[iyr+5]+passport[iyr+6]+passport[iyr+7]
                hgtc=hgtc+passport[hgt+4]+passport[hgt+5]+passport[hgt+6]+passport[hgt+7]+passport[hgt+8]+passport[hgt+9]
                eclc=eclc+passport[ecl+4]+passport[ecl+5]+passport[ecl+6]
                pidc=pidc++passport[pid+4]+passport[pid+5]+passport[pid+6]+passport[pid+7]+passport[pid+8]+passport[pid+9]+passport[pid+10]+passport[pid+11]+passport[pid+12]



    """
