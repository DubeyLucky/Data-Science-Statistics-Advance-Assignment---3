#!/usr/bin/env python
# coding: utf-8

# Q1: What is Estimation Statistics? Explain point estimate and interval estimate.

# Estimation statistics is a branch of statistics concerned with making inferences about population parameters based on sample data. It involves using sample statistics to estimate unknown population parameters. Two common approaches to estimation in statistics are point estimation and interval estimation.
# 
# 1. **Point Estimate**:
#    - A point estimate is a single value used to estimate an unknown population parameter. 
#    - It is typically computed from sample data and serves as the best guess or approximation of the true parameter value.
#    - For example, if we are interested in estimating the population mean (\(\mu\)) based on a sample mean (\(\bar{x}\)), then the sample mean (\(\bar{x}\)) serves as the point estimate for the population mean (\(\mu\)).
# 
# 2. **Interval Estimate**:
#    - An interval estimate, also known as a confidence interval, provides a range of plausible values for the unknown population parameter.
#    - It consists of a lower bound and an upper bound, typically computed from sample data along with a specified level of confidence.
#    - The confidence level reflects the probability that the interval estimate contains the true population parameter.
#    - For example, a 95% confidence interval for the population mean (\(\mu\)) would consist of a range of values within which we are 95% confident that the true population mean lies.
# 
# In summary, estimation statistics involves using sample data to estimate unknown population parameters. Point estimates provide single value approximations of the parameters, while interval estimates provide ranges of values that are likely to contain the true parameter value with a specified level of confidence. Both point estimates and interval estimates are important tools in statistical inference for making informed decisions and drawing conclusions about populations based on sample data.

# Q2. Write a Python function to estimate the population mean using a sample mean and standard
# deviation.

# In[1]:


def estimate_population_mean(sample_mean, sample_std_dev, sample_size):
    """
    Estimate the population mean using sample statistics.
    
    Args:
    sample_mean (float): The mean of the sample.
    sample_std_dev (float): The standard deviation of the sample.
    sample_size (int): The size of the sample.
    
    Returns:
    float: Estimated population mean.
    """
    import math
    
    # Calculate the standard error (standard deviation of the sampling distribution of the mean)
    standard_error = sample_std_dev / math.sqrt(sample_size)
    
    # Use the sample mean as the point estimate of the population mean
    population_mean = sample_mean
    
    return population_mean

# Example usage:
sample_mean = 50.0
sample_std_dev = 10.0
sample_size = 100
estimated_population_mean = estimate_population_mean(sample_mean, sample_std_dev, sample_size)
print("Estimated population mean:", estimated_population_mean)


# Q3: What is Hypothesis testing? Why is it used? State the importance of Hypothesis testing.

# Hypothesis testing is a statistical method used to make inferences about a population based on sample data. It involves evaluating two competing hypotheses about a population parameter: the null hypothesis (\(H_0\)) and the alternative hypothesis (\(H_a\) or \(H_1\)). The goal is to assess the evidence provided by the sample data and determine whether there is enough evidence to reject the null hypothesis in favor of the alternative hypothesis.
# 
# The null hypothesis (\(H_0\)) typically represents a default or status quo assumption, while the alternative hypothesis (\(H_a\) or \(H_1\)) represents the claim or effect we are interested in testing. Hypothesis testing involves calculating a test statistic from the sample data and comparing it to a critical value or p-value to make a decision about whether to reject the null hypothesis.
# 
# Hypothesis testing is used for several reasons:
# 
# 1. **Inference about Population Parameters**: Hypothesis testing allows us to make inferences about population parameters based on sample data. For example, we can test hypotheses about population means, proportions, variances, etc.
# 
# 2. **Decision Making**: Hypothesis testing provides a formal framework for making decisions in situations where we want to determine whether a claim or effect is statistically significant. It helps in making informed decisions based on evidence from the data.
# 
# 3. **Validation of Theories and Assumptions**: Hypothesis testing is used to test theories, hypotheses, or assumptions about the population. By subjecting these hypotheses to empirical scrutiny, we can validate or refute them based on the evidence provided by the data.
# 
# 4. **Quality Control and Process Improvement**: In fields such as manufacturing and healthcare, hypothesis testing is used to assess the effectiveness of process improvements or interventions. It helps organizations determine whether changes made to a process have resulted in a significant improvement or not.
# 
# 5. **Scientific Research**: In scientific research, hypothesis testing is a fundamental tool for testing research hypotheses and drawing conclusions about the relationships between variables or the effects of treatments.
# 
# The importance of hypothesis testing lies in its ability to provide a systematic and rigorous approach to decision making based on empirical evidence. It allows researchers, practitioners, and decision-makers to draw reliable conclusions from data, leading to more informed and evidence-based decisions.

