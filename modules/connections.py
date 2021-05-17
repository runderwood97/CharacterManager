import pyodbc

connection = pyodbc.connect("""
     DRIVER={ODBC Driver 17 for SQL Server};
     SERVER=LAPTOP-SDQV5OSG;
     DATABASE=CharacterManagement;
     Trusted_Connection=Yes;
""")