# import nltk
# nltk.download('punkt')

text = '''
The koala feeds very selectively on the leaves of certain eucalyptus trees. Generally solitary, individuals move within a home range of more than a dozen trees, one of which is favoured over the others. If koalas become too numerous in a restricted area, they defoliate preferred food trees and, unable to subsist on even closely related species, decline rapidly. To aid in digesting as much as 1.3 kg (3 pounds) of leaves daily, the koala has an intestinal pouch (cecum) about 2 metres (7 feet) long, where symbiotic bacteria degrade the tannins and other toxic and complex substances abundant in eucalyptus. This diet is relatively poor in nutrients and provides the koala little spare energy, so the animal spends long hours simply sitting or sleeping in tree forks, exposed to the elements but insulated by thick fur. Although placid most of the time, koalas produce loud, hollow grunts.
'''

from quizbot.ml_models.sense2vec_distractor_generation.sense2vec_generation import Sense2VecDistractorGeneration

sense2vec_distractor_generator = Sense2VecDistractorGeneration()
distractors = sense2vec_distractor_generator.generate("symbiotic_bacteria", 3)
print(distractors)