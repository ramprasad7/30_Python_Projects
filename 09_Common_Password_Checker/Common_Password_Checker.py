
def check_password(password: str):
    with open("passwords.txt", "r") as file:
        common_passwords: list[str] = file.read().splitlines()

    for i, common_password in enumerate(common_passwords, start=1):
        if password == common_password:
            print(f"{password}: ❌ (#{i})")
            return

    print(f"{password}: ✔️ (Unique)")

def main() -> None:
    user_pass: str = input("Enter Password:")

    if user_pass == '':
        print("Please enter a valid password")
    else:
        check_password(user_pass)


if __name__ == "__main__":
    main()