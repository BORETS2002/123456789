"""
Tarmoqdan royhatdan o'tish login passwordlarini kiritib tarmoqqa kirish
va login passwordlarini yangilash hamda uchirib tashlash
"""
import os
import sys


class User:
    def __init__(self, user_file_name="user2.txt"):
        os.system("cls")
        self.login = None
        self.password = None
        self.file_name = user_file_name
        self.all_user = []
        self.inital_paje()

    def inital_paje(self):
        enter_sys = input(self.welcome_msg()).strip()
        while not self.file_empty() and enter_sys not in ['1', '2', '3']:
            os.system("cls")
            print("Invalid input ! ")
            enter_sys = input(self.welcome_msg()).strip()

        while self.file_empty() and enter_sys not in ['1', '2']:
            os.system("cls")
            print("Invalid input ! ")
            enter_sys = input(self.welcome_msg()).strip()

        if enter_sys == "1":
            self.register()
        elif not self.file_empty() and enter_sys == "2":
            self.log_in()
        else:
            sys.exit()

    """
    boshlangich kirish qismi
    """

    def main_peg(self):
        os.system('cls')
        menyu_sys = input(self.menyu_msg() + ">>>").strip()

        while menyu_sys not in ["1", "2", "3", "4", "5"]:
            os.system('cls')
            print("Invalid input!")
            menyu_sys = input(self.menyu_msg() + ">>>").strip()
        os.system('cls')
        if menyu_sys == "1":
            self.log_out()
        if menyu_sys == "2":
            self.opdate_login()
        if menyu_sys == "3":
            self.opdate_password()
        if menyu_sys == "4":
            self.delete_account()
        if menyu_sys == "5":
            sys.exit()

    """
    foydalanuvchi ragistratsiadan o'tkandan keyin chiqadigan menyu"""

    def register(self):
        os.system("cls")
        self.get_all_user()
        new_ = []
        name = input("ismingiz:").strip().lower()
        full_name = input("familyangiz: ").strip().lower()
        age = input("yoshingiz: ").strip().lower()
        while not int(age) >= 12:
            os.system("cls")
            print("12+ bolish kerak")
            age = input("yoshingiz: ").strip().lower()

        log_ = input("loginingiz: ").strip().lower()
        while not self.login_is_correct(log_):
            os.system("cls")
            self.wrong_log_msg()
            log_ = input("loginingiz: ").strip().lower()

        pas_ = input("passwordingiz: ").strip()
        while not self.password_is_correct(pas_):
            os.system("cls")
            self.wrong_pasw()
            pas_ = input("passwordingiz: ").strip()
        while self.user_exists(log_, pas_):
            os.system("cls")
            print("bunday accaunt bor !!!")

            log_ = input("loginingiz: ").strip().lower()
            while not self.login_is_correct(log_):
                os.system("cls")
                self.wrong_log_msg()
                log_ = input("loginingiz: ").strip().lower()

            pas_ = input("passwordingiz: ").strip()
            while not self.password_is_correct(pas_):
                os.system("cls")
                self.wrong_pasw()
                pas_ = input("passwordingiz: ").strip()
        pas_tshr = input("tasdiqlovchi password: ").strip()

        while pas_tshr != pas_:
            os.system("cls")
            print("invalid pasword")
            pas_ = input("passwordingiz: ")
            pas_tshr = input("tasdiqlovchi password: ")

        with open(self.file_name) as file:
            for i in file.read().split():
                new_.append(i)

            new_.append(f"name={name}|full_name={full_name}|age={age}|login={log_}|password={pas_}")

        with open(self.file_name, 'w') as file:
            for i in new_:
                file.write(i)
                file.write('\n')
        os.system("cls")
        self.login = log_
        self.password = pas_
        self.get_all_user()
        print("You're successfully registered.")

        self.main_peg()

    """registratsia qismi ismi familyasi yoshi logini va passwordi bolish krk"""

    def log_in(self):
        if self.user_logget_in():
            return
        os.system("cls")
        tmp_login = input("Your login: ").strip()
        tmp_pasword = input("Your password: ").strip()

        while not self.login_is_correct(tmp_login) or not self.password_is_correct(tmp_pasword):
            os.system("cls")
            self.wrong_log_msg()
            tmp_login = input("Your login: ").strip()
            tmp_pasword = input("Your password: ").strip()

        # fayldan hamma userlarni oqib olish kereak
        self.get_all_user()
        if self.user_exists(tmp_login, tmp_pasword):
            print("You are logged in successfully")
            self.login = tmp_login
            self.password = tmp_pasword
        else:
            os.system("cls")
            print("This user does not exist")
            self.all_user.clear()
            self.inital_paje()

    """
    login qismi file da ma'lumoti bor odam kira olishini  yani registerdan o'tkan odam"""

    def log_out(self):
        self.login = None
        self.password = None
        self.all_user.clear()
        self.inital_paje()

    '''
    bosh menu ga qaytib qolish
    '''

    def opdate_login(self):
        if self.user_logget_in():
            with open(self.file_name, 'r+') as file:
                text = file.read()
                new_log = input("new login:").strip()
                while not self.login_is_correct(new_log):
                    os.system("cls")
                    self.wrong_log_msg()
                    new_log = input("new login:").strip()

                with open(self.file_name, 'w') as file:
                    file.write(text.replace("login=" + self.login + "|" + "password=" + self.password,
                                            "login=" + new_log + "|" + "password=" + self.password))
                os.system('cls')
                print("login ozgardi ! ")
                self.log_out()

    '''
    loginni yangilash qismi'''

    def opdate_password(self):
        if self.user_logget_in():
            with open(self.file_name, 'r+') as file:
                text = file.read()
                new_pass = input("new password:").strip()
                while not self.password_is_correct(new_pass):
                    os.system("cls")
                    self.wrong_pasw()
                    new_pass = input("new password:").strip()

                with open(self.file_name, 'w') as file:
                    file.write(text.replace("login=" + self.login + "|" + "password=" + self.password,
                                            "login=" + self.login + "|" + "password=" + new_pass))
                    self.__init__()

    '''passwordni yangilash qismi'''

    def delete_account(self):
        new = input("delete qilishga aminmisiz: [Y/N] ").lower()
        os.system('cls')
        while new not in ['y', 'n']:
            new = input('Siz [Y/N] ni tanlashingiz kerak: ').lower()
            os.system('cls')
        if new == 'n':
            self.log_out()
        else:
            man = self.login
            new_ = []
            with open(self.file_name) as file:
                for i in file.read().split():
                    if man not in i:
                        new_.append(i)
            with open(self.file_name, 'w') as file:
                for i in new_:
                    file.write(i)
                    file.write('\n')

            new_.clear()
            os.system("cls")
            self.login = None
            self.password = None
            self.all_user = []
            print("accaount is deleted seccesfully")
            self.log_out()

    '''bor accauntni butunley o'chirib yuborish'''

    def welcome_msg(self):
        if self.file_empty():
            return """ 
            Please select one of the options below:

            [1] Register
            [2] Exit  
            """
        else:
            return """
            Please select one of the options below:

            [1] Register
            [2] Login
            [3] Exit  
            """

    '''saitdan hechkim royhatdan otmagan bolsa va otgan bolsa chiqadigon  messeg qismi'''

    @staticmethod
    def login_is_correct(login_: str) -> bool:
        return len(login_) > 2 and login_.isalnum()

    '''loginni raqam va harfga tekshiradigon qismi va miqdoriga'''

    @staticmethod
    def password_is_correct(password_: str) -> bool:
        return len(password_) > 5

    '''passwordni miqdorini tekshiradigon qismi'''

    def wrong_log_msg(self):
        print("login or Invalit!")
        print("login should contain at least 3 charactes, [a-z] and/or[0-9]")

    '''login bilan hato yuz berganda chiqadigon messeg'''

    def file_empty(self):
        with open(self.file_name) as file:
            text = file.read()
        return text == ""

    '''file boshligini tekshruvchi qismi'''

    def get_all_user(self):  # hamma foydalanuvchilarni olish
        with open("user2.txt") as file:
            users = file.read()
            for row in users.split():
                self.all_user.append(
                    {
                        "name": row.split("|")[0].split("=")[1],
                        "full_name": row.split("|")[1].split("=")[1],
                        "age": row.split("|")[2].split("=")[1],
                        "login": row.split("|")[3].split("=")[1],
                        "password": row.split("|")[4].split("=")[1]

                    }
                )

    '''file dan hamma foydalanuvchilarni olish qismi'''

    def show_all_user(self):
        [print(user_) for user_ in self.all_user]
        """
        hamma userlarni txt file dan yigib oluvchi funcion
        :return: qaytarmaydi
        """

    def user_exists(self, login_: str, password_: str) -> bool:
        for user__ in self.all_user:
            if user__["login"] == login_ and user__["password"] == password_:
                return True
        return False

    def user_logget_in(self):
        return self.login is not None and self.password is not None

    '''foydalanuvchi tarmoqdami yoqmi tekshiruvhi'''

    def menyu_msg(self):
        return """
                  Menu:
                  [1] log Out
                  [2] Change login
                  [3] Change Password
                  [4] Delete account
                  [5] Exit
                  """

    '''foydalanuvhi registerdan otkandan keyin chiqadigon menyusini messegi '''

    def wrong_pasw(self):
        print("Password should contain at lest 6 characters")

    '''password xato bolganda messeg beradigon funcion'''


person = User()
person.main_peg()
