<h1 align="center">Github Streak</h1>

[![Maintainability](https://img.shields.io/codeclimate/maintainability/alexlostorto/github-streak?style=for-the-badge&message=Code+Climate&labelColor=222222&logo=Code+Climate&logoColor=FFFFFF)](https://codeclimate.com/github/alexlostorto/github-streak/maintainability)

The program automatically retrieves the user's streak statistics using **GitHub's GraphQL API**.

```python
# Examples in console
+---------------------+----------+      ╭─────────────────────┬──────────╮
|       Category      |  Count   |      │       Category      │   Count  │
+---------------------+----------+      ├─────────────────────┼──────────┤
|    Current Streak   | 102 days |      │    Current Streak   │ 104 days │
|    Longest Streak   | 102 days |      │    Longest Streak   │ 104 days │
| Total Contributions |   642    |      │ Total Contributions │    658   │
+---------------------+----------+      ╰─────────────────────┴──────────╯
```

## ⚡ Quick setup

1. Clone the repo

```bash
git clone https://github.com/alexlostorto/github-streak
```

2. Rename _.env.example_ to _.env_

3. Replace the _username_ with any **GitHub username** and replace _ghp_example_ with your **personal access token**.

```env
TOKEN=ghp_example
USER=username
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Run main.py

```bash
python main.py
```

6. Star the repo 😄

## Credits

Everything is coded by Alex lo Storto

Licensed under the MIT License.
