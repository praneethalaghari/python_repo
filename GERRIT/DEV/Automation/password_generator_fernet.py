from cryptography.fernet import Fernet

#key = Fernet.generate_key()
key = b'XpQu2hhMOyDhKs222X_CX5dfyLBUPWaoX93t_3-fkS8='

f = Fernet(key)

#encrypt_value = f.encrypt(b"booki123")
encrypt_value = b'gAAAAABeGLw8mHQBdvh5jDZyDzaigWMwyaMSSZSoabBKytVo4CvWwzFd7XI50JAcb-3W6l3KSofNVxyx8XaWcXTKQpyVH4zBUA=='

decrypt_value = f.decrypt(encrypt_value)
