if __name__ == "__main__":

    with open("kitten.jpeg", "rb") as file:
        prvni_dva_bajty = file.read(2)
        if prvni_dva_bajty == b'\xff\xd8':
            print("Soubor je typu JPEG.")
        else:
            print("Soubor není typu JPEG.")
