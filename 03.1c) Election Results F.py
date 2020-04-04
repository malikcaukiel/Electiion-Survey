# You are a part of an impartial research group that conducts phone surveys prior to local elections.
##### Cynthia Ceballos vs. Justin Kerrigan #####
# Now that the election has occurred, your group wants to compare the survey responses to the actual results.

from matplotlib import pyplot as plt
import numpy as np

survey_responses_arr = np.genfromtxt('election_survey.csv', delimiter=',', dtype= '<U32')
print(survey_responses_arr)

survey_responses = survey_responses_arr.tolist()
print(survey_responses)

#print(survey_responses.count('Ceballos'))
#print(survey_responses.count('Kerrigan'))

# Calculate the number of people who answered ‘Ceballos’
total_ceballos = survey_responses.count('Ceballos') 
print(total_ceballos)

# Calculate the percentage of people in the survey who voted for Ceballos.
total_surveyed = len(survey_responses)
#print(total_surveyed)
percentage_ceballos = total_ceballos / total_surveyed
print(percentage_ceballos)

# Generate a binomial distribution that takes the number of total survey responses, the actual success rate, and the size of the town’s population as its parameters.
possible_surveys = np.random.binomial(total_surveyed, 0.54, size = 10000)
scaled_possible_surveys = np.random.binomial(total_surveyed, 0.54, size = 10000) / total_surveyed

# Plot a histogram of possible_surveys
plt.hist(scaled_possible_surveys, range=(0,1), bins=20)
plt.show()

scaled_possible_surveys_length = len(scaled_possible_surveys)      # = possible_surveys_length
print(scaled_possible_surveys_length)
# Incorrect Predictions of Ceballos winning
incorrect_predictions = len(scaled_possible_surveys[scaled_possible_surveys < 0.5])
# Based on current survey, ceballos loss percentage
ceballos_loss_prediction = incorrect_predictions / scaled_possible_surveys_length
print(ceballos_loss_prediction)

# Generate another binomial distribution, but this time, assume surveyed people were 7,000.
# Now checking accuracy with more respondents
large_possible_surveys_length = 7000
large_possible_surveys = np.random.binomial(large_possible_surveys_length, 0.54, size = 10000)
scaled_large_possible_surveys = large_possible_surveys / large_possible_surveys_length
plt.close()
plt.hist(scaled_possible_surveys, range=(0,1), bins=20)
plt.hist(scaled_large_possible_surveys, range=(0,1), bins=20)
plt.show()

# Now, recalculate the percentage of surveys that would have an outcome of Ceballos losing using the large sample

scaled_large_possible_surveys_length = len(scaled_large_possible_surveys)
print(scaled_large_possible_surveys_length)
incorrect_predictions_new = len(scaled_large_possible_surveys[scaled_large_possible_surveys < 0.5])
ceballos_loss_new = incorrect_predictions_new / scaled_large_possible_surveys_length
print(ceballos_loss_new)    # So chances of incorrect fall to 0

####################################################################################################


