from requests_html import HTMLSession
session = HTMLSession()
response = session.get('https://www.imdb.com/movies-coming-soon/2018-08/?ref_=cs_dt_nx')
elements = response.html.find('.txt-block [href="/name/nm0950775/?ref_=cs_ov_nm"]')
for element in elements:
    print(element.text)


# #進階_印演員
# elements_actor = response.html.find('.overview-top [temprop="name"] [href="/title/tt4073790/?ref_=cs_ov_tt"]>.txt-block [itemprop="actors"]')
# for element in elements_actor:
#     print(element.text)