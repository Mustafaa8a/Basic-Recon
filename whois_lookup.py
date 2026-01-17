import whois
def whoIs(domain):
    try:
        who = whois.whois(domain)
        print("-"*50+"WHOIS Data"+"-"*50)
        print(f"Registrar     : {who.registrar}")
        print(f"Creation Date : {who.creation_date}")
        print(f"Expiration Date   : {who.expiration_date}")
        print(f"Name Servers  : {who.name_servers}")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__=="__main__":
    domain=input("Enter domain name: ")
    whoIs(domain)