# Q4. Create a hypothesis that states whether the average weight of male college students is greater than
# the average weight of female college students.

# Certainly! Here's a hypothesis statement regarding the average weight of male college students compared to female college students:
# 
# **Null Hypothesis (\(H_0\)):** The average weight of male college students is equal to or less than the average weight of female college students.
# 
# **Alternative Hypothesis (\(H_a\) or \(H_1\)):** The average weight of male college students is greater than the average weight of female college students.
# 
# Symbolically:
# 
# \(H_0: \mu_{\text{male}} \leq \mu_{\text{female}}\)
# 
# \(H_a: \mu_{\text{male}} > \mu_{\text{female}}\)
# 
# In words, the null hypothesis suggests that there is no significant difference or that male college students on average weigh the same as or less than female college students. The alternative hypothesis proposes that male college students, on average, weigh more than female college students.
# 
# This hypothesis could be tested using appropriate statistical methods, such as a one-tailed t-test or a confidence interval comparison, using data on the weights of male and female college students sampled from the population of interest.

# Q5. Write a Python script to conduct a hypothesis test on the difference between two population means,
# given a sample from each population.

# In[3]:


import numpy as np
from scipy.stats import ttest_ind

def two_sample_t_test(sample1, sample2, alpha=0.05):
    """
    Perform a two-sample t-test to compare the means of two populations.
    
    Args:
    sample1 (array-like): Sample data from population 1.
    sample2 (array-like): Sample data from population 2.
    alpha (float, optional): Significance level. Default is 0.05.
    
    Returns:
    tuple: t-statistic, p-value
    """
    # Perform the t-test
    t_statistic, p_value = ttest_ind(sample1, sample2, equal_var=False)
    
    # Print the results
    print("T-Statistic:", t_statistic)
    print("P-Value:", p_value)
    
    # Compare p-value with alpha
    if p_value < alpha:
        print("Reject the null hypothesis (H0: μ1 = μ2) in favor of the alternative hypothesis.")
    else:
        print("Fail to reject the null hypothesis (H0: μ1 = μ2).")

# Example usage:
# Generate sample data for two populations
np.random.seed(0)  # For reproducibility
sample1 = np.random.normal(loc=50, scale=10, size=30)  # Sample data from population 1
sample2 = np.random.normal(loc=45, scale=8, size=30)   # Sample data from population 2

# Perform the two-sample t-test
two_sample_t_test(sample1, sample2)


# Q6: What is a null and alternative hypothesis? Give some examples.

# The null hypothesis (\(H_0\)) and alternative hypothesis (\(H_a\) or \(H_1\)) are two complementary statements used in hypothesis testing to make inferences about population parameters based on sample data.
# 
# 1. **Null Hypothesis (\(H_0\))**:
#    - The null hypothesis represents the default or status quo assumption. It suggests that there is no significant difference or effect, or that any observed difference is due to random variation.
#    - In hypothesis testing, the null hypothesis is typically the hypothesis that researchers aim to test or potentially reject.
#    - Symbolically, the null hypothesis is often denoted as \(H_0\).
# 
# 2. **Alternative Hypothesis (\(H_a\) or \(H_1\))**:
#    - The alternative hypothesis represents the claim or effect that researchers are interested in testing. It proposes that there is a significant difference or effect in the population.
#    - The alternative hypothesis can take different forms depending on the nature of the research question, such as one-tailed or two-tailed alternatives.
#    - Symbolically, the alternative hypothesis is often denoted as \(H_a\) or \(H_1\).
# 
# Here are some examples to illustrate the concepts of null and alternative hypotheses:
# 
# 1. **Example 1 (Mean Comparison)**:
#    - Null Hypothesis (\(H_0\)): The mean IQ score of students who followed a traditional teaching method is equal to 100.
#    - Alternative Hypothesis (\(H_a\)): The mean IQ score of students who followed a new teaching method is greater than 100.
# 
# 2. **Example 2 (Proportion Comparison)**:
#    - Null Hypothesis (\(H_0\)): The proportion of voters who support Candidate A is 0.5 (50%).
#    - Alternative Hypothesis (\(H_a\)): The proportion of voters who support Candidate A is different from 0.5 (50%).
# 
# 3. **Example 3 (Equality of Variances)**:
#    - Null Hypothesis (\(H_0\)): The variance of test scores from two different schools is equal.
#    - Alternative Hypothesis (\(H_a\)): The variance of test scores from two different schools is not equal.
# 
# In each example, the null hypothesis states a default assumption or equality, while the alternative hypothesis proposes a specific difference or effect that the researcher is interested in testing. The conclusion about whether to reject the null hypothesis is based on the evidence provided by the sample data and the chosen significance level.

