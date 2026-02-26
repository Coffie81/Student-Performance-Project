import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_100 2.csv")


#Hardest score
subject_avgs = df[['math_score', 'reading_score', 'writing_score']].mean()
print(subject_avgs)

hardest_subject = subject_avgs.idxmin()
hardest_score = subject_avgs.min()

print("Hardest Subject:", hardest_subject, " with Average Score:", hardest_score)


#The 5 top performing Students
df['average_score'] = df[['math_score', 'reading_score', 'writing_score']].mean(axis=1)

top_students = df.sort_values(by='average_score', ascending=False).head(5)
print(top_students[['gender','student_id', 'average_score']])


#Comparing Performance by Gender
gender_comparison = df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean()
print(gender_comparison)


#Visualization (Showing the Average Scores for each subject)
plt.figure()
subject_avgs.plot(kind='bar')
plt.title("Average Score per Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.show()


#Visualization(Gender Performance)
plt.figure() 
gender_comparison.plot(kind='bar')
plt.title("Average Scores by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.show()
