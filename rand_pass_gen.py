import streamlit as st
import random
import string

def generate_password(use_lower, use_upper, use_numbers, use_symbols, length):
    """
    Generates a random password based on user-specified criteria.

    Args:
        use_lower (bool): Include lowercase letters?
        use_upper (bool): Include uppercase letters?
        use_numbers (bool): Include numbers?
        use_symbols (bool): Include symbols?
        length (int): The desired password length.

    Returns:
        str: The generated password.  Returns an empty string if no character
             sets are selected or length is invalid.
    """
    # Input validation:  Check for positive length
    if length <= 0:
        st.error("Password length must be a positive integer.")
        return ""

    # Define character sets based on user preferences.
    characters = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Handle the case where no characters were selected.
    if not characters:
        st.error("Error: No character sets selected. Cannot generate password.")
        return ""

    # Generate the password.
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    """
    Main function to run the password generator app using Streamlit.
    """
    st.title("Random Password Generator")

    # User inputs using Streamlit widgets
    use_lower = st.checkbox("Include lowercase letters")
    use_upper = st.checkbox("Include uppercase letters")
    use_numbers = st.checkbox("Include numbers")
    use_symbols = st.checkbox("Include symbols")
    length = st.number_input("Enter the desired password length", min_value=1, step=1, value=8) #Added default value

    # Generate and display the password
    if st.button("Generate Password"):
        generated_password = generate_password(use_lower, use_upper, use_numbers, use_symbols, int(length)) #changed length to int
        if generated_password:
            st.subheader("Generated Password:")
            st.success(generated_password)

if __name__ == "__main__":
    main()
