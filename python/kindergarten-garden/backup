class Garden:

    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram
        self.students = sorted(students)

        
        # print(type(self.diagram))
        # print(type(self.students))
        
        
        # temp_dict = dict(zip(students,rows))
        # print(temp_dict)
        # print(len(rows))
        # print(len(students))
        # temp_len = len(students)
        # print(len(students))
        # print(row1, row2)
        # print(plant_layout)
    def plants(self, name):
        """
        This does too much
        """
        
        self.name = name
        students = self.students
        diagram = self.diagram
        # print(sorted(students))
        # student_index = students.index(self.name)

        plant_layout = tuple(diagram.split("\n"))
        row1, row2 = plant_layout

        # Match length of row1 and row2 to double length of students with empty elements
        temp_len = len(students) * 2 - len(row1)
        row1 = list(row1)
        row2 = list(row2)
        row1 = [ row1[i:i+2] for i in range(0, len(row1), 2) ] #group elements in row1 by 2 
        row2 = [ row2[i:i+2] for i in range(0, len(row2), 2) ] #group elements in row2 by 2

        rows = [j for i in zip(row1, row2) for j in i]  #zip merge row1 and row2 into rows

        rows = [item for sublist in rows for item in sublist]
        # print(rows)
        # print(row1)
        # print(row2)
        while temp_len > 0:
            rows.append(None)
            rows.append(None)
            temp_len -= 1

        naming_list = []
        for plant in rows:
            if plant == "C":
                naming_list.append("Clover")
                # print(naming_list)
            elif plant == "R":
                naming_list.append("Radishes")
            elif plant == "G":
                naming_list.append("Grass")
            elif plant == "V":
                naming_list.append("Violets")
            else:
                naming_list.append(plant)

        rows = naming_list
        rows = [ rows[i:i+4] for i in range(0, len(rows), 4) ]
        school_dict = zip(students, rows)
        school_dict = dict(school_dict)
        # print(rows[student_index])
        # print(school_dict)
        # print(self.name)
        return school_dict.get(self.name)
        
    # def plant_type(self, plant):
    #     """
    #     Converts letters to plant names
    #     Returns list of plant names
    #     """
    #     self.plant = plant
    #     naming_list = []
    #     for life in self.plant:
    #         if self.plant == "C":
    #             naming_list.append("Clover")
    #         elif self.plant == "R":
    #             naming_list.append("Radishes")
    #         elif self.plant == "G":
    #             naming_list.append("Grass")
    #         elif self.plant == "V":
    #             naming_list.append("Violets")
    #     return naming_list




# garden = Garden("VC\nRC")
# print(garden.plants("Alice"))
# # ["Violets", "Clover", "Radishes", "Clover"]


# garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
# print(garden.plants("Alice"))

# garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
# print(garden.plants("Harriet"))
# # ["Violets", "Radishes", "Radishes", "Violets"]

# garden = Garden(
#             "VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"]
#         )
# print(garden.plants("Patricia"))
# # ["Violets", "Clover", "Radishes", "Violets"]