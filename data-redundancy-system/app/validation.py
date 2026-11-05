def is_valid_email(email: str) -> bool:
    if not isinstance(email, str):
        return False

    email = email.strip()
    if not email or " " in email:
        return False
    if email.count("@") != 1:
        return False

    local, domain = email.split("@", 1)
    if not local or not domain:
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    if "." not in domain:
        return False

    domain_parts = domain.split(".")
    if any(part == "" for part in domain_parts):
        return False
    if len(domain_parts[-1]) < 2:
        return False

    return True


PLACEHOLDER_NAMES = {"test", "none", "null", "unknown", "unkown", "audf", "xxx", "n/a", "na"}


def is_valid_name(name: str) -> bool:
    if not isinstance(name, str):
        return False

    name = name.strip()
    if len(name) < 2:
        return False

    lower_name = name.lower()
    if lower_name in PLACEHOLDER_NAMES:
        return False
    if lower_name.isdigit():
        return False
    if not any(char.isalpha() for char in name):
        return False

    return True


def is_valid_phone(phone: str) -> bool:
    if not isinstance(phone, str):
        return False

    digits = "".join(char for char in phone if char.isdigit())
    if not 7 <= len(digits) <= 15:
        return False
    if len(set(digits)) == 1:
        return False

    return True


def validate(record: dict) -> list:
    problems = []
    if not isinstance(record, dict):
        return ["invalid record"]

    if not is_valid_name(record.get("name", "")):
        problems.append("invalid name")
    if not is_valid_email(record.get("email", "")):
        problems.append("invalid email")
    if not is_valid_phone(record.get("phone", "")):
        problems.append("invalid phone")
    return problems
