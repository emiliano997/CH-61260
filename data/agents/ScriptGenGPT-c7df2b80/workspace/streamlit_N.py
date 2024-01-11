"""Import the necessary libraries
"""
import streamlit as st

# Main function to generate the script
def main():
    # Prompt the user to enter a natural number
    number = st.text_input('Enter a natural number')

    try:
        # Convert the input to an integer
        number = int(number)
        
        # Compute the double of the input number
        double = number * 2
        
        # Display the output number
        st.write('The double of', number, 'is', double)
    except ValueError:
        # Handle the case when the input is not a natural number
        st.error('Invalid input. Please enter a natural number.')


# Run the main function
if __name__ == '__main__':
    main()
