import datetime as datetime
import os 

def organize_monthly(issue_path):
	opened_per_month_path = issue_path + 'opened-per-month/'
	closed_per_month_path = issue_path + 'closed-per-month/'
	
	if not os.path.exists(closed_per_month_path):
		os.makedirs(closed_per_month_path)

	if not os.path.exists(opened_per_month_path):
		os.makedirs(opened_per_month_path)
				
	for file in os.listdir(issue_path):
		if file.endswith('.txt'):
			f = open(os.path.join(issue_path,file))
			file_name = file.split('-')[0]
			data = f.readlines()[1:]
			opened,closed = collect_issues(data)
			# write_file(opened,'opened',opened_per_month_path,file_name,issue_path)	
			# write_file(closed,'closed',closed_per_month_path,file_name,issue_path)
	
def collect_issues(data):
	opened = []
	closed = []
		
	for line in data:
		line = line.strip()
		issue_data = line.split(',') 
		open_date = issue_data[4]
		print open_date
		raw_input()
		
		"""		
		opened_values = (line_values[4]).split('/') 
		opened_date = datetime.datetime(int(opened_values[2]),int(opened_values[1]),int(opened_values[0]))
		opened.append(opened_date)
		
		if len(line_values[5]) > 12: 
			closed_date_list = (line_values[5])[1:-1] 
			closed_date_list = closed_date_list.split('-') 
			for date in closed_date_list:
				closed_value = date.strip().split('/')
				closed_date = datetime.datetime(int(closed_value[2]),int(closed_value[1]),int(closed_value[0]))
				closed.append(closed_date)
				
		else:
			if line_values[5] != 'Null' and len(line_values[5]) > 2: 
				closed_value = (line_values[5])[1:-1].split('/')
				closed_date = datetime.datetime(int(closed_value[2]),int(closed_value[1]),int(closed_value[0]))
				closed.append(closed_date)
				
	return opened,closed	
"""
def write_file(data,data_type,data_folder,file_name,issue_path):
	new_file_path = os.path.join(data_folder + file_name + '-' + data_type + '.txt') 
	new_file = open(new_file_path,'w')
	year_list = []
	
	for date in data: 
		if date.year not in year_list:
			year_list.append(date.year)
			
	year_sublists = [[list() for month in range(12)] for year in range(len(year_list))] 
	
	for current_year,current_year_sublist in zip(year_list,year_sublists):
		for current_month,month in zip(range(1,13),current_year_sublist): 
			for date in data:
				if date.year == current_year:
					if date.month == current_month:
						month.append(date.day) 

	for current_year,current_sublist in zip(year_list,year_sublists):
		new_file.write(str(current_year))
		new_file.write('\n')
		
		for current_month,month in zip(range(1,13),current_sublist):
			new_file.write(str(current_month) + '-' + str(len(month)))  
			new_file.write('\n')

if __name__ == "__main__":
	issue_path = raw_input('Specify issue files path: \n')
	organize_monthly(issue_path)

				
		
