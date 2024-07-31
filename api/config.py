import os
from re import split

""" Required """

BOT_TOKEN = os.environ.get("BOT_TOKEN")
GOOGLE_API_KEY = split(r'[ ,;，；]+', os.environ.get("GOOGLE_API_KEY"))

""" Optional """

ALLOWED_USERS = split(r'[ ,;，；]+', os.getenv("ALLOWED_USERS", '').replace("@", "").lower())
ALLOWED_GROUPS = split(r'[ ,;，；]+', os.getenv("-1002248903144", '').replace("@", "").lower())

# Logları göndermeye ve bazı yönetici komutlarını etkinleştirmeye yönelik ayar
IS_DEBUG_MODE = os.getenv("IS_DEBUG_MODE", '0')

# Yönetici komutlarını çalıştırma yetkisi olan ve log gönderebilen hedef hesap. ID'yi /get_my_info komutuyla alabilirsiniz.
ADMIN_ID = os.getenv("ADMIN_ID", "7132076370")

# Kimlik doğrulamasının yapılıp yapılmayacağını belirler. 0 ise herkes botu kullanabilir. Varsayılan olarak etkinleştirilmiştir.
AUCH_ENABLE = os.getenv("AUCH_ENABLE", "1")

# "1" grup içindeki tüm sohbet geçmişini aynı tutar, "2" her kişi için sohbet geçmişini ayrı ayrı kaydeder
GROUP_MODE = os.getenv("GROUP_MODE", "1")

# 3 tur diyalogdan sonra, kullanıcıyı yeni bir diyalog başlatması için uyarır
prompt_new_threshold = int(3)


# Fotoğrafın eşlik eden metni yoksa varsayılan istem
defaut_photo_caption = "describe this picture"
""" Aşağıda kullanıcı ile ilgili bazı metinler bulunmaktadır """
help_text = "Metin veya resim gönderebilirsiniz. Resim gönderirken lütfen metni aynı mesajda dahil edin.\nGrubu kullanmak için lütfen @bot şeklinde etiketleyin veya bot tarafından gönderilen herhangi bir mesaja yanıt verin."
command_list = "/new Yeni bir sohbet başlat\n/get_my_info Kişisel bilgileri al\n/get_group_info Grup bilgilerini al (sadece grup)\n/get_allowed_users Botu kullanma izni olan kullanıcıların listesini al (sadece yönetici)\n/get_allowed_groups Botu kullanma izni olan grupların listesini al (sadece yönetici)\n/list_models model_listesi (sadece yönetici)\n/get_api_key Gemini'nin apikey'lerini al. Şu anda işe yaramaz. Gelecekte otomatik geçiş için birden fazla anahtar eklenebilir (sadece yönetici)\n/help Yardım al\n/5g_test :)"
admin_auch_info = "Yönetici değilsiniz veya yönetici ID'niz yanlış ayarlanmış!!!"
debug_mode_info = "Hata ayıklama modu etkinleştirilmedi!"
command_format_error_info = "Komut format hatası"
command_invalid_error_info = "Geçersiz komut, yardım için /help kullanın"
user_no_permission_info = "Bu botu kullanma izniniz yok."
group_no_permission_info = "Bu grubun bu botu kullanma izni yok."
gemini_err_info = "Bir şeyler yanlış gitti!\nGirdiğiniz içerik uygunsuz olabilir, lütfen değiştirin ve tekrar deneyin"
new_chat_info = "Yeni bir sohbet başlatıyoruz."
prompt_new_info = "Yeni bir sohbet başlatmak için /new yazın."
unable_to_recognize_content_sent = "Gönderdiğiniz içerik tanınamadı!"

""" Aşağıda günlükle ilgili bazı metinler bulunmaktadır """
send_message_log = "Bir mesaj gönderildi. Döndürülen içerik:"
send_photo_log = "Bir fotoğraf gönderildi. Döndürülen içerik:"
unnamed_user = "AdsızKullanıcı"
unnamed_group = "AdsızGrup"
event_received = "etkinlik alındı"
group = "grup"
the_content_sent_is = "Gönderilen içerik:"
the_reply_content_is = "Yanıt içeriği:"
the_accompanying_message_is = "Eşlik eden mesaj:"
the_logarithm_of_historical_conversations_is = "Tarihi sohbetlerin logaritması:"
no_rights_to_use = "Kullanım hakkı yok"
send_unrecognized_content = "Tanınmayan içerik gönder"



""" https://ai.google.dev/api/rest/v1/GenerationConfig adresini okuyun """
generation_config = {
    "max_output_tokens": 1024,
}

""" https://ai.google.dev/api/rest/v1/HarmCategory adresini okuyun """
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]

