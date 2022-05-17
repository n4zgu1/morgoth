def encrypt_for_transefer(filename, password):
    with open(filename, 'rb') as f_in:
        original_data = f_in.read()
        print(original_data)
    encrypted = bytes(a ^ b for (a, b) in zip(original_data, password))
    print(encrypted)
    #with open(filename, 'wb') as f_out:
    #    pass

encrypt_for_transefer('testfile.txt', b'tttt')