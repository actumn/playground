import pandas as pd

test_data = pd.read_csv('data/test.csv', delimiter='\t')
test_data_url = test_data.url
test_data_ctr = test_data.ctr

# print(pd.concat(test_data_url, test_data_ctr))

print(test_data.url.astype(str).values.tolist())
print(test_data.ctr.astype(float).values.tolist())

result = '[\'{"aaa":{"score":"0.5523"}, "bbb":{"score":"0.1231"}, "ccc":{"score":"0.2313"}, "ddd":{"score":"0.1241"}}\']'
result = eval(result)
result = eval(result[0])
print(result)
print(result['aaa']['score'])

result = pd.DataFrame.from_dict(result, orient='index', columns=['score']).reset_index(col_fill='url')
result.columns = ['url', 'score']
print(result)

result = pd.DataFrame.merge(result, test_data)
print(result)

result.to_csv('data/test_result.csv', index=False, sep='\t')
