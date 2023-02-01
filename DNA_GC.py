with open("Seq.fa") as df:
    for line in df:
        upper_df = line.upper()
        no_A = upper_df.replace('A', '')
        no_T = no_A.replace('T', '')
        GC_content = (len(no_T)/len(upper_df))*100
        print(upper_df)
        print("GC content is: %5.2f %%" %GC_content)
        # @sharifrahmanie
