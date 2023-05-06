# exercise 7.1

import csv
def create_file(file_name):
    with open(file_name, 'w') as file:
        file.writelines("Lea,Laura,Matilda,Marta,Bruno,Eva,Mona,Marko,Robert,Daniel")


def transform_to_row(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open(output_file, 'w') as out_file:
            for row in csv_reader:
                for name in row:
                    out_file.write(name+'\n')

def add_greeting(input_file, output_file):
    with open(output_file, 'w') as out_file:
        with open(input_file, 'r') as in_file:
            for line in in_file.readlines():
                out_file.write("Hello "+line)

def strip_greeting(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=' ')
        with open(output_file, 'w') as out_file:
            for row in csv_reader:
                out_file.write(row[1] + '\n')

def create_lastnames(lastnames):
    with open("lastnames.txt", 'w') as file:
        file.writelines(lastnames)

def combine_files(file1, file2, output_file):
    with open(file1, 'r') as first_file:
        with open(file2, 'r') as second_file:
            lines1 = first_file.readlines()
            lines2 = second_file.readlines()
            if len(lines1) != len(lines2):
                print(f'Only files with the same amount of lines are supported: {len(lines1)} != {len(lines2)}')
            else:
                with open(output_file, 'w') as out_file:
                    for i in range(0,len(lines1)):
                        out_file.write(lines1[i].rstrip() + " " + lines2[i])


if __name__ == '__main__':
    exercise = input("exercise nr: ")
    if exercise == '1':
        create_file("names.txt")
    elif exercise == '2':
        transform_to_row("names.txt", "name_list.txt")
    elif exercise == '3':
        add_greeting("name_list.txt", "greeting_list.txt")
    elif exercise == '4':
        strip_greeting("greeting_list.txt", "stripped_list.txt")
    elif exercise == '5':
        create_lastnames("Devide")
        combine_files("greeting_list.txt","lastnames.txt","combined1.txt")
        create_lastnames("Devide\nMayer\nMaier\nMayr\nMaier\nMeier\nHuber\nMueller\nFischer\nBauer")
        combine_files("greeting_list.txt","lastnames.txt","combined2.txt")
    else:
        print(f"unknown exercise {exercise}")