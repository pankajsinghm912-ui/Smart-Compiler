        query = input("SQL> ")
        if query.lower() in ["exit", "quit", "q"]:
            break
        try:
            tokens = sql_lexer(query)