class ArbreBinaire:
    def __init__(self, valeur, name, parent):
        self.valeur = valeur
        self.parent = parent
        self.name = name
        self.node = []

    def insert(self, valeur, name):
        for node in self.node:
            if node.name == name:
                node.valeur = valeur
        self.node.append(ArbreBinaire(valeur, name, self))

    def update_tree(self):
        result = self.valeur
        for node in self.node:
            node.update_tree()
            result += node.valeur
        self.valeur = result

    def get_child(self, Name):
        for node in self.node:
            if node.name == Name:
                return node
        self.node.append(ArbreBinaire(0, Name, self))
        return self.get_child(Name)


    def bigger(self):
        return max([self.valeur] + [i.valeur for i in self.node])

    def get_valeur(self):
        return self.valeur

    def get_parent(self):
        return self.parent

    def calc(self):
        result = 0
        for ch in self.node:
            if ch.valeur <= 100000 and ch.node != []:
                result += ch.valeur
            result += ch.calc()
        return result

    def ola(self, value):
        result = []
        for ch in self.node:
            if (value + ch.valeur) >= 30000000 and ch.node != []:
                result += [ch.valeur]
                result += ch.ola(value)
        return result


with open('input.txt') as f:
    lines = f.readlines()

tree = ArbreBinaire(0, "/", None)

test_input = [
"$ ls",
"dir a",
"14848514 b.txt",
"8504156 c.dat",
"dir d",
"$ cd a",
"$ ls",
"dir e",
"29116 f",
"2557 g",
"62596 h.lst",
"$ cd e",
"$ ls",
"584 i",
"$ cd ..",
"$ cd ..",
"$ cd d",
"$ ls",
"4060174 j",
"8033020 d.log",
"5626152 d.ext",
"7214296 k"]

result = 0
cd_name = ""

current_node = tree

for line in lines:
#for line in test_input:
    line.replace("\n", "")

    if line.startswith("$ cd"):
        if line.startswith("$ cd .."):
            current_node = current_node.parent
            continue
        cd_name = line.split(" ")[2]
        current_node.insert(0, cd_name)
        current_node = current_node.get_child(cd_name)
        continue

    if line.startswith("$ ls"):
        continue

    if line.startswith("dir"):
        current_node.insert(0, line.split(" ")[1])
        continue

    temp = line.split(" ")
    current_node.insert(int(temp[0]), temp[1])



tree.update_tree()
print(tree.bigger())
print(tree.calc())
print(tree.ola(70000000 - tree.valeur))
print(min(tree.ola(70000000 - tree.valeur)))

print("----- PART 2 -----")