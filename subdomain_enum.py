import requests,json
def subEnum(domain):
    # we use crt.sh in this case to uncover hidden subdomains
    URL=f"https://crt.sh/?q={domain}&output=json"
    # set used to remove duplicates
    subDomains=  set()
    try:
        res = requests.request(method="GET",url=URL,timeout=10)
        # check that there is no error in the response 
        if res.status_code!=200:
            print("[-]Error: couldn't fetch data from crt.sh")
            return
        # we ruterned data in a json format so we can handle it 
        data = json.loads(res.text)
        """ 
        json data format
        {
        "issuer_ca_id": 16418,
        "name_value": "*.mail.example.com\nsmtp.example.com",
        "common_name": "*.mail.example.com"
        }
        """

        # get all sub domain in each json object 
        # every name_value key may have one or more subdomain separated by \n
        for obj in data:
            subDomain = obj.get("name_value","")
            for sub in subDomain.split("\n"):
                sub = sub.strip()

                # remove wild card char 
                if sub.startswith("*."):
                    # skip first 2 chars
                    sub = sub[2:]

                # Add subdomain in the set 
                if sub.endswith(f"{domain}"):
                    subDomains.add(sub)

        # Sort set of subdomains
        subDomains = sorted(subDomains)

        print("-"*50+f" Subdomains for {domain} "+"-"*50)
        for sub in subDomains:
            print(sub)


    except Exception as e:
        print(f"[-] Error: {e}")

if __name__=="__main__":
    domain=input("Enter domain name: ")
    subEnum(domain)
