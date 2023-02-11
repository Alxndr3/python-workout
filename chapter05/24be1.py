"""“Encrypt” a text file by turning all of its characters into their numeric
equivalents (with the built-in ord function) and writing that file to disk. Now
“decrypt” the file (using the built-in chr function), turning the numbers
back into their original characters."""

def encrypt_file(infile, encrypted_file):
    list_line = []
    with open(infile, 'r') as inf, open(encrypted_file, 'w') as ouf:
        for line in inf:
            for c in line.strip():
                ouf.write((f"{str(ord(c))}\n"))
            ouf.write(str(ord('\n')))


def decrypt_file(infile, decrypted_file):
    with open(infile, 'r') as ef, open(decrypted_file, "w") as denf:
        for line in ef:
            for c in line.split():
                denf.write(chr(int(c)))


#encrypt_file("files/fstab", "files/fstab_encrypted")
#decrypt_file("files/fstab_encrypted", "files/decrypted_encrypted_file")


"""Solution to chapter 5, exercise 24, beyond 1: encrypt"""

def encrypt(filename, text):
    with open(filename, 'w') as outfile:
        for one_character in text:
            outfile.write(f'{ord(one_character)}\n')


def decrypt(filename):
    characters = [chr(int(one_character))
                  for one_character in open(filename)
                  if one_character.strip().isdigit()]
    return ''.join(characters)

encrypt("files/fstab_bs", "files/fstab")
print(decrypt("files/fstab_bs"))

