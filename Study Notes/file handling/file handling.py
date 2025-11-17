names = ["Marcus", "Kyle", "Gelo", "CJ"]
new_names = []

file_path = "result.txt"

with open(file_path, "w") as file:
    for name in names:
        file.write(name + "\n")
    print(f"its done")

with open(file_path, "r+") as file:
    names = []
    for line in file:
        name = line.strip()
        if name == "":
            names.append("Sigma Boy")
        else:
            names.append(name)
    new_name = "\n".join(names)

    file.seek(0)
    file.write(new_name)


