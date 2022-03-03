#Matthew Lane P1M5
type_report = input("Select a report type: all Items (\"A\") or Total Only (\"T\")!")
def adding_report(T):
    total = 0
    items = "" 
    while True:
        report = input("Input an integer or \"Q\" :")
        if report.isdigit() == True:
            total =  total + int(report)
            if type_report == "A":
                items += report + "\n"
        elif report.startswith("Q") == True:
                if type_report == "A":
                    print("Items", "\n", items)
                    print("Total", "\n", total)
                elif type_report == "T":
                    print("Total", "\n", total)
                else:
                    print(type_report, "input is invalid")
                break
        else:
            print(report, "input is invalid")
                         
adding_report("A")