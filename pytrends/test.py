from request import TrendReq
import pandas as pd



pytrend = TrendReq()

htd='20180827'
sheet_number=1

writer = pd.ExcelWriter('20180827_kr.xlsx')

for i in range(10):
	sheet='Sheet'+ str(sheet_number)
	trending_searches_df = pytrend.trending_searches(htd=htd)
	trending_searches_df.to_excel(writer, sheet)
	htd_int = int(htd) - 2
	print(htd_int)
	htd = str(htd_int)
	sheet_number += 1
	print(sheet_number)


writer.save()

