from card import Card
from user import User
import random

class ATM(object):
    def __init__(self, allUsers):
        self.allUsers = allUsers  #卡号-用户
    #开户
    def createUser(self):
        #目标：向用户自字典中添加一对键值对(卡号-用户)
        name   = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phone  = input("请输入您的电话号码：")
        # 请输入预存款金额
        prestoreMoney = int(input("请输入预存款金额："))
        if prestoreMoney < 0:
            print("预存款输入有误！！开户失败......")
            return -1
        # 请设置密码
        onepassword = input("请设置密码")
        #验证密码
        if not self.checkPasswd(onepassword):
            print("密码输入有误！！开户失败......")
            return -1
        #所有需要的信息就全了
        cardStr = self.randomCardId()
        card = Card(cardStr,onepassword,prestoreMoney)
        user = User(name,idCard,phone,card)
        #存到字典
        self.allUsers[cardStr] = user
        print("开户成功！！请牢记卡号（%s）..." %(cardStr))
        


    #查询
    def searchUserInfo(self):
        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        # 验证是否存在改卡号
        if not user:
            print("该卡号不存在！！查询失败")
            return -1
        # 判断是否锁定
        elif user.card.cardLock:
            print("该卡已被锁定！！请解锁后在进行其他操作......")
            return -1
        # 验证密码
        elif not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误！！该卡已被锁定！！请解锁后进行其他操作......")
            user.card.cardLock = True
            return -1
        print("帐号：{} 余额：{}".format(user.card.cardId,user.card.cardMoney))


    #取款
    def getMoney(self):
        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        # 验证是否存在改卡号
        if not user:
            print("该卡号不存在！！查询失败")
            return -1
        # 判断是否锁定
        elif user.card.cardLock:
            print("该卡已被锁定！！请解锁后在进行其他操作......")
            return -1
        # 验证密码
        elif not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误！！该卡已被锁定！！请解锁后进行其他操作......")
            user.card.cardLock = True
            return -1
        # 验证账户余额和金额是否正确
        money = input("请输入取款金额：")
        if money > user.card.cardMoney:
            print("余额不足！！取款失败......")
            return -1
        if money <= 0:
            print("输入错误！！取款失败......")
            return -1
        #取款
        user.card.cardMoney -= money
        print("取款成功！！ 余额：{}".format(user.card.cardMoney))
        
    #存款
    def saveMoney(self):
        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        # 验证是否存在改卡号
        if not user:
            print("该卡号不存在！！查询失败")
            return -1
        # 判断是否锁定
        elif user.card.cardLock:
            print("该卡已被锁定！！请解锁后在进行其他操作......")
            return -1
        # 验证密码
        elif not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误！！该卡已被锁定！！请解锁后进行其他操作......")
            user.card.cardLock = True
            return -1
        money = input("请输入取款金额：")
        if money <= 0:
            print("输入错误！！取款失败......")
            return -1
        # 存款
        user.card.cardMoney += money
        print("取款成功！！ 余额：{}".format(user.card.cardMoney))
    #转账
    def transferMoney(self):
        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        # 验证是否存在改卡号
        if not user:
            print("该卡号不存在！！查询失败")
            return -1
        # 判断是否锁定
        elif user.card.cardLock:
            print("该卡已被锁定！！请解锁后在进行其他操作......")
            return -1
        # 验证密码
        elif not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误！！该卡已被锁定！！请解锁后进行其他操作......")
            user.card.cardLock = True
            return -1
        goal_CarID = input("输入你想转的帐号：")
        goal_User = self.allUsers.get(goal_CarID)
        if not goal_User:
            print("该卡号不存在")
            return -1
        elif goal_User.card.cardLock:
            print("该卡已被锁定！！请解锁后在进行其他操作......")
            return -1
        money = int(input("请输入转账金额："))
        if money > user.card.cardMoney:
            print("余额不足！！取款失败......")
            return -1
        if money < 0:
            print("输入错误！！取款失败......")
            return -1
        user.card.cardMoney -= money
        goal_User.card.cardMoney += money
        print("转账成功,转账金额为:{}".format(money))
        print("您的余额：{}".format(user.card.cardMoney))
    #改密
    def changePasswd(self):
        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        # 验证是否存在改卡号
        if not user:
            print("该卡号不存在！！查询失败")
            return -1
        # 判断是否锁定
        elif user.card.cardLock:
            print("该卡已被锁定！！请解锁后在进行其他操作......")
            return -1
        # 验证密码
        elif not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误！！该卡已被锁定！！请解锁后进行其他操作......")
            user.card.cardLock = True
            return -1
        inputcount = 0
        while inputcount <3:
            new_password = input("输入您的新密码：")
            inputcount += 1
            print("再次输入您的新密码")
            if not self.checkPasswd(new_password):
                print("三次输入输入失败，修改密码失败")
                return -1
            print("修改成功")
            user.card.cardPasswd = new_password
            break
    #锁定
    def lockUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在改卡号
        user = self.allUsers.get(cardNum)
        if user.card.cardLock:
            print("该卡已被锁定！！请解锁后在使用其他功能……")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！锁定失败……")
            return -1

        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！！锁定失败……")
            return -1

        #锁它
        user.card.cardLock = True
        print("锁定成功……")

    #解锁
    def unlockUser(self):
        cardNum = input("请输入您的卡号：")
        # 验证是否存在改卡号
        user = self.allUsers.get(cardNum)
        if not user:
            print("该卡号不存在！！解锁失败……")
            return -1

        if not user.card.cardLock:
            print("该卡没有锁定!!无需解锁……")
            return -1

        if not self.checkPasswd(user.card.cardPasswd):
            print("密码输入错误！！解锁失败……")
            return -1

        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！！解锁失败……")
            return -1

        #解锁
        user.card.cardLock = False
        print("解锁成功……")

    #补卡
    def newCard(self):
        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        # 验证是否存在改卡号
        if not user:
            print("该卡号不存在！！查询失败")
            return -1
        # 判断是否锁定
        elif user.card.cardLock:
            print("该卡已被锁定！！请解锁后在进行其他操作......")
            return -1
        # 验证密码
        elif not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误！！该卡已被锁定！！请解锁后进行其他操作......")
            user.card.cardLock = True
            return -1
        print("补卡申请以提交,请等候短信通知")
    #销户
    def killUser(self):
        cardNum = input("请输入您的卡号：")
        user = self.allUsers.get(cardNum)
        # 验证是否存在改卡号
        if not user:
            print("该卡号不存在！！查询失败")
            return -1
        # 判断是否锁定
        elif user.card.cardLock:
            print("该卡已被锁定！！请解锁后在进行其他操作......")
            return -1
        # 验证密码
        elif not self.checkPasswd(user.card.cardPasswd):
            print("密码输入有误！！该卡已被锁定！！请解锁后进行其他操作......")
            user.card.cardLock = True
            return -1
        del self.allUsers[cardNum]
        print("销户成功")

    #验证密码
    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码：")
            if tempPasswd == realPasswd:
                return True
        return False

    #生成卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch
            #判断是否重复
            if not self.allUsers.get(str):
                return str



