from app import app, db, Question

cse_questions = [
    {"question": "What is the time complexity of binary search?", "option_a": "O(n)", "option_b": "O(log n)", "option_c": "O(n log n)", "option_d": "O(1)", "correct_option": "B"},
    {"question": "Which data structure uses FIFO?", "option_a": "Stack", "option_b": "Queue", "option_c": "Tree", "option_d": "Graph", "correct_option": "B"},
    {"question": "Which data structure uses LIFO?", "option_a": "Queue", "option_b": "Stack", "option_c": "Tree", "option_d": "Graph", "correct_option": "B"},
    {"question": "Which of the following is not an OOP concept?", "option_a": "Encapsulation", "option_b": "Polymorphism", "option_c": "Compilation", "option_d": "Inheritance", "correct_option": "C"},
    {"question": "Which protocol is used to send emails?", "option_a": "HTTP", "option_b": "FTP", "option_c": "SMTP", "option_d": "TCP", "correct_option": "C"},
    {"question": "Which SQL command is used to remove a table?", "option_a": "DELETE", "option_b": "REMOVE", "option_c": "DROP", "option_d": "CLEAR", "correct_option": "C"},
    {"question": "Which layer of OSI model handles routing?", "option_a": "Transport", "option_b": "Network", "option_c": "Session", "option_d": "Data Link", "correct_option": "B"},
    {"question": "What does RAM stand for?", "option_a": "Random Access Memory", "option_b": "Read Access Memory", "option_c": "Run Access Memory", "option_d": "Real Access Memory", "correct_option": "A"},
    {"question": "Which symbol is used for comments in Python?", "option_a": "//", "option_b": "<!--", "option_c": "#", "option_d": "/* */", "correct_option": "C"},
    {"question": "Which command creates a database in MySQL?", "option_a": "MAKE DATABASE", "option_b": "CREATE DATABASE", "option_c": "NEW DATABASE", "option_d": "ADD DATABASE", "correct_option": "B"},
    {"question": "TCP is:", "option_a": "Connectionless", "option_b": "Connection-oriented", "option_c": "Stateless", "option_d": "None", "correct_option": "B"},
    {"question": "Which is a NoSQL database?", "option_a": "MySQL", "option_b": "Oracle", "option_c": "MongoDB", "option_d": "SQL Server", "correct_option": "C"},
    {"question": "HTML stands for:", "option_a": "Hyper Text Markup Language", "option_b": "Hyperlinks Text Mark Language", "option_c": "Hyper Tool Multi Language", "option_d": "None of these", "correct_option": "A"},
    {"question": "Python is:", "option_a": "Compiled", "option_b": "Interpreted", "option_c": "Assembly", "option_d": "Machine language", "correct_option": "B"},
    {"question": "Stack operations are:", "option_a": "Push & Pop", "option_b": "Enqueue & Dequeue", "option_c": "Insert & Delete", "option_d": "None of these", "correct_option": "A"},
    {"question": "Queue operations are:", "option_a": "Push & Pop", "option_b": "Enqueue & Dequeue", "option_c": "Insert & Delete", "option_d": "None of these", "correct_option": "B"},
    {"question": "Tree root has no parent", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Graph uses vertices & edges", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Hashing improves search", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "OS manages hardware", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Deadlock occurs when resources wait circularly", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Paging avoids fragmentation", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Kernel is core of OS", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Process is program in execution", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Normalization reduces redundancy", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Foreign key links tables", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "SELECT retrieves data", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "WHERE filters data", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "JOIN combines tables", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "FTP transfers files", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "DNS converts domain to IP", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "IP address identifies device", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Firewall improves security", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Router connects networks", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Compiler converts source to machine code", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Interpreter executes line by line", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Git is version control", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "API stands for Application Programming Interface", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "JSON is data format", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "AI means Artificial Intelligence", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Cloud computing stores data online", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Encryption secures data", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Agile is development methodology", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "Machine learning is subset of AI", "option_a": "True", "option_b": "False", "option_c": "-", "option_d": "-", "correct_option": "A"},
    {"question": "BFS is used for:", "option_a": "Depth traversal", "option_b": "Level traversal", "option_c": "Both", "option_d": "None", "correct_option": "B"},
    {"question": "DFS is used for:", "option_a": "Depth traversal", "option_b": "Level traversal", "option_c": "Both", "option_d": "None", "correct_option": "A"},
    {"question": "Which is mutable in Python?", "option_a": "List", "option_b": "Tuple", "option_c": "String", "option_d": "None", "correct_option": "A"},
    {"question": "Which is immutable in Python?", "option_a": "List", "option_b": "Tuple", "option_c": "Set", "option_d": "Dictionary", "correct_option": "B"},
    {"question": "Which is used to handle exceptions in Python?", "option_a": "try-except", "option_b": "if-else", "option_c": "switch", "option_d": "for", "correct_option": "A"},
    {"question": "Which method is used to start a thread in Python?", "option_a": "run()", "option_b": "start()", "option_c": "execute()", "option_d": "init()", "correct_option": "B"}
]

with app.app_context():
    for q in cse_questions:
        existing = Question.query.filter_by(question=q["question"]).first()
        if not existing:  # Prevent duplicates
            question = Question(
                department="CSE",
                question=q["question"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                correct_option=q["correct_option"]
            )
            db.session.add(question)
    db.session.commit()
    print("✅ All 50 CSE Questions Added Successfully!")
