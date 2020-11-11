from decimal import Decimal
from fractions import Fraction
import random


class QuestionMaker:

	def __init__(self):
		self.init()

	def init(self):
		self.numChoices = 3
		#incorrectAnswers and correctAnswers scrambled
		self.mixedAnswers = []
		#only correct answers
		self.correctAnswerSet = []
		self.goalFractFraction = []

	def genNumCorrect(self, level):
		#restrict number of fractions to add up based on level.
		if(level <= 3) : return 1
		elif(level <= 6) : return random.randint(1, 2)
		return random.randint(1, 3)
		
	def getChoices(self):
		return self.mixedAnswers
	
	def getAnswers(self):
		return self.correctAnswerSet
		
	def getAnswerNum(self):
		return self.goalFractFraction

	# Returns a new goal based on givven level
	def createGoal(self, level):
		if level < 5:
			denom = random.randint(2, 5)
		elif level > 5 and level < 20:
			denom = random.randint(2, level - 1)
		else:
			denom = random.randint(2, 20)
		return [random.randint(1, denom), denom]

	'''
	goal = 6
	possible denom = [2, 3, 6, 12, 18]

	'''

	def createCorrectAnswers(self, goal):
		# generate list of denominators from 2..20 divisible by goal denominator
		# goal[0] is numerator, goal[1] is denominator
		# you must access these outside of goal_Fract as goal_Fract will reduce to lowest terms.
		goal_denom = goal[1]
		possible_denom = list()
		goal_Fract = Fraction(goal[0], goal[1])
		for x in range(2, 21):
			if goal_denom % x == 0 or x % goal_denom == 0:
				possible_denom.append(x)
		
		print("possible denominators defined")
		#select denom
		first_denom = possible_denom[random.randint(0, len(possible_denom) - 1)]
		#base of first_fract
		first_fraction = Fraction(1, first_denom)
		print("first denominator set")
		multiple_range = first_fraction // goal_Fract
		rngVal = []
		for x in range(1, multiple_range - 1):
			rngVal.append(x)
		print("numenator magnitude choices made")
		magnitude_select = random.choice(rngVal)
		print("numerator magnitude chosen")
		first_fract = first_fraction * magnitude_select
		print("fraction magnitude applied")
		second_fract = goal_Fract - first_fract

		print("second fraction set")

		first_correct = [first_fract.numerator, first_fract.denominator]
		second_correct = [second_fract.numerator, second_fract.denominator]
		print("fractions converted to lists")
		return  [first_correct, second_correct]
		
	def createIncorrectAnswers(self, goal, correctAnswers):

		goal_fract = Fraction(goal[0], goal[1])
		correct_fracts = [Fraction(correctAnswers[0][0], correctAnswers[0][1])]
		incorrect_fract = Fraction(0,0)

		print("entering incorrect answers verification loop")
		cont = True
		while cont:
			incorrect_denom = random.randint(2, goal[1])
			incorrect_fract = Fraction(random.randint(1, goal[1]), incorrect_denom)
			print("testing conflict with " + incorrect_fract + " to " + correct_fracts[0] + ", " + correct_fracts[1] + " for goal " + goal_fract)
			if incorrect_fract + correct_fracts[0] != goal_fract and incorrect_fract + correct_fracts[1] != goal_fract and incorrect_fract != goal_fract:
				cont = False

		return [incorrect_fract.numerator, incorrect_fract.denominator]

	def randomizeOrder(self):
		# Choose 2 correct, 1 incorrect

		order = [random.choice([True, False])]
		if not order[0]:
			order.append(True)
			order.append(True)
		else:
			order.append(random.choice([True,False]))
			order.append(not order[1])
		print(order)
		return order

	def makeNextQuestion(self, level):
		#clear your answerSet and instantiate necessary temporary variables
		self.init()
		print("STARTING")
		self.correctAnswerSet = self.randomizeOrder()
		print("ORDER CHOSEN")
		self.goalFractFraction = self.createGoal(level)
		print("GOAL SET")

		# to build self.mixedAnswers
		correctAnswers = self.createCorrectAnswers(self.goalFractFraction)
		print("CORRECT ANSWERS CHOSEN")
		incorrectAnswer = self.createIncorrectAnswers(self.goalFractFraction, correctAnswers)
		print("INCORRECT ANSWERS CHOSEN")

		#mix answers
		#which correct answer appears first
		correctOrder = random.randint(0,1)

		# if  is True, choice is a correct answer
		if self.correctAnswerSet[0]:
			self.mixedAnswers.append(correctAnswers[correctOrder])
			if correctOrder == 0:
				correctOrder = 1
			else:
				correctOrder = 0
		else:
			self.mixedAnswers.append(incorrectAnswer)
		
		if self.correctAnswerSet[1]:
			self.mixedAnswers.append(correctAnswers[correctOrder])
			if correctOrder == 0:
				correctOrder = 1
			else:
				correctOrder = 0
		else:
			self.mixedAnswers.append(incorrectAnswer)
		
		if self.correctAnswerSet[2]:
			self.mixedAnswers.append(correctAnswers[correctOrder])
		else:
			self.mixedAnswers.append(incorrectAnswer)

		


		'''numCorrect = self.genNumCorrect(level)
		numIncorrect = self.numChoices - numCorrect
		remainingInCorrect = numCorrect
		levelDenom = 0
		'''

		
		'''
		#generate non-zero goal numerator and denominator
		if(level <= 6): levelDenom = 8
		else:
			levelDenom = 4 + int((level * level) / (level + level))
			if(levelDenom > 20) : levelDenom = 20
			
		
		goal = random.randint(numCorrect, (levelDenom - 1))
		#goalMod = goal % 2
		#if(goalMod != 0) :
			#goal = goal - 1
		
		#Turn goal into a fraction, and reduce it an arbitrary amount.
		cont = False
		extra = 0
		goalNumer = goal
		goalDenom = levelDenom
		goalMod = 0
		
		while(cont == False) :
			# randomly leave fraction unreduced
			print(goalNumer)
			print(goalDenom)
			
			extra = random.randint(1,3)
			
			if(extra <= 2) :
				#is the value and the denominator divisible by five?
				goalMod = goalNumer % 5
				if(goalMod == 0) :
					goalMod = goalDenom % 5
					if(goalMod == 0) :
						#both are divisible by 5. Reduce, then repeat the loop.
						goalNumer = goalNumer / 5
						goalDenom = goalDenom / 5
					else: 
						#check if they are divisible by two instead.
						goalMod = goalNumer % 2
						if(goalMod == 0) :
							goalMod = goalDenom % 2
							if(goalMod == 0) :
								#both are divisible by two. Reduce, then repeat the loop.
								goalNumer = goalNumer / 2
								goalDenom = goalDenom / 2
							else: 
								# denominator not divisible by two. Can't be reduced further.
								cont = True
						else:
							#value not divisible by two. Can't be reduced further.
							cont = True
				else:
					#The value was not divisible by five. Check for divisible by two.
					goalMod = goalNumer % 2
					if(goalMod == 0) :
						goalMod = goalDenom % 2
						if(goalMod == 0) :
							# Both are divisible by two. Reduce and repeat loop.
							goalNumer = goalNumer / 2
							goalDenom = goalDenom / 2
						else:
							# denom not divisible by two. Can't be reduced further.
							cont = True
					else:
						# Value can't be divided by two. Can't be reduced further.
						cont = True
			else: cont = True
		
		
		
		#save the goal fraction
		self.goalFractFraction.append(goalNumer)
		self.goalFractFraction.append(goalDenom)
		#self.goalFract = float(goal) / 40.0
		
		#generate correct Answers that add up to goal
		for i in range(1,numCorrect + 1):
			#more temp variables (ones that are reset each round)
			value = 0
			valueMod = 0
			extra = 0
			denom = levelDenom
			
			if(i != numCorrect) :
				#insure we don't have any fractions that are equal to zero
				value = random.randint(1, (goal - (1 *(numCorrect - i))))
				#valueMod = value % 2
				
				#if(valueMod != 0) :
					#value = value - 1
			else :
				value = goal
			
			#subtract our value from the goal before we change it to a fraction
			goal = goal - value
			
			#get a denominator and numerator value (maximum is fortieths)
			extra = 0
			cont = False
			
			while(cont == False) :
				#randomly leave fraction unreduced
				extra = random.randint(1,3)

				if(extra <= 2) :
					#is the value and the denominator divisible by five?
					valueMod = value % 5
					if(valueMod == 0) :
						valueMod = denom % 5
						if(valueMod == 0) :
							#both are divisible by 5. Reduce, then repeat the loop.
							value = value / 5
							denom = denom / 5
						else: 
							#check if they are divisible by two instead.
							valueMod = value % 2
							if(valueMod == 0) :
								valueMod = denom % 2
								if(valueMod == 0) :
									#both are divisible by two. Reduce, then repeat the loop.
									value = value / 2
									denom = denom / 2
								else: 
									# denominator not divisible by two. Can't be reduced further.
									cont = True
							else:
								#value not divisible by two. Can't be reduced further.
								cont = True
					else:
						#The value was not divisible by five. Check for divisible by two.
						valueMod = value % 2
						if(valueMod == 0) :
							valueMod = denom % 2
							if(valueMod == 0) :
								# Both are divisible by two. Reduce and repeat loop.
								value = value / 2
								denom = denom / 2
							else:
								# denom not divisible by two. Can't be reduced further.
								cont = True
						else:
							# Value can't be divided by two. Can't be reduced further.
							cont = True
				else: cont = True
			
			#Now turn the denominator and value into a pair.
			tempArray = []
			tempArray.append(value)
			tempArray.append(denom)
			#tempArray = str(value) + "/" + str(denom)
			correctAnswers.append(tempArray)
			
		
		#generate potentially incorrect answers
		for i in range(1,numIncorrect + 1):
			#more temp variables (ones that are reset each round)
			value = 0
			valueMod = 0
			extra = 0
			denom = levelDenom
			
			#make a fraction that is at least reduce-able once and not equal to zero
			value = random.randint(2, (levelDenom - 1))
			#valueMod = value % 2
			
			#if(valueMod != 0) :
				#value = value - 1
			
			#get a denominator and numerator value (maximum is twentieths)
			extra = 0
			cont = False
			
			while(cont == False) :
				#randomly leave fraction unreduced
				extra = random.randint(1,3)

				if(extra <= 2) :
					#is the value and the denominator divisible by five?
					valueMod = value % 5
					if(valueMod == 0) :
						valueMod = denom % 5
						if(valueMod == 0) :
							#both are divisible by 5. Reduce, then repeat the loop.
							value = value / 5
							denom = denom / 5
						else: 
							#check if they are divisible by two instead.
							valueMod = value % 2
							if(valueMod == 0) :
								valueMod = denom % 2
								if(valueMod == 0) :
									#both are divisible by two. Reduce, then repeat the loop.
									value = value / 2
									denom = denom / 2
								else: 
									# denominator not divisible by two. Can't be reduced further.
									cont = True
							else:
								#value not divisible by two. Can't be reduced further.
								cont = True
					else:
						#The value was not divisible by five. Check for divisible by two.
						valueMod = value % 2
						if(valueMod == 0) :
							valueMod = value % 2
							if(valueMod == 0) :
								# Both are divisible by two. Reduce and repeat loop.
								value = value / 2
								denom = denom / 2
							else:
								# denom not divisible by two. Can't be reduced further.
								cont = True
						else:
							# Value can't be divided by two. Can't be reduced further.
							cont = True
				else: cont = True
			
			#Now turn the denominator and value into a string for a fraction 
			tempArray = []
			tempArray.append(value)
			tempArray.append(denom)
			#tempString = str(value) + "/" + str(denom)
			incorrectAnswers.append(tempArray)
		
		#self.correctAnswerSet.extend(correctAnswers)
		
		#Now mix the answers together to ensure that one can't guess based on order.
		remainingVars = self.numChoices
		intendedAnsArray = []
		for i in range(1,self.numChoices + 1):
			
			nextIndex = random.randint(1,remainingVars)
			
			if(nextIndex > remainingInCorrect) :
				# use an incorrect Answer
				nextIndex = nextIndex - (remainingInCorrect + 2)
				intendedAnsArray.append(False)
				self.mixedAnswers.append(incorrectAnswers.pop(nextIndex))
			else:
				# use a correct Answer
				nextIndex = nextIndex - 1
				intendedAnsArray.append(True)
				self.mixedAnswers.append(correctAnswers.pop(nextIndex))
				remainingInCorrect = remainingInCorrect - 1
				
			remainingVars = remainingVars - 1
		
		self.correctAnswerSet.append(intendedAnsArray)
		
		#Now determine if any of the incorrect answers are equal to the correct answers
		#if(numCorrect != 3) :
		
			#acceptableAns = []
			
			#No 123 possibility since that would mean that all three were in the intended answer, meaning that no combination of the pieces except 123 would get the desired result.
			#for i in range(0, self.numChoices):
				
				#if((self.goalFractFraction[0] % self.mixedAnswers[i][0] == 0) or (self.mixedAnswer[i][0] % self.goalFractFraction[0] == 0)) :
					#One of the numerators is divisible by the other numerator. This means that the two fractions (goal and answer) could potentially be equal.
					#denomMult1 = self.goalFractFraction[0] * self.mixedAnswer[i][1]
					#denomMult2 = self.goalFractFraction[1] * self.mixedAnswer[i][0]
					#if(denomMult1 == denomMult2):
						#They are equal. Append this to acceptableAns.
						#if(i == 0) : acceptableAns.append([True, False, False])
						#elif(i == 1) : acceptableAns.append([False, True, False])
						#else : acceptableAns.append([False, False, True])
						
					#for j in range(i + 1, self.numChoices) :
						# add the fractions together without using floats by multiplying their denominators and multiplying numerators by their opposing denominator.
						#sumNumer = ((self.mixedAnswer[i][0] * self.mixedAnswer[j][1]) + (self.mixedAnswer[j][0] * self.mixedAnswer[i][1]))
						#sumDenom = (self.mixedAnswer[i][1] * self.mixedAnswer[j][1])
						#denomMult1 = self.goalFractFraction[0] * sumDenom
						#denomMult2 = self.goalFractFraction[1] * sumNumer
					
						#if(denomMult1 == denomMult2) :
							#The sum of the two fractions are equal to the goal fraction. Add them to acceptableAns.
							#if(i == 0) :
								#if(j == 1) : acceptableAns.append([True, True, False])
								#else : acceptableAns.append([True, False, True])
							#elif(i == 1) : acceptableAns.append([False, True, True])
					
			# extend the correct answer set with acceptable Ans.
			#print acceptableAns
			#self.correctAnswerSet.extend(acceptableAns)


#def __init__(self,questionType):
		##The number of total answers
		##Give us a random number representing the number of correct answers
		#numCorrect = random.randint(2, 4)
		#correctAnswers = []
		#incorrectAnswers = []
		#print numCorrect

		##break 1 into x amount of sections(number of correct answers)
		#section = float(1) / float(numCorrect)

		##generate the correct answers (pulls out a chunk from section)
		#for i in range(0, numCorrect):
			#fraction = round(random.uniform(0.1, section), 2)
			#correctAnswers.append(fraction)
			#print(fraction)

		#print correctAnswers

		##add correct answers together to get goal decimal
		#goal = sum(correctAnswers)
		#print goal

		##how many incorrect answers should we generate? (toal number of questions minus correct answers)
		#dummyQuestions = numChoices - numCorrect
		#print dummyQuestions

		##generate dummy questions
		#for i in range(0, dummyQuestions):
			#fraction = round(random.uniform(0.1, 0.9), 2)
			#incorrectAnswers.append(fraction)

		#print incorrectAnswers
		'''