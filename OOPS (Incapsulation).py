class Student:
    def __init__(self, marks):
        self.__marks = marks
    
    def show_marks(self):
        # Yahan humein bracket mein kuch bhejne ki zaroorat nahi
        print(f"Mere {self.__marks} marks aaye hain! 🎓")

    def update_marks(self, new_marks):
        if new_marks > 0:
            self.__marks = new_marks
            print(f"Marks update hokar {new_marks} ho gaye! ✅")
        else:
            print("Invalid marks! ❌")

# 1. Object banao (Shuruati marks ke saath)
s = Student(92) 

# 2. Marks dekho
s.show_marks() 

# 3. Marks update karo (Usi same object 's' ke marks)
s.update_marks(100)

# 4. Phir se check karo updated marks
s.show_marks()
