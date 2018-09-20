
# coding: utf-8

# In[1]:


# Blood glucose levels for obese patients have a mean of 100 with a standard deviation of 15. A researcher thinks that a diet high in raw cornstarch will have a positive effect on blood glucose levels. A sample of 36 patients who have tried the raw cornstarch diet have a mean glucose level of 108. Test the hypothesis that the raw cornstarch had an effect or not.


# In[2]:


import math

no_of_sample = 36
sample_mean = 108
population_mean = 100
population_sigma = 15

# Step-1: State the hypothesis. The population mean is 100.
# H0:µ=100 ==> null hypothesis
# H1:≠100 ==> Research hypothesis / Alternate hypothesis

# Step-2: Set up the significance level. It is not given in the problem so let's assume it as 5% (0.05).

# This 5% is called Significance Level also known as alpha level (symbolized as α).
# It means that if random chance probability is less than 5% then we can conclude that there is difference in behaviour of 
# two different population.
# (1 - significance level) is also known as Confidence level
# i.e. we can say that iam 95% confident that it is not driven by randomness.

# Step-3: Calculate Z score
z = (sample_mean - population_mean) / (population_sigma / math.sqrt(no_of_sample))
print("Z score :",z)

# By looking at z-table and p-value associated with 3.20 is 0.9993
# The probability of having value less than 108 is 0.9993 and more than or equals to 108 is (1-0.9993)=0.0007.

# Step-4: Since the probability of having mean glucose level more than or equals to 108 is 0.0007 which is less than 0.05.
# So we will reject the Null hypothesis i.e. there is raw cornstarch  effect.


# In[3]:


# In one state, 52% of the voters are Republicans, and 48% are Democrats. In a second state, 47% of the voters are Republicans, and 53% are Democrats. Suppose a simple random sample of 100 voters are surveyed from each state. What is the probability that the survey will show a greater percentage of Republican voters in the second state than in the first state?


# In[5]:


# Let:

#P1 = The proportion of Republican Voters in the first state
#P2 = The proportion of Republican Voters in the second state
#p1 = The proportion of Republican Voters in the sample from the first state
#p2 = The proportion of Republican Voters in the sample from the second state

# The number of Voters sampled from the first state (n1) = 100
n1 = 100

# The number of Voters sampled from the second state (n2) = 100
n2 = 100

P1 = 0.52
#(1 - P1) = Q1
Q1 = 0.48
P2 = 0.47
#(1 - P2) = Q2
Q2 = 0.53

# The mean of the difference in sample proportions .i.e Expected Value E[p1 -p2] = P1 - P2 = mu 
mu = P1 - P2

# The standard deviation of the difference (std)
std = math.sqrt(((P1 * Q1) / n1) + ((P2 * Q2) / n2))
print("Mu : ",mu,"Std : ", std)

# This problem requires us to find the probability that p1 is less than p2.
# This is eqivalent to finding the probability that p1 - p2 < 0.
x = 0
# To find this probability, we need to transform the random variable (p1 - p2) into a z-score. That transformation appears below:
Z_p1_p2 = (x - mu) / std

print("Z_score(p1,p2) : ", Z_p1_p2)

# From Z table we find that the probability of a z-score being -0.7082 or less is 0.24.

# Therefore, the probability that the survey will show a greater percentage of Republican Voters in the second state than
# in the first state is 0.24.
        


# In[6]:


# You take the SAT and score 1100. The mean score for the SAT is 1026 and the standard deviation is 209. How well did you score on the test compared to the average test taker?


# In[7]:


# The z score tells you how many standard deviations from the mean your score is
x = 1100
mu = 1026 # Population Mean
sd = 209 # population standard deviation
z = (x - mu) / sd
print("Z Score : ", z)
# The above calculation shows that my score is 0.35 standard deviations above the mean
print("My score is in the range {} - {} with a zscore {:.2f}".format(mu - sd, mu + sd, z))

