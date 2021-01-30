"""class methos"""
class studnet:
    school="admaren"
    def __init__(self,name,age,std):
        self.name=name
        self.age=age
        self.std = std

    @classmethod
    def student_name(cls,instance):
        instance.name = "NEw NameA changed with class method"
        instance.age = "NEw age changed with class method"
        print(f"Student Name : {instance.name}, {instance.age}")

    @staticmethod
    def staticcls(instance):
        print(instance.name)

# s1=studnet("aaaa",22)
# studnet.studentclas(s1)
# studnet.staticcls(s1)
# s1.staticcls()
