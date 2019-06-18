from urllib.parse import urlparse

#list = ['https://slapcity.org/download/steam', 'https://slapcity1.org/download/official-site',
#		'https://slapcity.org/download/origin', 'https://www.wizard101.com/forum/ravenwood-commons/', 'linking-accounts-8ad6a41b40e8127e01412c04e2a777a3']

domain_uni_list = set()

with open('url.txt', 'r', encoding='utf-8') as file:
	try:
		for i in file:
			parsed_uri = urlparse(i)
			domain = '{uri.netloc}'.format(uri=parsed_uri)
			domain_uni_list.add(domain)
	except Exception:
		 print('An error occured.')

with open('host_result.txt', 'a', encoding='utf-8') as file:
	try:
		for a in domain_uni_list:
			file.write(a + '\n')
	except Exception:
		 print('An error occured.')

print('готовченко')