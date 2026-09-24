import sqlite3
from pydantic import BaseModel
class SQLResult(BaseModel):
    sql_query: str
    explanation: str
conn = sqlite3.connect("final.db")
cursor = conn.cursor()
SCHEMA = "Table students(id INTEGER, name  TEXT, marks INTEGER, city TEXT)"
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT, marks INTEGER, city TEXT)")
cursor.execute("DELETE FROM students")
cursor.executemany("INSERT INTO students VALUES (?,?,?,?)", 
                   [(1, 'Shanza', 92, 'Islambad'),
                    (2, 'Nisha', 85, 'Rawalpindi'),          
                    (3, 'Samavia', 75, 'Lahore'),
                    (4, 'Shanaya', 62, 'Karachi'),
                    (5, 'Ayat', 50, 'Rawalpindi')])
conn.commit()
print("=== PROJECT 1 READY - 5 AI Engineer Projects ===")
print(f"Schema: {SCHEMA}")
print("Database: final.db (PostgreSQL ka free version SQLite)")
print("Stack: Python + SQL + Pydantic + Prompt Engineering + Gemini/OpenAI Logic")
print("Cost: ZERO")
def ai_engine(question):
    prompt = f""""
    Schema: {SCHEMA}
    User Question: {question}
    Task: convert to SQL. only SELECT query
""" 
    print(f"\n[Prompt Engineering] AI ko bheja: {prompt}")
    q = question.lower()
    if "islambad" in q:
        return SQLResult(sql_query="SELECT * FROM students WHERE city 'Islambad'", explanation="Islambad ke students filter kiye")
    elif "Lahore" in q:
        return SQLResult(sql_query="SELECT * FROM students WHERE city = 'Lahore'", explanation="Lahore ka students")
    elif "85" in q or "zyda" in q or "greater" in q or "90" in q:
        return SQLResult(sql_query="SELECT * FROM students WHERE marks > 85", explanation="85 se zayada marks wale")
    elif "average" in q:
        return SQLResult(sql_query="SELECT AVG(marks) FROM students", explanation="Average marks nikla")
    elif "count" in q :
        return SQLResult(sql_query="SELECT COUNT (*) FROM students", explanation="Total student count kary")
    elif "all" in q:
        return SQLResult(sql_query="SELECT * FROM students", explanation="Sara students dikhaye")
    else:
        return SQLResult(sql_query="SELECT * FROM students", explanation="Default - sab dikhaye")
while True:
    user_q = input("\nAap pucho (e.g, 'Rawalpindi wale dikhao' / '85 se zyada' / q to exit): ")
    if user_q.lower() == 'q':
        break
    result = ai_engine(user_q)
    print(f"\n[Gemini/OpenAI Output] SQL:{result.sql_query}")
    print(f"[Structured Output - Pydantic] Explanation: {result.explanation}")
    cursor.execute(result.sql_query)
    rows = cursor.fetchall()
    print("--- SQL Result ---")
    for r in rows:
        print(r)
    conn.close()
    print("\nProject khtam!")
