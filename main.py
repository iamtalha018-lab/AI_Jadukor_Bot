import telebot
import requests
import os

# আপনার টোকেনটি এখানে সরাসরি বসিয়ে দিচ্ছি যাতে কোনো ভুল না হয়
API_TOKEN = '8571253841:AAF-qalGQB6bzohp4dgla7ysVFkFGarn1fc'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "স্বাগতম! আমি এআই জাদুকর। ✨\n\n"
        "ছবি তৈরি করতে লিখুন `/draw` এরপর ইংরেজিতে বর্ণনা দিন।\n"
        "উদাহরণ: `/draw a futuristic city in Bangladesh`"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['draw'])
def generate_image(message):
    # কমান্ডের পরের অংশটুকু (প্রম্পট) আলাদা করা
    prompt = message.text.replace('/draw', '').strip()
    
    if not prompt:
        bot.reply_to(message, "দয়া করে ছবির একটি বর্ণনা দিন। যেমন: `/draw a cat with a hat`")
        return

    bot.reply_to(message, "আপনার ছবি জাদুকরী শক্তিতে তৈরি হচ্ছে... দয়া করে ১০-১৫ সেকেন্ড অপেক্ষা করুন। 🪄")
    
    # Pollinations AI API ব্যবহার করে ছবি জেনারেট
    image_url = f"https://pollinations.ai{prompt.replace(' ', '%20')}?width=1024&height=1024&nologo=true"
    
    try:
        # ব্যবহারকারীকে ছবি পাঠানো
        bot.send_photo(message.chat.id, image_url, caption=f"আপনার ছবি: {prompt}")
    except Exception as e:
        bot.reply_to(message, "দুঃখিত, ছবি তৈরি করতে সমস্যা হয়েছে। আবার চেষ্টা করুন।")

if __name__ == "__main__":
    print("বট সচল আছে...")
    bot.polling(none_stop=True)
