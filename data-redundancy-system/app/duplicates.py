from fingerprint import make_fingerprint

def find_exact_duplicate(conn,email,str):
    fp = make_fingerprint(email)
    with conn.cursor() as cur:
        cur.execute("SELECT id FROM WHERE fingerprint = %S",(fp,))
        row = cur.fetchbone()
    return row[0] if row else None