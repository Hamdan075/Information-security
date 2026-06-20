import streamlit as st
from crypto_utils import encrypt_file, decrypt_file
import base64

st.title("🔐 Hybrid RSA + AES Encryption App")

menu = st.sidebar.selectbox("Choose Action", ["Encrypt File", "Decrypt File"])

# ---------------------------------------------------------
# ENCRYPT FILE
# ---------------------------------------------------------
if menu == "Encrypt File":
    uploaded = st.file_uploader("Upload a file to encrypt")

    if uploaded:
        file_bytes = uploaded.read()

        if st.button("Encrypt"):
            enc_key, nonce, tag, ciphertext = encrypt_file(file_bytes)

            # Combine all encrypted parts
            final_data = enc_key + b"::" + nonce + b"::" + tag + b"::" + ciphertext
            
            # Convert to Base64 for safe file download
            final_b64 = base64.b64encode(final_data)

            st.success("File encrypted successfully!")

            # Proper encrypted file download
            st.download_button(
                label="📥 Download Encrypted File",
                data=final_b64,
                file_name=f"{uploaded.name}.enc",
                mime="text/plain"
            )


# ---------------------------------------------------------
# DECRYPT FILE
# ---------------------------------------------------------
elif menu == "Decrypt File":
    uploaded = st.file_uploader("Upload encrypted .enc file")

    if uploaded:

        file_bytes = uploaded.read()

        try:
            # Fix: Add padding to prevent "Incorrect padding" error
            raw = base64.b64decode(file_bytes + b'===')

            enc_key, nonce, tag, ciphertext = raw.split(b"::", 3)

            if st.button("Decrypt"):

                try:
                    plaintext = decrypt_file(enc_key, nonce, tag, ciphertext)

                    st.success("File decrypted successfully!")

                    # Download decrypted original file
                    st.download_button(
                        label="📥 Download Decrypted File",
                        data=plaintext,
                        file_name=uploaded.name.replace(".enc", ""),
                        mime="application/octet-stream"
                    )

                except Exception as e:
                    st.error(f"Decryption failed: {e}")

        except Exception as e:
            st.error(f"Invalid encrypted file format! Error: {e}")
