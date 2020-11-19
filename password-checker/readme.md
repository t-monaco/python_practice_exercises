# Password Checker

This is a password checker, basically it's shows if your password(s) have been used. This script consumes **[Have I been PWNED](https://haveibeenpwned.com/API/v3)** API.

### Execution

Basically, you introduce the password(s) you want to check into the file ***"paswords.txt"*** one in each line.

```bash
    password_1
    password_2
    password_3LoremLoremLorem
    ...
```

Then, you should run the script from the command line: 

```bash
    python check_my_pass.py
```

Finally, you will have an output like this:

```bash
    password_1 was found 2202 times... you should probably change your password!
    password_2 was found 380 times... you should probably change your password!
    password_3LoremLoremLorem was NOT found. Carry on!
    ... was found 4620 times... you should probably change your password!
    Done!
```
