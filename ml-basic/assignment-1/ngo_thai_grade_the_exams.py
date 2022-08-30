def is_file_name_with_txt_extension(file_name):
    """ Check if file name has .txt extension
    
    Args:
        file_name (str): file name to check
        
    Returns:
        bool: True if file name has .txt extension, False otherwise
    """

    if file_name.endswith('.txt'):
        return True
    else:
        return False


def add_txt_extension(file_name):
    """ Add .txt extension to file name if it does not have .txt extension

    Args:
        file_name (str): file name

    Returns:
        str: file name with .txt extension
    """

    if is_file_name_with_txt_extension(file_name):
        return file_name
    else:
        return file_name + '.txt'


def open_file(file_name):
    """ Open file with file name

    Args:
        file_name (str): file name

    Returns:
        file: opened file
    """

    file_name = add_txt_extension(file_name)
    try:
        file = open(file_name, 'r')
        print('\n Successfully opened ' + file_name + '\n')
        return file
    except FileNotFoundError:
        print('\n File cannot be found. \n')
        return None


def is_digit(string):
    """ Check if string is digit
    
    Args:
        string (str): string to check
        
    Returns:
        bool: True if string is digit, False otherwise
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_line_valid(line):
    """ Check if line is valid

    Args:
        line (str): line to check

    Returns:
        bool: True if line is valid, False otherwise
    """
    data = line.split(',')
    if len(data) != 26:
        print('Invalid line of data: does not contain exactly 26 values:')
        print(line + '\n')
        return False
    student_id = data[0]
    if len(student_id) != 9 or student_id[0] != 'N' or (not is_digit(student_id[1:])):
        print('Invalid line of data: N# is invalid')
        print(line + '\n')
        return False
    return True


def grade_the_exams(student_info):
    """ Grade the exams of student

    Args:
        student_info (str): list of student info

    Returns:
        str: student id
        int: point of student
    """

    correct_answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    correct_answer_array = correct_answer_key.split(',')
    data = student_info.split(',')
    student_answer = data[1:]
    point = 0
    for index, answer in enumerate(student_answer):
        if len(answer.strip()) == 0:
            continue
        if answer.strip() == correct_answer_array[index]:
            point += 4
        else:
            point -= 1
    return data[0], point


def get_min_max(list_point):
    """ Get min and max point from list of points

    Args:
        list_point (list): list of points

    Returns:
        int: min point
        int: max point
    """
    min_point = min(list_point)
    max_point = max(list_point)
    return min_point, max_point


def get_average(list_point):
    """ Get average point from list of points

    Args:
        list_point (list): list of points

    Returns:
        float: average point
    """
    sum_point = sum(list_point)
    return round(sum_point / len(list_point), 2)


def get_median(list_point):
    """ Get median point from list of points

    Args:
        list_point (list): list of points

    Returns:
        float: median point
    """
    list_point.sort()
    if len(list_point) % 2 == 0:
        median = (list_point[len(list_point) // 2] + list_point[len(list_point) // 2 - 1]) / 2
    else:
        median = list_point[len(list_point) // 2]
    return median


def print_student_point_to_file(student_point, file_name):
    """ Print dict point to file

    Args:
        student_point (dict): dict of points
        file_name (str): file name
    """
    file = open(file_name, 'w')
    for key, value in student_point.items():
        file.write(key + ',' + str(value) + '\n')
    file.close()


def main():
    """ Main function"""
    filename = input('Enter a class file to grade (i.e. class1 for class1.txt): ')
    file = open_file(filename)

    if file is not None:
        invalid_line = 0
        valid_line = 0
        student_point = {}
        print('**** ANALYZING **** \n')
        lines = file.readlines()
        for line in lines:
            if is_line_valid(line):
                valid_line += 1
                point_data = grade_the_exams(line)
                student_point[point_data[0]] = point_data[1]
            else:
                invalid_line += 1

        if invalid_line == 0:
            print('No errors found! \n')
        print('**** REPORT **** \n')
        print('Total valid lines of data: ' + str(valid_line))
        print('Total invalid lines of data: ' + str(invalid_line) + '\n')
        list_point = list(student_point.values())
        print('Mean (average) score: ' + str(get_average(list_point)))
        min_point, max_point = get_min_max(list_point)
        print('Highest score: ' + str(max_point))
        print('Lowest score: ' + str(min_point))
        print('Range of scores: ' + str(max_point - min_point))
        print('Median score: ' + str(get_median(list_point)))

        new_file_name = filename.split('.')[0]
        print_student_point_to_file(student_point, new_file_name + '_grades.txt')
        file.close()


main()
