# Pandas Series and DataFrame
import pandas as pd
marks = pd.Series([85, 91, 78, 88, 95],
index=[&quot;A&quot;, &quot;B&quot;, &quot;C&quot;, &quot;D&quot;, &quot;E&quot;])
print(&quot;--- Pandas Series ---&quot;)
print(marks)
data = {
quot;RollNo&quot: [101, 102, 103, 104, 105],
&quot;Name&quot;: [&quot;Anitha&quot;, &quot;Bala&quot;, &quot;Chitra&quot;, &quot;Dinesh&quot;, &quot;Ezhil&quot;],
&quot;Department&quot;: [&quot;CSE&quot;, &quot;CSE&quot;, &quot;ECE&quot;, &quot;CSE&quot;, &quot;ECE&quot;],
&quot;Mark&quot;: [85, 91, 78, 88, 95]
}
df = pd.DataFrame(data)
print(&quot;\n--- DataFrame ---&quot;)
print(df)
print(&quot;\nAverage Mark:&quot;, round(df[&quot;Mark&quot;].mean(), 2))
print(&quot;\nStudents scoring above 85:&quot;)
print(df[df[&quot;Mark&quot;] &gt; 85])