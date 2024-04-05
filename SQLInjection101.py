# Disclaimer: This script is for educational purposes only. Do not attempt to perform SQL injection attacks on any real systems without proper authorization.

# Author: Tamer Hellah
# Date: 03/4/2024
# Version: 1.0


import time
import random


def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def colorize(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'magenta': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'underline': '\033[4m',
        'end': '\033[0m'
    }
    return colors[color] + text + colors['end']


def ask_question(question, options, correct_answer):
    random_indices = list(range(len(options)))
    random.shuffle(random_indices)
    slow_print(question)
    for i, index in enumerate(random_indices, start=1):
        slow_print(f"{i}. {options[index]}")
    attempt = 1
    while attempt <= 2:
        try:
            answer = int(input("Your answer: "))
            if 1 <= answer <= len(options):
                if options[random_indices[answer - 1]] == correct_answer:
                    slow_print("Correct!\n")
                    return True
                else:
                    slow_print("Incorrect. Try again.")
                    attempt += 1
            else:
                slow_print("Invalid choice. Please enter a number between 1 and " + str(len(options)) + ".")
        except ValueError:
            slow_print("Invalid choice. Please enter a number.")
    slow_print("Incorrect. The correct answer is: " + correct_answer + "\n")
    return False


slow_print("Disclaimer: This tutorial is for educational purposes only. Do not attempt to perform SQL injection attacks on any real systems without proper authorization.\n")


slow_print("This is Tamer Hellah \!/Welcome to the SQL Injection Tutorial\!/")
slow_print("Today, we'll learn about SQL injection attacks and how they can be prevented.")
slow_print("Let's dive in!\n")


slow_print(colorize("Section 1: What is SQL Injection?", 'bold'))
slow_print("SQL injection (SQLi) is a technique where attackers inject malicious SQL code into application inputs to manipulate the SQL queries executed by the application.")
slow_print("This can lead to unauthorized access, modification, or deletion of data in the database.\n")


slow_print(colorize("Section 2: Basic Example of SQL Injection", 'bold'))
slow_print("Consider a simple authentication query:")
slow_print("SELECT * FROM users WHERE username = '[username]' AND password = '[password]';")
slow_print("An attacker could bypass authentication by entering a username like " + colorize("' OR '1'='1", 'green') + ". This would alter the query to always return true, granting access.\n")
slow_print("In the frontend, the input field might look like this:")
slow_print(colorize("<input type='text' name='username' value='' OR '1'='1' />", 'cyan'))
slow_print("\n")


slow_print(colorize("Section 3: Different Types of SQL Injection Attacks", 'bold'))
slow_print("1. In-band SQLi:")
slow_print("- Tautologies")
slow_print("- Union Queries")
slow_print("- Error-Based\n")
slow_print("2. Inferential (Blind SQLi):")
slow_print("- Boolean-Based")
slow_print("- Time-Based\n")
slow_print("3. Out-of-band SQLi\n")


slow_print(colorize("Section 4: Prevention Strategies for SQL Injection", 'bold'))
slow_print("Frontend Prevention:")
slow_print("- Data Binding")
slow_print("- HttpClient\n")
slow_print("Backend Prevention:")
slow_print("- Input Validation")
slow_print("- Spring Data JPA Repositories")
slow_print("- Hibernate HQL\n")


slow_print(colorize("Section 5: Queries to Retrieve Data from the Database", 'bold'))
queries = [
    ("Retrieve Database Version", "SELECT @@VERSION;", "Retrieve the version of the database server"),
    ("Retrieve List of Tables", "SELECT table_name FROM information_schema.tables WHERE table_schema = database();", "List tables in current database"),
    ("Retrieve List of Columns from a Specific Table", "SELECT column_name FROM information_schema.columns WHERE table_name = 'your_table_name';", "Retrieve columns from a specific table"),
    ("Retrieve Data from a Specific Table", "SELECT * FROM your_table_name;", "Retrieve all data from a specific table"),
    ("Retrieve Specific Columns from a Specific Table", "SELECT column1, column2 FROM your_table_name;", "This query selects data from two columns"),
    ("Retrieve Data Based on a Condition", "SELECT * FROM your_table_name WHERE condition;", "Retrieve data based on a condition"),
    ("Retrieve Distinct Values from a Column", "SELECT DISTINCT column_name FROM your_table_name;", "Retrieve distinct values from a column"),
    ("Retrieve Data with Sorting", "SELECT * FROM your_table_name ORDER BY column_name;", "Retrieve data with sorting"),
    ("Retrieve Data with Pagination", "SELECT * FROM your_table_name LIMIT offset, limit;", "Retrieve data with pagination"),
    ("Retrieve Data with Aggregate Functions (e.g., COUNT, SUM, AVG)", "SELECT COUNT(*) FROM your_table_name;", "Retrieve aggregated data from a table"),
    ("Retrieve Data from Multiple Tables (Join)", "SELECT t1.column1, t2.column2 FROM table1 t1 JOIN table2 t2 ON t1.id = t2.id;", "Retrieve data from multiple tables with a join"),
    ("Retrieve Data Grouped by a Column", "SELECT column_name, COUNT(*) FROM your_table_name GROUP BY column_name;", "Retrieve grouped data"),
    ("Retrieve Data with Filtering using HAVING Clause", "SELECT column_name, COUNT(*) FROM your_table_name GROUP BY column_name HAVING COUNT(*) > 1;", "Retrieve filtered data with HAVING clause"),
    ("Retrieve Data Ordered Randomly", "SELECT * FROM your_table_name ORDER BY RAND();", "Retrieve data ordered randomly"),
    ("Retrieve Data with String Manipulations", "SELECT CONCAT(column1, column2) AS concatenated_string FROM your_table_name;", "Retrieve data with string manipulations"),
    ("Retrieve Data with Date and Time Functions", "SELECT DATE_FORMAT(date_column, '%Y-%m-%d') AS formatted_date FROM your_table_name;", "Retrieve data with date and time functions"),
    ("Retrieve Data with CASE Statements", "SELECT column_name, CASE WHEN condition THEN value1 ELSE value2 END AS custom_column FROM your_table_name;", "Retrieve data with CASE statements"),
    ("Retrieve Data Using Full-Text Search", "SELECT * FROM your_table_name WHERE MATCH(column_name) AGAINST ('search_term');", "Retrieve data using full-text search")
]

score = 0


for i, (query_title, query, answer) in enumerate(queries, start=1):
    slow_print(f"Question {i + 4}:")
    if ask_question(f"What does the following SQL query do?\n{query}", [answer, "Deletes data from the database", "Updates data in the database", "Inserts data into the database", "None of the above"], answer):
        score += 1

# Conclusion
slow_print(colorize("Section 6: Conclusion", 'bold'))
slow_print("SQL injection poses a significant threat to web application security.")
slow_print("By understanding and implementing prevention strategies, we can mitigate the risk and safeguard user data.")
slow_print("Stay vigilant and prioritize security to protect against SQL injection attacks!\n")


slow_print(f"Your score: {score}/{len(queries)}")


slow_print("For more information on cybersecurity, visit " + colorize("cybersecveillance.com", 'cyan'))


slow_print("Thank you for learning with us!")
