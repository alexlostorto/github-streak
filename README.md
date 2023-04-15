<h1 align="center">Github Streak</h1>

[![Maintainability](https://img.shields.io/codeclimate/maintainability/alexlostorto/github-streak?style=for-the-badge&message=Code+Climate&labelColor=222222&logo=Code+Climate&logoColor=FFFFFF)](https://codeclimate.com/github/alexlostorto/github-streak/maintainability)


The program automatically retrieves the user's streak statistics using **GitHub's API**.

```python
# Example in console
Current streak: 100
Longest streak: 100
Total contributions: 623
```

## ⚡ Quick setup

1. Clone the repo

```bash
git clone https://github.com/alexlostorto/github-streak
```

2. Create a _secrets.json_ file the following contents

```json
{
    "user": "<USERNAME>",
    "token": "<PERSONAL_ACCESS_TOKEN>"
}
```

3. Replace the _username_ with any **GitHub username** and replace the _token_ with your **personal access token**.

4. Run main.py

```bash
python main.py
```

5. Star the repo 😄

## Credits

Everything is coded by Alex lo Storto

Licensed under the MIT License.
