import pyotp


def generate_secret_key():
    secret_key = pyotp.random_base32()
    return secret_key


def generate_otp(secret_key):
    totp = pyotp.TOTP(secret_key)

    otp = totp.now()
    return otp


def verify_otp(secret_key, entered_otp):
    totp = pyotp.TOTP(secret_key)

    return totp.verify(entered_otp)


secret_key = generate_secret_key()
otp = generate_otp(secret_key)
# Display the generated OTP
print("Generated OTP:", otp)
print()

entered_otp = input("Enter the OTP: ")

if verify_otp(secret_key, entered_otp):
    print("OTP verification successful!")

else:
    print("Wrong code")
