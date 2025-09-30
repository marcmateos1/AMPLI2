from scipy import stats

esperanza=10
desviacio=500
a=10
b=20

X=stats.norm(esperanza,desviacio)
p=X.cdf(b)-X.cdf(a)
print(p)