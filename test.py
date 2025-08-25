from git import Repo

repo = Repo(".")
u = repo.untracked_files
print(u)
print(len(u))