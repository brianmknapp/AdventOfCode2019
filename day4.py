def password_valid(password):
    password_details = str(password)
    if len(password_details) != 6:
        return False
    last = -1
    has_double = False
    current_double = False
    larger_group = False
    for i in range(len(password_details)):
        if int(password_details[i]) < last:
            return False
        if int(password_details[i]) == last:
            if current_double:
                current_double = False
                larger_group = True
            elif not larger_group:
                current_double = True
        if int(password_details[i]) > last:
            if current_double:
                has_double = True
            current_double = False
            larger_group = False
        last = int(password_details[i])
    if current_double:
        has_double = True
    return has_double


if __name__ == '__main__':
    valid_passwords = 0
    for j in range(206938, 679129):
        if password_valid(j):
            valid_passwords += 1
    print('Possible Solutions: {}'.format(valid_passwords))
