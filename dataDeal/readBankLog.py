# -*- coding: cp936 -*-
import re
import os
import codecs
receiveAUser=r' recv kahaoo '
serviceType=""
file=open(r'C:\Users\Administrator\Desktop\��������\bankLog\ylk_err20150825.err20150825')
lines=file.readline()
class User:

    def __init__(self,serviceType,kahao,area,jiaoYiJinE,status,reasion):
        self.serviceType=serviceType
        self.kahao=kahao
        self.area=area
        self.jiaoYiJinE=jiaoYiJinE
        self.status=status
        self.reasion=reasion
    def displayUser(self):
        print "\n"
        print " tradeType��",self.serviceType, " cadeNumber��",self.kahao," area��",self.area," tradeAmount��",self.jiaoYiJinE,"status:",self.status,"reasion:",self.reasion
users=[] #�û����飬���Դ���û���Ϣ����¼��ʱ����û���Ϣ
while lines:
    linePart=lines.split()
    if re.search(receiveAUser,lines):   #�����鵽���û����׾ʹ����û�����
        lineSplit=lines.split()
        user=User("","","",0,"","")
        kahao=lineSplit[6][1:20]
        area=lineSplit[8]
        user.kahao=kahao
        user.area=area
        user.jiaoYiJinE=0
        if len(users)==0:
            users.append(user)
        isHere=False
        for us in users:
            if us.kahao==kahao:
                isHere=True
                break
        if not isHere:
            users.append(user)


    if re.search(r':Begin',lines):
        for user0 in users:
            if re.search(user0.kahao,lineSplit[3]):
                user=user0
                users.append(user)
                break

    if re.search(r':End',lines):
        lineSplit=lines.split()
        serviceType=lineSplit[2][:lineSplit[2].index(':')]
        if re.search(r'Success!',lines):
            for user1 in users:
                if re.search(user1.kahao,lineSplit[3]):
                    user1.serviceType=serviceType
                    user1.status="succeed"
                    user1.reasion="succeed"
                if re.search(r',',lineSplit[3]):
                    user1.jiaoYiJinE=float(lineSplit[3][lineSplit[3].index(',')+1:len(lineSplit[3])-2])
                else:
                    user1.jiaoYiJinE=0
                user1.displayUser()
                users.remove(user1)
                break
        if re.search(r'Failed,',lines):
            for user in users:
                if re.search(user.kahao,lineSplit[3]):
                    user.serviceType=serviceType
                    user.status="failded"
                    user.reasion=serviceType+"ʧ��"
                    user.jiaoYiJinE=0
                    user.displayUser()
                    users.remove(user)
                    break
    if re.search(r'����',lines):
        lineSplit2=lines.split()
        for user2 in users:
            if re.search(user2.kahao,lines):
                user2.status="failed"
                user2.serviceType="����ʧ��"
                user2.reasion=lineSplit2[4]
                user2.displayUser()
                users.remove(user2)
                break
    lines=file.readline()
file.close()




