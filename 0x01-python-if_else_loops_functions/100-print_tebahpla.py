for char_code in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(char_code) if (char_code - ord('z')) % 2 == 0 else "{:c}".format(char_code - 32), end='')
