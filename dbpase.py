@app.post("/customers")
def create_customer(name: str = Form(...), email: str = Form(...)):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO customers (name, email) VALUES (?, ?)",
        (name, email)
    )
    conn.commit()
    conn.close()

    return {"status": "customer added", "name": name, "email": email}