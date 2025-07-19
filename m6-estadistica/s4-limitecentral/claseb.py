from scipy import stats

# probabilidad valor menor o igual a 8 (probabilidad acumulada)
# distribucion normal media 10 desviacion std 2
prob=stats.norm.cdf(8,loc=10,scale=2)
print(prob)