# Q7: Write down the steps involved in hypothesis testing.

# Hypothesis testing is a systematic process used to make inferences about population parameters based on sample data. The following are the general steps involved in hypothesis testing:
# 
# 1. **Formulate Hypotheses**:
#    - Clearly state the null hypothesis (\(H_0\)) and the alternative hypothesis (\(H_a\) or \(H_1\)).
#    - Define the population parameters of interest and the specific claim or effect being tested.
# 
# 2. **Select Significance Level (\(\alpha\))**:
#    - Choose the significance level (\(\alpha\)), which represents the probability of rejecting the null hypothesis when it is actually true.
#    - Common significance levels include 0.05 (5%), 0.01 (1%), or other predetermined values.
# 
# 3. **Select Test Statistic**:
#    - Choose an appropriate test statistic based on the sample data and the hypothesis being tested.
#    - The choice of test statistic depends on factors such as the type of data (e.g., mean, proportion) and the hypothesis being tested.
# 
# 4. **Collect Sample Data**:
#    - Collect data from the population of interest through random sampling or other appropriate methods.
#    - Ensure that the sample size is sufficient to provide reliable results and meet the assumptions of the chosen hypothesis test.
# 
# 5. **Compute Test Statistic**:
#    - Calculate the value of the test statistic using the sample data and the chosen test statistic formula.
#    - The test statistic measures the difference or effect observed in the sample relative to what would be expected under the null hypothesis.
# 
# 6. **Determine Critical Region**:
#    - Determine the critical region or rejection region based on the chosen significance level (\(\alpha\)) and the sampling distribution of the test statistic.
#    - The critical region represents the set of values of the test statistic that would lead to rejection of the null hypothesis.
# 
# 7. **Make Decision**:
#    - Compare the calculated test statistic to the critical value(s) or calculate the p-value associated with the test statistic.
#    - If the test statistic falls within the critical region or the p-value is less than the significance level (\(\alpha\)), reject the null hypothesis.
#    - If the test statistic does not fall within the critical region or the p-value is greater than the significance level, fail to reject the null hypothesis.
# 
# 8. **Draw Conclusion**:
#    - Based on the decision made in step 7, draw a conclusion about the null hypothesis.
#    - If the null hypothesis is rejected, conclude that there is sufficient evidence to support the alternative hypothesis.
#    - If the null hypothesis is not rejected, conclude that there is not enough evidence to support the alternative hypothesis.
# 
# 9. **Interpret Results**:
#    - Interpret the results of the hypothesis test in the context of the research question and the specific hypothesis being tested.
#    - Consider the practical significance of the findings and their implications for decision-making or further research.
# 
# These steps provide a structured approach to hypothesis testing, ensuring that conclusions drawn from sample data are based on sound statistical principles and rigorous reasoning.

# Q8. Define p-value and explain its significance in hypothesis testing.

