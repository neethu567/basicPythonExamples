"""iterators """
class topten:
    def __init__(self):
        self.nums=1
    def __iter__(self):
        return self
    def __next__(self):
        var=self.nums
        if self.nums<10:
            self.nums+=1
            return var
        else:
            raise StopIteration

v=topten()
for i in v:
    print(i)

nums=[1,3,4,5]
it =iter(nums)
print(next(it))
print(next(it))
