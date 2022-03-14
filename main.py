
"""
Tarmoqdan royhatdan o'tish login passwordlarini kiritib tarmoqqa kirish
va login passwordlarini yangilash hamda uchirib tashlash
"""

class User:
    def __init__(self, user_file_name="user2.txt"):
        self.login = None
        self.password = None
        self.file_name = user_file_name
        self.all_user = []

    def inital_paje(self):
        pass
    """
    boshlangich kirish qismi
    """

    def main_peg(self):
        pass
    """
    foydalanuvchi ragistratsiadan o'tkandan keyin chiqadigan menyu"""

    def register(self):
        pass

    """registratsia qismi ismi familyasi yishi logini va passwordi bolish krk"""

    def log_in(self):
        pass
    """
    login qismi file da ma'lumoti bor odam kira olishini  yani registerdan o'tkan odam"""

    def log_out(self):
        pass
    '''
    bosh menu ga qaytib qolish
    '''

    def  opdate_login(self):
        pass
    '''
    loginni yangilash qismi'''

    def opdate_password(self):
        pass
    '''passwordni yangilash qismi'''

    def delete_account(self):
        pass
    '''bor accauntni butunley o'chirib yuborish'''

    def welcome_msg(self):
        pass
    '''saitdan hechkim royhatdan otmagan bolsa va otgan bolsa chiqadigon  messeg qismi'''

    @staticmethod
    def login_is_correct(login_: str) -> bool:
        pass
    '''loginni raqam va harfga tekshiradigon qismi va miqdoriga'''

    @staticmethod
    def password_is_correct(password_: str) -> bool:
        pass
    '''passwordni miqdorini tekshiradigon qismi'''

    def wrong_log_msg(self):
        pass
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
        pass
        """
        hamma userlarni txt file dan yigib oluvchi funcion
        :return: qaytarmaydi
        """

    def user_exists(self):
        '''foydalanuvhi bormi yoqmi tekshiruvchi funcion'''

    def user_logget_in(self):
        pass
    '''foydalanuvchi tarmoqdami yoqmi tekshiruvhi'''

    def menyu_msg(self):
        pass
    '''foydalanuvhi registerdan otkandan keyin chiqadigon menyusini messegi '''

    def wrong_pasw(self):
        pass
    '''password xato bolganda messeg beradigon funcion'''