import pandas as pd

def get_department(df):
    pass
    
def get_second_record(df):
    pass
    
def get_info_grace(df):
    pass

def get_experience_location(df):
    pass
    
def get_department_elena_aiden(df):   
    pass

def get_experience_salary_first_three(df):
    pass

def main():
    df = pd.read_csv("data.csv", index_col= 0)

    print("Department Column:\n", get_department(df))
    print("\nSecond Record:\n", get_second_record(df))
    print("\nGrace's Info:\n", get_info_grace(df))
    print("\nExperience and Location Columns:\n", get_experience_location(df))
    print("\nDepartment of Elena and Aiden:\n", get_department_elena_aiden(df))
    print("\nExperience and Monthly Salary of First Three:\n", get_experience_salary_first_three(df))


if __name__ == "__main__":
        main()
