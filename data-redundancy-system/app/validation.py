def is_valid_email(email: str) -> bool:
    if " " in email:
        return False
    if email.count("@") != 1:
        return False
    local,domain = email.split("@")
    if local == " " or "." not in domain:
        return False
