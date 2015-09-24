import re
def featureExtraction(case):
	common_words = ['is','i','am','a']
	locations = ['ghana','odorkor','kaneshie']
	symptoms = ['headache','pain','chest']
	essential_words = filter(lambda word : word not in common_words,case.split())
	essential_words = set(essential_words)
	essential_words = [ str(x).translate(None,r'[,.]') for x in essential_words ]
	
	features = { 'location':[],'symptoms':[]}
	for word in essential_words:
		if word in locations:
			features['location'].append(word)
		if word in symptoms:
			features['symptoms'].append(word)
	return features

def remedy(case):
	features = featureExtraction(case)
	remedies = {
		'headache':['Dandylon','Pear leaves'],
		'chest':['Dandylon','Cocoa leaves']
	}
	preparations = {
		'Dandylon':'Boil Dandylon leaves',
		'Pear leaves':'Roast and inhale pear leaves'
	}
	remedy = {
		'message':'The ancestors have spoken',
		'herbs':[],
		'preparations':[]
	}
	
	for symptoms in features['symptoms']:
		remedy['herbs']+=remedies.get(symptoms,None)
	remedy['herbs'] = set(remedy['herbs'])
	
	for herb in remedy['herbs']:
		preparation = preparations.get(herb,None)
		if preparation:
			remedy['preparations'].append(preparation) 
	return 	remedy

	