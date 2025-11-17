days=1000
years=days//365
remain_days=days%365
weeks=remain_days//7
days_left=remain_days%7
print(years, weeks, days_left)