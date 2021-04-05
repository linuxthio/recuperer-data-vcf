


def load_vcf(filename):
    sortie=[]
    try:
        with open(filename,'r') as f:
            t=f.readlines()
            # print(t)
            # recuperation des contacts
            print(type(t),len(t))
            i=0
            for e in t:
                if e=="BEGIN:VCARD\n" or e=='END:VCARD\n':
                    sortie.append("===")
                else:
                    
                    sortie.append(e)
            # for e in t:
            #     if e=="BEGIN:VCARD":
            #         uncontact=[]
            #         while e!='END:VCARD':
            #             print(e,i)
            #             uncontact.append(e)
            #         sortie.append(uncontact)
            #     i=i+1
    except:
        print(f"Warning : file {filename} dosen't exist ")

    return str(sortie)

filename="mescontacts2021.vcf"

ss=load_vcf(filename)
print(ss,type(ss))


