import datetime as datetime
import os 

def main(committer_path):
	if not os.path.exists(committer_path + 'committer-per-month'):
		os.makedirs(committer_path + 'committer-per-month')
	committer_per_month_path = committer_path + 'committer-per-month/'
	for file in os.listdir(committer_path): 
		if file.endswith('.txt'):
			f = open(os.path.join(committer_path,file))
			data = f.readlines()
			committer_date_list = parse_committer_file(data)		
			write_monthly_amount_file(committer_date_list,committer_per_month_path,file)
				
def parse_committer_file(data):
	committer_date_list = []
	
	for line in data:
		committer_value = line.split('-')
		if (len(committer_value) > 1):
		  committer_date = datetime.datetime(int(committer_value[0]),int(committer_value[1]),int(committer_value[2]))
		  committer_date_list.append(committer_date)
		
	return committer_date_list
	
	
def write_monthly_amount_file(committer_date_list,committer_per_month_path,file_name):
	monthly_amount_file_path = committer_per_month_path + (file_name).replace('.txt','-committer.txt')
	monthly_amount_file = open(monthly_amount_file_path,'w')
	year_list = []
	for date in committer_date_list: 
		if date.year not in year_list:
			year_list.append(date.year)
			
	year_sublists = [[list() for month in range(12)] for year in range(len(year_list))] 
	for current_year,current_year_sublist in zip(year_list,year_sublists):
		for current_month,month in zip(range(1,13),current_year_sublist): 
			for date in committer_date_list:
				if date.year == current_year:
					if date.month == current_month:
						month.append(date.day) 

	for current_year,current_sublist in zip(year_list,year_sublists):
		monthly_amount_file.write(str(current_year))
		monthly_amount_file.write('\n')	
		for current_month,month in zip(range(1,13),current_sublist):
			monthly_amount_file.write(str(current_month) + '-' + str(len(month)))  
			monthly_amount_file.write('\n')
			
if __name__ == "__main__":	
	committer_path = raw_input('Specify committer date files path: \n(Example: /home/user/documents/committer/)\n')
	main(committer_path)