# The p-value, or probability value, is a measure that quantifies the strength of evidence against the null hypothesis (\(H_0\)) in hypothesis testing. It represents the probability of observing a test statistic as extreme as, or more extreme than, the one computed from the sample data, assuming that the null hypothesis is true.
# 
# In other words, the p-value indicates the likelihood of obtaining the observed results (or more extreme results) if the null hypothesis is correct. A small p-value suggests that the observed results are unlikely to occur under the null hypothesis, providing evidence against it. Conversely, a large p-value suggests that the observed results are more likely to occur by chance, and there is insufficient evidence to reject the null hypothesis.
# 
# The significance of the p-value in hypothesis testing can be summarized as follows:
# 
# 1. **Decision Rule**:
#    - In hypothesis testing, the p-value is compared to the chosen significance level (\(\alpha\)) to make a decision about whether to reject the null hypothesis.
#    - If the p-value is less than or equal to the significance level (\(p \leq \alpha\)), the null hypothesis is rejected.
#    - If the p-value is greater than the significance level (\(p > \alpha\)), the null hypothesis is not rejected.
# 
# 2. **Strength of Evidence**:
#    - The smaller the p-value, the stronger the evidence against the null hypothesis. A small p-value suggests that the observed results are unlikely to occur by random chance alone, providing stronger support for the alternative hypothesis.
#    - Conversely, a large p-value indicates that the observed results are more likely to occur by random chance, leading to a weaker rejection of the null hypothesis.
# 
# 3. **Interpretation**:
#    - The p-value provides a quantitative measure of the significance of the observed results in relation to the null hypothesis.
#    - Researchers can use the p-value to interpret the practical implications of their findings and to draw conclusions about the null hypothesis.
# 
# 4. **Uncertainty**:
#    - It's important to note that the p-value does not provide direct evidence in favor of the alternative hypothesis. Instead, it quantifies the uncertainty associated with the null hypothesis.
#    - A significant result (small p-value) indicates that the observed results are inconsistent with what would be expected under the null hypothesis, but it does not prove the truth of the alternative hypothesis.
# 
# Overall, the p-value plays a critical role in hypothesis testing by providing a standardized measure of the strength of evidence against the null hypothesis. It helps researchers make informed decisions about the validity of their hypotheses based on the observed data.

# Q9. Generate a Student's t-distribution plot using Python's matplotlib library, with the degrees of freedom
# parameter set to 10.

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Define the range of x values
x = np.linspace(-5, 5, 1000)

# Calculate the probability density function (PDF) for the Student's t-distribution
df = 10  # degrees of freedom
pdf = t.pdf(x, df)

# Plot the PDF
plt.plot(x, pdf, label='t-distribution (df=10)')
plt.title("Student's t-distribution (df=10)")
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()


# Q10. Write a Python program to calculate the two-sample t-test for independent samples, given two
# random samples of equal size and a null hypothesis that the population means are equal.

# In[5]:


import numpy as np
from scipy.stats import ttest_ind

def two_sample_t_test(sample1, sample2, alpha=0.05):
    """
    Perform a two-sample t-test for independent samples.
    
    Args:
    sample1 (array-like): Sample data from the first population.
    sample2 (array-like): Sample data from the second population.
    alpha (float, optional): Significance level. Default is 0.05.
    
    Returns:
    tuple: t-statistic, p-value
    """
    # Perform the t-test
    t_statistic, p_value = ttest_ind(sample1, sample2, equal_var=True)
    
    # Print the results
    print("T-Statistic:", t_statistic)
    print("P-Value:", p_value)
    
    # Compare p-value with alpha
    if p_value < alpha:
        print("Reject the null hypothesis (H0: μ1 = μ2) in favor of the alternative hypothesis.")
    else:
        print("Fail to reject the null hypothesis (H0: μ1 = μ2).")

# Generate two random samples of equal size
np.random.seed(0)  # For reproducibility
sample_size = 30
sample1 = np.random.normal(loc=50, scale=10, size=sample_size)  # Sample data from population 1
sample2 = np.random.normal(loc=45, scale=10, size=sample_size)  # Sample data from population 2

# Perform the two-sample t-test
two_sample_t_test(sample1, sample2)


# Q11: What is Student’s t distribution? When to use the t-Distribution.

