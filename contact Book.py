contacts = {}

while True:
    print("\n1.Add  2.View  3.Search  4.Update  5.Delete  6.Exit")
    c = input("Choose: ")

    if c=="1":
        n=input("Name: "); p=input("Phone: ")
        e=input("Email: "); a=input("Address: ")
        contacts[n]={"Phone":p,"Email":e,"Address":a}
    elif c=="2":
        [print(f"{n} - {d['Phone']}") for n,d in contacts.items()]
    elif c=="3":
        s=input("Search name/phone: ")
        f=[(n,d) for n,d in contacts.items() if n==s or d["Phone"]==s]
        print(f"Found: {f}" if f else "Not found")
    elif c=="4":
        n=input("Name to update: ")
        if n in contacts:
            contacts[n]={"Phone":input("New Phone: "),"Email":input("New Email: "),"Address":input("New Addr: ")}
    elif c=="5":
        contacts.pop(input("Name to delete: "),"Not found")
    elif c=="6": break