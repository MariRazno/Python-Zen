def real_zen(input_file, output_file):
    necessary = []
    with open(input_file, 'r') as zen:
        text = zen.read()
        sent = text.split('\n')
        print(sent)
        get_out = []
        for i in sent:
            if i.startswith("//"):
                get_out.append(i)
            else:
                necessary.append(i)
    with open(output_file, 'w') as new_zen:
        start = []
        rules = []
        for i in necessary:
            if i.startswith("Title: ") or i.startswith("Author: "):
                start.append(i)
            else:
                rules.append(i)
        for i in start:
            i = i.replace("Title: ", "") or i.replace("Author: ", "")
            new_zen.write(i+"\n")
        for num in enumerate(rules):
            new_zen.write(str(num[0]) + ". " + str(num[1])+ "\n")


real_zen(r"C:\PyCharmGrammarly\Grammarly\classes_3_python_data_zen.txt", r"C:\PyCharmGrammarly\Grammarly\out_put_zen.txt")
