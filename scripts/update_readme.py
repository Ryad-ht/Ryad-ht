import os
from datetime import datetime

def update_readme():
    readme_path = "README.md"
    
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    base_content = """👋 Hello, I am @Ryad-ht, a data analyst & vibe coding
I am currently working on case studies by myself and I am open to freelance or employment opportunities.
Here are all the tools I have used before: Programming languages: Python, R, SQL, VBA, Java, C, C++, JavaScript, Swift, PHP. Software: Tableau, Orange, Power BI, Excel, PyCharm, Jupyter Notebook, IntelliJ, RStudio, Eclipse.
You can contact me via email at hadjtahar.ryad@gmail.com."""

    if content.strip() == base_content.strip():
        new_content = base_content + "\n\u200B"
        action = "added"
    else:
        new_content = base_content
        action = "removed"
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    
    print(f"README updated: character {action} at {datetime.now()}")
    return action

if __name__ == "__main__":
    update_readme()

Clique sur **"Commit new file"**


1. Va dans **Settings** (paramètres de ton repo)
2. Dans le menu de gauche, clique sur **Actions** → **General**
3. Dans "Actions permissions", sélectionne **"Allow all actions and reusable workflows"**
4. Dans "Workflow permissions", sélectionne **"Read and write permissions"**
5. Clique sur **Save**


1. Va dans l'onglet **Actions** de ton repo
2. Clique sur **"Update README"** dans la liste des workflows
3. Clique sur **"Run workflow"** → **"Run workflow"**
4. Attends 30 secondes, le workflow va s'exécuter
