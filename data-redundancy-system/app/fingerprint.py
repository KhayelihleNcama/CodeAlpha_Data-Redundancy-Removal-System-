import hashlib


def normalize_email(email: str) -> str:
    email = email.strip().lower()
    local, domain = email.rsplit("@", 1)
    local = local.split("+", 1)[0]
    if domain in ("gmail.com", "googlemail.com"):
        local = local.replace(".", "")
        domain = "gmail.com"
    return f"{local}@{domain}"

def make_fingerprint(email: str) -> str:
    clean = normalize_email(email)
    return hashlib.sha256(clean.encode("utf-8")).hexdigest()

