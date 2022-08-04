Class ActiveLearner(person):
		def __init__(self, name, job, interest):
				super().__init__(name)
				self.job = job
				self.interest = interest
				
		def greeting(self):
				print(f" Hi! I am a {self.job}. My name is {self.name}, I am interest in {slef.interest}")


f1= ActiveLearner('Vee', 'Student', 'a world of data')

f1.greeting()
