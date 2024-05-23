import pandas as pd
import os
from datetime import datetime

class Data:
    def __init__(self, file_path):
        self.file_path = file_path
        self.columns = ['userID', 'firstName', 'lastName', 'eMail', 'password', 'keepMeSign', 'keepMeSignCount']
        if not os.path.exists(file_path):
            self.data = pd.DataFrame(columns=self.columns)
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
        if email in self.data['eMail'].values:
            return 0

        new_data = {'userID': [], 'firstName': [], 'lastName': [], 'eMail': [], 'password': [], 'keepMeSign': [], 'keepMeSignCount': []}
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
                new_data['keepMeSign'].append(False)
            elif column.lower() == 'keepmesigncount':
                new_data['keepMeSignCount'].append(0)
            else:
                print(f"Column {column} not found in the database.")
        
        new_entries_df = pd.DataFrame(new_data)
        self.data = pd.concat([self.data, new_entries_df], ignore_index=True)

        # Veritabanını kaydet
        self.save()
        return 1

    def update_keep_me_signed_in(self, email, keep):
        self.data.loc[self.data['eMail'] == email, 'keepMeSign'] = keep
        if keep:
            self.data.loc[self.data['eMail'] == email, 'keepMeSignCount'] = 0
        self.save()

    def get_keep_me_signed_in_user(self):
        found = self.data[self.data['keepMeSign'] == True]
        if not found.empty:
            return found.iloc[0]
        return None

    def increment_keep_me_sign_count(self, email):
        self.data.loc[self.data['eMail'] == email, 'keepMeSignCount'] += 1
        self.save()

    def reset_keep_me_sign(self, email):
        self.data.loc[self.data['eMail'] == email, 'keepMeSign'] = False
        self.data.loc[self.data['eMail'] == email, 'keepMeSignCount'] = 0
        self.save()

    def save(self):
        self.data.to_excel(self.file_path, index=False)
