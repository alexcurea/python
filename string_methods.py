highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

print(highlighted_poems_list)

highlighted_poems_stripped = []

for n in highlighted_poems_list:
  x = n.strip()
  highlighted_poems_stripped.append(x)

print(highlighted_poems_stripped)

highlighted_poems_details = []

for n in highlighted_poems_stripped:
  x = n.split(':')
  highlighted_poems_details.append(x)

titles = []
poets = []
dates = []

print(highlighted_poems_details)

for n in highlighted_poems_details:
  titles.append(n[0])
  poets.append(n[1])
  dates.append(n[2])

# for title in titles:
#   for poet in poets:
#     for date in dates:
#       print('The poem {title} was published by {poet} in {date}.'.format(title=title, poet=poet, date=date))

for i in range(0, len(highlighted_poems_details)):
   print('The poem {} was published by {} in {}.'.format(titles[i],poets[i],dates[i]))
