import dns.resolver
def dnsEnum(target):

    record_types = ["A","MX", "NS"]
    try:
        resolver = dns.resolver.Resolver()
        for recordType in record_types:
            try:
                res = resolver.resolve(target, recordType)
            except dns.resolver.NoAnswer:
                continue
            print("-"*60)
            print(f"\"{recordType}\" records for {target}")
            for data in res:
                print(data)

    except Exception as e :
        print(f"Error: {e}")

if __name__=="__main__":
    domain = input("Enter domain name: ")
    dnsEnum(domain)