# Student's t-distribution, often referred to simply as the t-distribution, is a probability distribution that is symmetric and bell-shaped, similar to the normal distribution. It is used primarily in inferential statistics to make inferences about population parameters when the sample size is small or when the population standard deviation is unknown.
# 
# The t-distribution is characterized by a single parameter, known as the degrees of freedom (\(df\)). The shape of the t-distribution depends on the degrees of freedom, with larger degrees of freedom leading to distributions that closely resemble the standard normal distribution (Z-distribution).
# 
# Here are some key points about the t-distribution and when to use it:
# 
# 1. **Characteristics**:
#    - The t-distribution is symmetric and bell-shaped, like the normal distribution.
#    - As the degrees of freedom increase, the t-distribution approaches the standard normal distribution (Z-distribution).
#    - The mean of the t-distribution is typically zero, and its variance depends on the degrees of freedom.
# 
# 2. **When to Use**:
#    - **Small Sample Sizes**: The t-distribution is especially useful when dealing with small sample sizes (typically n < 30) where the population standard deviation is unknown.
#    - **Unknown Population Standard Deviation**: When the population standard deviation is unknown and must be estimated from the sample data, the t-distribution is used instead of the normal distribution.
#    - **Estimation and Inference**: The t-distribution is commonly used in hypothesis testing and confidence interval estimation for population means when dealing with small samples.
# 
# 3. **Applications**:
#    - **Comparing Means**: When comparing means of two independent samples or performing a one-sample t-test to compare a sample mean to a known or hypothesized population mean.
#    - **Estimating Confidence Intervals**: When estimating confidence intervals for population means or differences in means.
# 
# 4. **Robustness**:
#    - The t-distribution is more robust than the normal distribution when dealing with outliers or non-normal data, especially with small sample sizes.
#    - It provides more accurate inference when the assumptions of normality and equal variances are not fully met.
# 
# In summary, the t-distribution is a key statistical tool used in situations where the population standard deviation is unknown and the sample size is small. It provides a more accurate and reliable framework for making inferences about population parameters in such scenarios, particularly in hypothesis testing and confidence interval estimation.

# Q12: What is t-statistic? State the formula for t-statistic.

# The t-statistic is a measure that quantifies the difference between the sample statistic (such as the sample mean) and the population parameter (such as the population mean), relative to the variability observed in the sample data. It is used primarily in hypothesis testing to assess whether the observed difference is statistically significant.
# 
# The formula for the t-statistic depends on the specific context and hypothesis being tested. However, the general formula for the t-statistic when comparing a sample mean to a population mean (or comparing two sample means) is as follows:
# 
# \[ t = \frac{\bar{x} - \mu}{\frac{s}{\sqrt{n}}} \]
# 
# Where:
# - \( \bar{x} \) is the sample mean.
# - \( \mu \) is the population mean (or the hypothesized population mean under the null hypothesis).
# - \( s \) is the sample standard deviation.
# - \( n \) is the sample size.
# 
# This formula calculates the difference between the sample mean (\( \bar{x} \)) and the population mean (\( \mu \)), expressed in terms of the standard error of the sample mean (\( \frac{s}{\sqrt{n}} \)). The standard error reflects the variability in sample means that would be expected under repeated sampling from the population.
# 
# The t-statistic measures how many standard errors the sample mean is away from the population mean. A larger absolute value of the t-statistic indicates a greater difference between the sample mean and the population mean, relative to the variability observed in the sample data.
# 
# In hypothesis testing, the t-statistic is compared to a critical value from the t-distribution or used to calculate a p-value, which helps determine whether to reject the null hypothesis in favor of the alternative hypothesis. If the absolute value of the t-statistic is large enough (i.e., exceeds the critical value or results in a small p-value), the difference between the sample mean and the population mean is considered statistically significant, leading to rejection of the null hypothesis.

# Q13. A coffee shop owner wants to estimate the average daily revenue for their shop. They take a random
# sample of 50 days and find the sample mean revenue to be $500 with a standard deviation of $50.
# Estimate the population mean revenue with a 95% confidence interval.

