def extract_emails():
    while True:
        try:
            filnavn_epost = input("Name of the file with emails: ")
            filnavn_write = input("Name the file it should be written to: ")
            filvariabel_epost = open(filnavn_epost, 'r')
            filvariabel_write = open(filnavn_write, 'w')
            for linje in filvariabel_epost:
                linje.strip()
                if linje.startswith("From: "):
                    eposter = linje[linje.find("<") + 1:linje.find(">")]
                    filvariabel_write.write(eposter + '\n')
            filvariabel_epost.close()
            filvariabel_write.close()
            break
        except FileNotFoundError:
            print("Write a valid filename with .txt in the end!! (filnavn.txt)")


if __name__ == "__main__":
    extract_emails()
