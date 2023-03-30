number = "347891"
result = ""
 for cixarilan in number:
    if cixarilan != '3' and cixarilan != '7':
        result += cixarilan

        if len(result) < 4:
            print("Ededi duzgun daxil edin:")
            else:
                print("Yekun eded:", int(result[:4]))
