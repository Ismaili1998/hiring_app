import pandas as pd

def get_consultants():
    csv_file_path = "data/consultants.csv"
    df = pd.read_csv(csv_file_path, delimiter='|')
    df = df.fillna("-")
    consultants_list = df.apply(lambda row: ("", "end", row.name, row.name, 
                                (row["full_name"], row["education"], row["years_of_exp"], row["automative_exp"])), axis=1).tolist()
    return df, consultants_list
                            
def get_consultant_skills():
    skills = pd.read_csv('data/skills.txt', delimiter="|")
    skills = skills.apply(lambda row: (row["id"], row["skill_name"]), axis=1).tolist()
    return skills

def get_availability_list():
    availability_list = []
    with open("data/availability_list.txt", "r") as file:
        for line in file:
            data = line.strip()
            availability_list.append(data)
    return availability_list