# To estimate the population mean revenue with a 95% confidence interval, we can use the formula for the confidence interval for the population mean when the population standard deviation is unknown. The formula is:
# 
# \[ \text{Confidence Interval} = \bar{x} \pm t \times \frac{s}{\sqrt{n}} \]
# 
# Where:
# - \( \bar{x} \) is the sample mean.
# - \( s \) is the sample standard deviation.
# - \( n \) is the sample size.
# - \( t \) is the critical value from the t-distribution for the desired confidence level and degrees of freedom.
# 
# Given:
# - Sample mean (\( \bar{x} \)) = $500
# - Sample standard deviation (\( s \)) = $50
# - Sample size (\( n \)) = 50
# - Confidence level = 95%
# 
# We need to find the critical value \( t \) for a 95% confidence level with \( n - 1 \) degrees of freedom (where \( n \) is the sample size). Then we can plug in the values into the formula to calculate the confidence interval.
# 
# Let's calculate it step by step:
# 
# 1. **Find the Critical Value \( t \)**:
#    - We need to find the critical value from the t-distribution for a 95% confidence level and \( n - 1 = 50 - 1 = 49 \) degrees of freedom.
#    - We can find this using statistical software or a t-distribution table. For a 95% confidence level and 49 degrees of freedom, \( t \) is approximately 2.0096.
# 
# 2. **Calculate the Confidence Interval**:
#    - \( \text{Confidence Interval} = 500 \pm 2.0096 \times \frac{50}{\sqrt{50}} \)
# 
# Let's calculate the confidence interval:
# 
# \[ \text{Confidence Interval} = 500 \pm 2.0096 \times \frac{50}{\sqrt{50}} \]
# 
# \[ \text{Confidence Interval} = 500 \pm 2.0096 \times \frac{50}{\sqrt{50}} \]
# 
# \[ \text{Confidence Interval} = 500 \pm 14.234 \]
# 
# So, the 95% confidence interval for the population mean revenue is approximately \( \$500 \pm \$14.234 \), or from approximately \$485.766 to \$514.234.

# Q14. A researcher hypothesizes that a new drug will decrease blood pressure by 10 mmHg. They conduct a
# clinical trial with 100 patients and find that the sample mean decrease in blood pressure is 8 mmHg with a
# standard deviation of 3 mmHg. Test the hypothesis with a significance level of 0.05.

# To test the hypothesis that the new drug decreases blood pressure by 10 mmHg, we can perform a one-sample t-test. The null and alternative hypotheses are as follows:
# 
# - Null Hypothesis (\(H_0\)): The mean decrease in blood pressure (\( \mu \)) is equal to 10 mmHg.
# - Alternative Hypothesis (\(H_a\)): The mean decrease in blood pressure (\( \mu \)) is less than 10 mmHg.
# 
# Given:
# - Sample mean (\( \bar{x} \)) = 8 mmHg
# - Sample standard deviation (\( s \)) = 3 mmHg
# - Sample size (\( n \)) = 100
# - Significance level (\( \alpha \)) = 0.05
# 
# We can calculate the t-statistic using the formula:
# 
# \[ t = \frac{\bar{x} - \mu_0}{\frac{s}{\sqrt{n}}} \]
# 
# where \( \mu_0 \) is the hypothesized population mean under the null hypothesis.
# 
# Then, we compare the calculated t-statistic to the critical value from the t-distribution with \( n - 1 \) degrees of freedom (99 degrees of freedom in this case) at the chosen significance level (\( \alpha = 0.05 \)).
# 
# If the calculated t-statistic falls in the critical region (i.e., if \( t < -t_{\alpha, df} \)), we reject the null hypothesis in favor of the alternative hypothesis.
# 
# Let's perform the calculation:
# 
# \[ t = \frac{8 - 10}{\frac{3}{\sqrt{100}}} \]
# \[ t = \frac{-2}{0.3} \]
# \[ t = -6.67 \]
# 
# We can look up the critical value for a one-tailed test with 99 degrees of freedom and a significance level of 0.05. From a t-distribution table or using statistical software, the critical value is approximately -1.660.
# 
# Since \( t = -6.67 < -1.660 \), we reject the null hypothesis.
# 
# Therefore, we have sufficient evidence to conclude that the new drug decreases blood pressure by less than 10 mmHg, with a significance level of 0.05.

# Q15. An electronics company produces a certain type of product with a mean weight of 5 pounds and a
# standard deviation of 0.5 pounds. A random sample of 25 products is taken, and the sample mean weight
# is found to be 4.8 pounds. Test the hypothesis that the true mean weight of the products is less than 5
# pounds with a significance level of 0.01.

