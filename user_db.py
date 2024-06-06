import pandas as pd
from datetime import datetime
import os

class User:
    def __init__(self, file_path):
        self.file_path = file_path
        self.columns = ['user_id', 'first_name', 'last_name', 'time', 'account_name', 'account_type', 'card_number', 'transaction_type', 'transaction_description', 'transaction_date']
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
    
    def save_user_id(self, user_id):
        self.user_id = user_id
        new_data = {'user_id': [user_id]}
        new_entries_df = pd.DataFrame(new_data)
        self.data = pd.concat([self.data, new_entries_df], ignore_index=True)

    def save(self):
        self.data.to_excel(self.file_path, index=False)