```python
myself = {
    'Name' : 'Vee',
    'Status' : 'Undergradute',
    'Interest' : 'Data',
    'Programming SKills' : ['Python', 'SQL', 'R']
}

print(myself)


class ActiveLearner:
    def __init__(self, name, job, interest):
        self.name = name
        self.job = job
        self.interest = interest

    def greeting(self):
        print(f" Hi! I am a {self.job}. My name is {self.name}, I am interest in {self.interest}")


f1 = ActiveLearner('Vee', 'Student', 'a world of data')

f1.greeting()
```
