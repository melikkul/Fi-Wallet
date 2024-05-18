import pandas as pd
from datetime import datetime

class UserRegistration:
    def __init__(self, file_path):
        self.file_path = file_path

    def setup_database(self):
        """
        Veritabanı dosyasını oluşturur veya mevcut dosyayı okur.
        """
        try:
            df = pd.read_excel(self.file_path)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['UserID', 'FirstName', 'LastName', 'Email', 'Password'])
            df.to_excel(self.file_path, index=False)


    def generate_user_id(self):
        """
        Kullanıcı ID'si oluşturur. Bu ID kayıt yılı, ayı, günü, saati ve saniyeyi içerir.
        """
        now = datetime.now()
        user_id = now.strftime('%Y%m%d%H%M%S')
        return user_id

    def register_user(self, first_name, last_name, email, password):
        """
        Yeni bir kullanıcı kaydeder.
        :param first_name: Kullanıcının adı
        :param last_name: Kullanıcının soyadı
        :param email: Kullanıcının e-posta adresi
        :param password: Kullanıcının şifresi
        """
        user_id = self.generate_user_id()
        new_user = {
            'UserID': user_id,
            'FirstName': first_name,
            'LastName': last_name,
            'Email': email,
            'Password': password
        }
        
        try:
            df = pd.read_excel(self.file_path)
            new_user_series = pd.Series(new_user)
            df = df.append(new_user_series, ignore_index=True)
            df.to_excel(self.file_path, index=False)
            print(f"Yeni kullanıcı başarıyla kaydedildi: {user_id}")
        except Exception as e:
            print(f"Kullanıcı kaydedilirken hata oluştu: {e}")

    def authenticate_user(self, username, password):
        #Kullanıcı doğrulaması
        try:
            df = pd.read_excel(self.file_path)
            user = df[(df['Email'] == username) & (df['Password'] == password)]
            if len(user) > 0:
                return True
            else:
                return False
        except Exception as e:
            print(f"Kullanıcı doğrulanırken hata oluştu: {e}")
            return False
        
if __name__ == "__main__":
    user_reg = UserRegistration("user_database.xlsx")
    user_reg.setup_database()
    
    user_reg.register_user()
    
    is_authenticated = user_reg.authenticate_user("", "")
    print(f"Kullanıcı girişi {'başarılı' if is_authenticated else 'başarısız'}.")