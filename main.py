import re
import getpass

def check_length(password):
    return len(password) >= 8

def check_upper_lower(password):
    return any(c.isupper() for c in password) and any(c.islower() for c in password)

def check_digit(password):
    return any(c.isdigit() for c in password)

def check_special(password):
    return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

def calculate_score(password):
    score = 0
    if check_length(password):
        score += 25
    if check_upper_lower(password):
        score += 25
    if check_digit(password):
        score += 25
    if check_special(password):
        score += 25
    return score

def strength_label(score):
    if score < 50:
        return "Weak"
    elif score < 75:
        return "Medium"
    else:
        return "Strong"

def analyze_password(password):
    score = calculate_score(password)

    print("\nPassword Analysis")
    print("-----------------")
    print(f"Score: {score}/100")
    print(f"Strength: {strength_label(score)}")

    if not check_length(password):
        print("- Password should be at least 8 characters long")
    if not check_upper_lower(password):
        print("- Use both uppercase and lowercase letters")
    if not check_digit(password):
        print("- Add at least one digit")
    if not check_special(password):
        print("- Include a special character")

def main():
    print("Secure Password Strength Analyzer")
    password = getpass.getpass("Enter password: ")
    analyze_password(password)

if __name__ == "__main__":
    main()
