import urllib.request as req
import json

url = 'https://www.klook.com/v1/experiencesrv/search/vertical_service/activity'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
    'cookie': 'kepler_id=d4043640-8dec-4bb2-8509-b3c2dfae0a02; klk_currency=TWD; klk_rdc=TW; referring_domain_channel=seo; persisted_source=www.google.com; k_tff_ch=google_seo; klk_ps=1; _fwb=241ATw9W9mRPLeZrbtUzZt2.1762656368386; _yjsu_yjad=1762656368.d4081dc5-99d3-436a-81f3-3b8066385461; tr_update_tt=1762656368426; campaign_tag=klc_l1%3DSEO; dable_uid=37047702.1762656367215; __lt__cid=785dfd00-eae5-438b-a8f5-fc77432f65cb; __lt__cid.c83939be=785dfd00-eae5-438b-a8f5-fc77432f65cb; _gcl_au=1.1.2052570430.1762656369; _gid=GA1.2.91803931.1762656369; JSESSIONID=32D5C7203E2E550C5A9EFB2F43F92905; KOUNT_SESSION_ID=32D5C7203E2E550C5A9EFB2F43F92905; _tt_enable_cookie=1; _ttp=01K9K83EFDPZCZXB846HA26BRG_.tt.1; clientside-cookie=7f2d9d482c0dc2ccaf7fa20168b864492065912a211a1a18fd962ee843785a9bd6b6b46b7c66ff60fc2eec836af98d5e4134ee20282fe4894a09bfe9e1fda974b84af81e3eab1bbb1bf3914adfcb85338bce930e843473ba2ed977b21317a6d5c0e45a06e226fe70eec41e0f2ecb04c5340d36fedd2cc57b139280583b6ca6547c6512019ade697005e21591d49ee574562f8af50b85417128c9; traffic_retain=true; _dc_gtm_UA-86696233-1=1; KSID=MQ.930074f7f9f3420473ae1da81bad1aea; __lt__sid=250b672e-62256873; __lt__sid.c83939be=250b672e-62256873; webp_support=1; retina_support=0; CSRF-Token=MTc2MjY1ODc5OXxJNklHRDlBcWVlYVl5SHhCcE41RERtSzM2UlVvNGl2aHyEQqG3zo5_FeGf3DK-yIzlGiu8POi8Gv-GyNppvdgtaQ==; CSRF-Token-Valid=valid; tag_fok=1762658799000; locale=en-us; device_id_new=DpqwU4zEdN00500000000000005B8Gc9qXKS00502715765WpYWiKzBGPJDH3eybWIBix7RX3az8002Th6u90FJYi00000qZkTE00000PrudJXTtQr2Szw7FNSbc:40::45e980508ecc11b1; klk_ga_sn=9394136723..1762658821790; wcs_bt=s_2cb388a4aa34:1762658822; TNAHD=g12_1762658823568; _ga=GA1.1.1134566283.1762656369; _ga_FW3CMDM313=GS2.1.s1762658794$o2$g1$t1762658823$j31$l0$h0; _ga_HSY7KJ18X2=GS2.1.s1762658794$o2$g1$t1762658823$j31$l0$h0; _uetsid=3ee572a0bd1611f09f5ed1a49f47f391; _uetvid=3ee5aac0bd1611f0ab7f5366834880f0; _ga_V8S4KC8ZXR=GS2.1.s1762658794$o2$g1$t1762658825$j29$l0$h360190051; forterToken=bf4decbfbe714996ae8ef1aa1c77d38d_1762658824411__UDF43-m4_21ck_; datadome=3foIHjAGh8B14cVkP2PkCrjmvesEHXpQw~DCv4VVP75t8cMPE29sL~UdrEo9_XB_FGNmLsfPZJ5pIvnvn5vhM5Xy4rifFMCkbpzIUIMryIjuLlDUM43Dqe26ypOtRVkR; klk_i_sn=2217315702..1762658838410; ttcsid=1762658794017::Tqz_DDuwLB7h3jIy5-xc.2.1762658841305.0; ttcsid_C1SIFQUHLSU5AAHCT7H0=1762658794017::V01U-JoFsnhJB1nsCfGp.2.1762658841305.0',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh_TW',
    'content-type': 'application/json',
    'origin': 'https://www.klook.com',
    'priority': 'u=1, i',
    'referer': 'https://www.klook.com/zh-TW/experiences/list/japan-tours/g12-cate9/?spm=Country.Category_LIST&clickId=4fb8369bef'
}

request = req.Request(url, headers=header)

with req.urlopen(request) as res:
    result = res.read()
    print(result)


