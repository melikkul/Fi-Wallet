import pandas as pd
import os
from datetime import datetime

class Data:
    def __init__(self, file_path):
        self.file_path = file_path
        # Eğer dosya mevcut değilse, boş bir DataFrame oluşturarak dosyayı oluştur
        if not os.path.exists(file_path):
            self.data = pd.DataFrame(columns=['userID', 'firstName', 'lastName', 'eMail', 'password', 'keepMeSign'])
            self.save()
        else:
            self.load_data()

    def load_data(self):
        self.data = pd.read_excel(self.file_path)
        self.columns = self.data.columns.tolist()
        for column in self.columns:
            setattr(self, column.lower(), self.data[column])

    def search_db(self, email):
        found = self.data[self.data['eMail'] == email]
        if not found.empty:
            password = found['password'].iloc[0]
            input_password = input("Enter password for validation: ")
            if input_password == password:
                print("Password is correct.")
            else:
                print("Password is incorrect.")
        else:
            print("E-mail not found in the database.")

    def sign_db(self, email, password):
        found = self.data[self.data['eMail'] == email]
        if not found.empty:
            if found['password'].iloc[0] == password:
                print("Login successful.")
                return True
            else:
                print("Incorrect password.")
        else:
            print("E-mail not found in the database.")
        return False

    def update_db(self, name, surname, email, password):
        # E-posta benzersiz mi kontrol et
        if email in self.data['eMail'].values:
            print("Error: This email is already registered.")
            return 0
        

        new_data = {'userID': [], 'firstName': [], 'lastName': [], 'eMail': [], 'password': [], 'keepMeSign': []}
        for column in self.columns:
            if column.lower() == 'userid':
                current_time = datetime.now()
                id_value = current_time.strftime('%y%m%d%H%M%S%f')
                new_data['userID'].append(id_value)
            elif column.lower() == 'firstname':
                new_data['firstName'].append(name)
            elif column.lower() == 'lastname':
                new_data['lastName'].append(surname)
            elif column.lower() == 'email':
                new_data['eMail'].append(email)
            elif column.lower() == 'password':
                new_data['password'].append(password)
            elif column.lower() == 'keepmesign':
                new_data['keepMeSign'].append(None)
            else:
                print(f"Column {column} not found in the database.")
        
        # Yeni verileri DataFrame'e ekleyin
        new_entries_df = pd.DataFrame(new_data)
        self.data = pd.concat([self.data, new_entries_df], ignore_index=True)

        # Veritabanını kaydet
        self.save()
        return 1

    def save(self):
        # Veritabanını Excel dosyasına kaydetme
        self.data.to_excel(self.file_path, index=False)

# Kullanım örneği:
# Dosya yolu ile bir Data nesnesi oluşturulur
database = Data('firmy_db.xlsx')
