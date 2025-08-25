import sys
from git import Repo
from git_suggestion import suggest_git_commands # type: ignore

def main():

    try:
        repo = Repo(".")
        if repo.bare:
            print("Not a Git repository.")
            sys.exit(1)
    except Exception as e:
        print(f"Error accessing Git repository: {e}")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Use command: python main.py [suggest]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "suggest":
        suggestions = suggest_git_commands(repo)
        print("\nSuggested Git Commands:")
        for suggestion in suggestions:
            print(f"- {suggestion['command']}: {suggestion['reason']}")

    else:
        print("Incorrect command. Use 'suggest'.")
        sys.exit(1)

if __name__ == "__main__":
    main()