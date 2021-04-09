#编写程序，实现如下功能：
# – 用户输入国家名称
# – 打印出所输入国家名称及其首都

nations = {'China': 'Beijing', 'Japan': 'Tokyo', 'India': 'New Delhi', 'Sweden': 'Stockholm', 'Russian': 'Moscow', 'Germany': 'Berlin', 'UK': 'London', 'French': 'Paris', 'Swiss': 'Bern', 'Egypt':'Cairo', 'Australia': 'Canberra', 'New Zealand': 'Wellington', 'Canada': 'Ottawa', 'USA': 'Washington', 'Cuba': 'Havana', 'Brazil': 'Brasilia'}
country = input('input the name of country：')
capital = nations.get(country)

print('the country is:', country)
print('the capital is:', capital)
