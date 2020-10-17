# display menu
# get input, validate it
# run user's selection
# when user selects, average price
def load_file(filename):
  f = open(filename, 'r')
  # do something with f
  # MM-DD-YYYY:<float>
  fileContents= []
  for line in f:
    fileContents.append(line.rstrip())
  f.close()
  return fileContents

# mm-dd-yyyy:float

def convertFile(str_data):
  data = []
  for line in str_data:
    dateStr, priceStr = line.split(':')
    price = float(priceStr)
    month, day, year = dateStr.split("-")
    month, day, year = int(month), int(day), int(year)
    rec = [month, day, year, price]
    data.append(rec)
  return data

def sort_key(rec):## find out how use key parameter
    return rec[3]

def sort_asc(data):
    asc_data = data + []
    asc_data.sort(key = sort_key)
    for rec in asc_data:
        print(display_rec(rec))

def get_input():
  menu = """
  1. Avg per year
  2. Avg per Month
  3. Highest and lowest per year
  4. Low to high prices (Makes a file)
  5. High to low prices (Makes a file)
  6. Exit
"""
  print(menu)
  still_choosing = True
  while still_choosing:
    choice = input('>> ')
    try:
      int_choice = int(choice)
    except ValueError as err:
      print('Please enter an integer value')
    else:
      if not 0 < int_choice < 7:
        print('Please select a value between 1 and 6')
      else:
        still_choosing = False

  return int_choice

def avg_per_year(data):
    #[[month, day, year, price]]
    #[year, year2]
    #[sum of prices of year, sum of prices of year 2]
    #[count of prices of year one, count of prices of year2 ]
    years = []
    totals = []
    counts = []
    for rec in data:
        month = rec[0]
        day = rec[1]
        year = rec[2]
        price = rec[3]

        if year not in years:
            years.append(year)
            totals.append(0)
            counts.append(0)

        index = years.index(year)
        totals[index] += price
        counts[index] += 1

    for i in range(len(years)):
        print(years[i], '$' + format(totals[i]/counts[i], '.2f'))


def display_rec(rec):
    output = str(rec[0])+ '-' + str(rec[1])+'-'+str(rec[2])+":"+str(rec[3])
    return output

def year_hi_low(data):
    years = []
    hi = []
    low = []

    for rec in data:
        month = rec[0]
        day = rec[1]
        year = rec[2]
        price = rec[3]
        if year not in years:
            years.append(year)
            hi.append(rec)
            low.append(rec)
        else:
            index = years.index(year)
            if price > hi[index][3]:
                hi[index] = rec
            if price < low[index][3]:
                low[index] = rec
    for i in range(len(years)):
        print(years[i])
        print('  low:', display_rec(low[i]))

        print('  high:', display_rec(hi[i]))



def run_selection(selection, data):
  if selection == 1:
    avg_per_year(data)

  elif selection == 2:
    print('avg_per_month(data)')

  elif selection == 3:
    year_hi_low(data)

  elif selection == 4:
    sort_asc(data)

  elif selection == 5:
    print('sort_desc(data)')

def main():
  #1. read file into memory 
  str_data = load_file('GasPrices.txt')
  # now do other stuff
  #print(str_data)
  #1.b convert strings into data  
  data = convertFile(str_data)
  keep_going = True
  while keep_going:
    selection = get_input()
    if selection == 6:
      break
    run_selection(selection, data)


#https://repl.it/@YufengGuo/CIIC3015liveexercise1#main.py
main()