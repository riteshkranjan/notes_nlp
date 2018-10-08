from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob
training_corpus = [
                   ('The work outstanding is Provide needs completing', 'Out of scheduled hours'),
		   ('The work outstanding is Fault on current line', 'Out of scheduled hours'),
		   ('The work outstanding is Ug', 'Out of scheduled hours'),
		   ('The work outstanding is New e', 'Out of scheduled hours'),
		   ('The work outstanding is Lead in', 'Out of scheduled hours'),
		   ('The work outstanding is Another fault on line', 'Out of scheduled hours'),
		   ('The work outstanding is Waiting on job', 'Out of scheduled hours'),
                   ('I am passing to an engineer with a heavy lid lifter', 'Assistance- Heavy lift required'),
                   ('I cannot complete this task because Sales query', 'Sales Query'),
                   ('Task Completed Successfully', 'Task Completed Successfully'),
                   ('job was allocated past my end of day', 'Track and Locate required'),
                   ('track locate engineer cannot get to me until the morning', 'Track and Locate required'),
                   ('Splicer,obtaining tomorrow  were required which could not be obtained on the day', 'Splicer required'),
                   ('Closing down as no access','No Access'),
                   ('Closing down as no access','Assistance- Hoist required'),
		   ('hoist needed to get line from dp to carrier pole',	'Assistance- Hoist required'),
		   ('Needs hoist','Assistance- Hoist required'),
		   ('The work outstanding is Provide two spans of dropwire','Assistance- Hoist required'),
		   ('No access', 'No Access'),
		   ('Difficult cable run involved through false ceiling', 'Assistance- Cabling required'),
		   ('I am passing to an engineer with a heavy lid lifter', 'Assistance- Heavy lift required'),
		   ('flat roof engineer required for DP that cannot be reached from ladders', 'Assistance- Ladder required'),
		   ('Assistance required for DP that cannot be reached from ladders', 'Assistance- Ladder required'),
		   ('I do not have the skills required to complete the task and could not obtain assistance on the day','Assistance- Overhead skill'),
		   ('I am passing to an engineer with overhead skills','Assistance- Overhead skill'),
		   ('The work outstanding is Line disconnected on roof','Assistance- Rooftop work'),
		   ('The work outstanding is Cabinet work dslam','Cabinet work required'),
		   ('end customer or their representative was not present at the premises.','Customer unavailable'),
		   ('end customer or their representative is unaware of the order','Customer uninformed'),
		   ("Customer doesn't knock order and no contact details for customer in job","Customer uninformed"),
		   ('the address on the order is incorrect','Incorrect address'),
		   ('The work outstanding is Internal wiring','Internal work required'),
		   ('The work outstanding is PQT from customer socket and internal work','Internal work required'),
		   ('Network issue','Network issue'),
		   ('The work outstanding is Pcp work','Network issue'),
		   ('Work outstanding is a linked fibre task and to push dial tone to end user','Network issue'),
		   ('The work outstanding is Needs pushing through across carrier poles','Network issue'),
		   ('The work outstanding is There is a hr in if network','Network issue'),
		   ('The work outstanding is Nlp requires new d side','Network issue')]

test_corpus = [
		   ('requires pushing through to DP and pushing to PCP, on D3','Network issue'),
		   ('Task Completed Successfully', 'Task Completed Successfully'),
		   ('The work outstanding is Prove pair from the pcp','Network issue'),
		   ('because Hoist were required which could not be obtained on the day','Assistance- Hoist required'),
		   ('The work outstanding is D/w to run by 2 hoists near HV cables pr still to divert but nte5c fitted','Assistance- Hoist required')
               ]

model = NBC(training_corpus) 
accuracy = model.accuracy(test_corpus)


def apply_nlp(data):
    print("in apply nlp method")
    print(data)
    return model.classify(data)
	
def get_accuracy():
    return accuracy
