import streamlit as st
import pickle
from PIL import Image

# Load the pre-trained model and vectorizer
model = pickle.load(open('spam123', 'rb'))  # Corrected to 'rb' (read binary)
cv = pickle.load(open('vec123', 'rb'))  # Corrected to 'rb' (read binary)

def main():
    # Page configuration
    st.set_page_config(page_title="Spam Classifier App", page_icon="📧")

    # App Title and Developer Credit
    st.title("📧 Email Spam Classifier")
    st.write("A simple app to classify emails as **spam** or **not spam**.")
    st.markdown("**Developed by Amlan Pandey**")

    # Banner (optional)
    banner = Image.open("banner_image.jpg")  # Replace with your banner image path
    st.image(banner, use_container_width=True)

    # Input area for email message
    user_input = st.text_area(
        "Enter email content to classify:",
        height=200,
        placeholder="Type or paste the email content here...",
    )

    # Classify button
    if st.button("Classify"):
        if user_input:
            # Preprocess and predict
            data = [user_input]
            vec = cv.transform(data).toarray()  # Transform input using the vectorizer
            result = model.predict(vec)  # Predict with the model

            # Display result
            if result[0] == 0:
                st.success("✅ This is **NOT** a spam email!")
            else:
                st.error("❌ This is a **spam** email!")
        else:
            st.warning("⚠️ Please enter an email to classify.")

# Run the app
if __name__ == "__main__":
    main()
