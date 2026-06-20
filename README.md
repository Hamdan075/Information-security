# Hybrid RSA + AES Encryption App

This is a web-based application built with [Streamlit](https://streamlit.io/) that allows you to securely encrypt and decrypt files using a hybrid encryption scheme. It leverages the speed of AES for file data encryption and the security of RSA for protecting the AES key.

## How it Works

The application uses **Hybrid Encryption**:
- **AES (Advanced Encryption Standard)**: A symmetric encryption algorithm used to quickly encrypt and decrypt the actual file contents.
- **RSA (Rivest-Shamir-Adleman)**: An asymmetric encryption algorithm used to securely encrypt the AES key. 

When you encrypt a file:
1. A random AES key is generated.
2. The file is encrypted using the AES key.
3. The AES key is then encrypted using an RSA public key.
4. The encrypted file, the encrypted AES key, and other necessary decryption metadata are bundled together in a base64 encoded `.enc` file.

When you decrypt a file:
1. The application reads the `.enc` file and extracts the encrypted AES key.
2. The AES key is decrypted using your RSA private key.
3. The decrypted AES key is used to decrypt the original file data.

## Project Structure

- `app.py`: The main Streamlit web application interface.
- `crypto_utils.py`: Contains the core cryptography logic (using PyCryptodome) for file encryption and decryption.
- `keygen.py`: A helper script to generate the RSA public and private key pairs.
- `keys/`: Directory where the RSA `public.pem` and `private.pem` keys are stored.
- `requirements.txt`: The Python dependencies needed to run the project.

## Setup and Installation

1. Make sure you have Python installed.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Generate your RSA key pairs (if not already present):
   ```bash
   python keygen.py
   ```
   *This will create `keys/public.pem` and `keys/private.pem`.*

## Running the Application

To start the Streamlit application, run the following command in your terminal:

```bash
streamlit run app.py
```

This will automatically open the application in your default web browser (typically at `http://localhost:8501`).

## Usage

### Encrypt a File
1. Select **Encrypt File** from the sidebar.
2. Upload any file you wish to encrypt.
3. Click the **Encrypt** button.
4. Download the resulting `.enc` file.

### Decrypt a File
1. Select **Decrypt File** from the sidebar.
2. Upload the encrypted `.enc` file.
3. Click the **Decrypt** button.
4. Download your original file.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/)