# To test the hypothesis that the true mean weight of the products is less than 5 pounds, we can perform a one-sample t-test. The null and alternative hypotheses are as follows:
# 
# - Null Hypothesis (\(H_0\)): The mean weight of the products (\( \mu \)) is equal to 5 pounds.
# - Alternative Hypothesis (\(H_a\)): The mean weight of the products (\( \mu \)) is less than 5 pounds.
# 
# Given:
# - Population mean (\( \mu \)) = 5 pounds
# - Population standard deviation (\( \sigma \)) = 0.5 pounds
# - Sample mean (\( \bar{x} \)) = 4.8 pounds
# - Sample size (\( n \)) = 25
# - Significance level (\( \alpha \)) = 0.01
# 
# We can calculate the t-statistic using the formula:
# 
# \[ t = \frac{\bar{x} - \mu}{\frac{\sigma}{\sqrt{n}}} \]
# 
# Then, we compare the calculated t-statistic to the critical value from the t-distribution with \( n - 1 \) degrees of freedom (24 degrees of freedom in this case) at the chosen significance level (\( \alpha = 0.01 \)).
# 
# If the calculated t-statistic falls in the critical region (i.e., if \( t < -t_{\alpha, df} \)), we reject the null hypothesis in favor of the alternative hypothesis.
# 
# Let's perform the calculation:
# 
# \[ t = \frac{4.8 - 5}{\frac{0.5}{\sqrt{25}}} \]
# \[ t = \frac{-0.2}{0.1} \]
# \[ t = -2 \]
# 
# We can look up the critical value for a one-tailed test with 24 degrees of freedom and a significance level of 0.01. From a t-distribution table or using statistical software, the critical value is approximately -2.492.
# 
# Since \( t = -2 > -2.492 \), we fail to reject the null hypothesis.
# 
# Therefore, we do not have sufficient evidence to conclude that the true mean weight of the products is less than 5 pounds, with a significance level of 0.01.

# Q16. Two groups of students are given different study materials to prepare for a test. The first group (n1 =
# 30) has a mean score of 80 with a standard deviation of 10, and the second group (n2 = 40) has a mean
# score of 75 with a standard deviation of 8. Test the hypothesis that the population means for the two
# groups are equal with a significance level of 0.01.

# To test the hypothesis that the population means for the two groups are equal, we can perform a two-sample t-test for independent samples. The null and alternative hypotheses are as follows:
# 
# - Null Hypothesis (\(H_0\)): The population means for the two groups are equal (\( \mu_1 = \mu_2 \)).
# - Alternative Hypothesis (\(H_a\)): The population means for the two groups are not equal (\( \mu_1 \neq \mu_2 \)).
# 
# Given:
# For Group 1:
# - Sample size (\(n_1\)) = 30
# - Sample mean (\(\bar{x}_1\)) = 80
# - Sample standard deviation (\(s_1\)) = 10
# 
# For Group 2:
# - Sample size (\(n_2\)) = 40
# - Sample mean (\(\bar{x}_2\)) = 75
# - Sample standard deviation (\(s_2\)) = 8
# 
# Significance level (\( \alpha \)) = 0.01
# 
# We can calculate the t-statistic for the two-sample t-test using the formula:
# 
# \[ t = \frac{(\bar{x}_1 - \bar{x}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} \]
# 
# Then, we compare the absolute value of the calculated t-statistic to the critical value from the t-distribution with degrees of freedom determined by the Welch-Satterthwaite equation, and at the chosen significance level (\( \alpha = 0.01 \)).
# 
# If the absolute value of the calculated t-statistic exceeds the critical value, we reject the null hypothesis in favor of the alternative hypothesis.
# 
# Let's perform the calculation:
# 
# \[ t = \frac{(80 - 75) - (0)}{\sqrt{\frac{10^2}{30} + \frac{8^2}{40}}} \]
# \[ t = \frac{5 - 0}{\sqrt{\frac{100}{30} + \frac{64}{40}}} \]
# \[ t = \frac{5}{\sqrt{3.333 + 1.6}} \]
# \[ t ≈ \frac{5}{\sqrt{4.933}} \]
# \[ t ≈ \frac{5}{2.221} \]
# \[ t ≈ 2.252 \]
# 
# The critical value for a two-tailed test with 30 and 40 degrees of freedom and a significance level of 0.01 is approximately 2.660 (obtained from a t-distribution table or using statistical software).
# 
# Since \( |t| = 2.252 < 2.660 \), we fail to reject the null hypothesis.
# 
# Therefore, we do not have sufficient evidence to conclude that the population means for the two groups are different, with a significance level of 0.01.

# Q17. A marketing company wants to estimate the average number of ads watched by viewers during a TV
# program. They take a random sample of 50 viewers and find that the sample mean is 4 with a standard
# deviation of 1.5. Estimate the population mean with a 99% confidence interval.

# In[ ]:




