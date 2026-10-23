import sys
import os

# ✅ Correct path to 'core' folder
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

# ✅ Proper imports
from core.math_evaluator import evaluate as eval_math
from core.markdowna_parser import convert_markdown_to_html
from core.sql_executor import query_executor

def math_mode():
    print("\n🧠 MATH EXPRESSION MODE (type 'exit' to return)")
    while True:
        expr = input("MATH> ")
        if expr.lower() in ["exit", "quit", "q"]:
            break
        try:
            result = eval_math(expr)
            print(f"✅ Result: {result}")
        except Exception as e:
            print("❌ Error:", e)

def markdown_mode():
    print("\n📝 MARKDOWN MODE")
    print("Type your Markdown content. Press Enter on an empty line to finish:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    md_text = "\n".join(lines)
    try:
        html = convert_markdown_to_html(md_text)
        print("\n✅ Converted HTML:\n")
        print(html)
    except Exception as e:
        print("❌ Markdown Error:", e)

def sql_mode():
    print("\n🔍 SQL QUERY MODE (type 'exit' to return)")
    while True:
        query = input("SQL> ")
        if query.lower() in ["exit", "quit", "q"]:
            break
        try:
            result = query_executor(query)
            print("✅ Query Result:\n")
            if isinstance(result, list):
                for row in result:
                    print(row)
            else:
                print(result)
        except Exception as e:
            print("❌ SQL Error:", e)

def main():
    print("\n🛠 Welcome to the Mini Compiler CLI 🛠")
    while True:
        print("\n🎯 Choose an Option:")
        print("1. Math Expression Evaluation")
        print("2. Markdown to HTML Conversion")
        print("3. SQL Query Execution on CSV")
        print("4. Exit")

        choice = input("👉 Enter choice (1-4): ")

        if choice == '1':
            math_mode()
        elif choice == '2':
            markdown_mode()
        elif choice == '3':
            sql_mode()
        elif choice == '4':
            print("👋 Exiting... Shukriya!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

# ✅ Correct main entry point
if __name__ == "__main__":
    main()
