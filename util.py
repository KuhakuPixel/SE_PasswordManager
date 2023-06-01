import re

# regex to check email
# dont ask me what it means cause I dont know
# https://stackoverflow.com/a/201378/14073678
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
email_regex = r"email :(.+) password"
password_regex = r"password :(.+)"
#belum di encrypt ya 

def is_email_valid(email: str) -> bool:
    return re.match(EMAIL_REGEX, email)

def is_login_info_valid(email, password, data_class):

    for item in data_class.data:
        match_email = re.search(email_regex, item)
        match_password = re.search(password_regex, item)

        if match_email and match_password:
            stored_email = match_email.group(1)
            stored_password = match_password.group(1)

            if email == stored_email and password == stored_password:
                return True

    return False