from agent_tools import list_files, read_file, grep_logs, get_time

def simple_agent(question: str):
    q = question.lower()
    if "error" in q:
        result = grep_logs("error")
        return f"I searched logs for errors:\n{result}"
    elif "list" in q:
        result = list_files(".")
        return f"Files in project:\n{result}"
    elif "log" in q or "epoch" in q:
        result = read_file("logs/train.log")
        return f"Recent logs:\n{result}"
    elif "time" in q:
        return f"Current time: {get_time()}"
    elif "read" in q:
        for word in question.split():
            if ".txt" in word or ".log" in word:
                return f"Content of {word}:\n{read_file(word)}"
        return "Say like: read hello.txt"
    else:
        return f"I'm Log Detective. Try:\n- list files\n- read hello.txt\n- show errors\n- show logs\nYou asked: {question}"
