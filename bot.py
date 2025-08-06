import re
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = '7858558354:AAFjrDm5RPYlktT55i89TH6Avopc6OrbTwc'

assignments = {
    "4.1": "https://editor.codeyogi.io/u/58a8f61b2c5f939e4b63d02cf437dd9e/s/4c54256ca6d3bef6851cbf350c37918ffcc029bffca2daa4542b7dedecd1de8d/",
    "6.1": "https://editor.codeyogi.io/u/58a8f61b2c5f939e4b63d02cf437dd9e/s/47138be5888e56590af840189231c39cedb588ab0d5497fae8833884e81a3bce/",
    "7.1": "https://editor.codeyogi.io/u/58a8f61b2c5f939e4b63d02cf437dd9e/s/b3ddfa959259e9642629b625c3dd6846148dd81345c0f06caf2a5ce6e3be2d3a/",
    "8.1": "https://editor.codeyogi.io/u/58a8f61b2c5f939e4b63d02cf437dd9e/s/91d1706c185a0e90f4517cffd8bdf2f3ddf569c868b5e97d176fa6ff87939ab3/",
    "10.1": "https://editor.codeyogi.io/u/58a8f61b2c5f939e4b63d02cf437dd9e/s/b80aed1e6e89df78560f3639b54217780b92a045a2d9e3100b9985daf7fee983/",
    "11.1": "https://editor.codeyogi.io/u/58a8f61b2c5f939e4b63d02cf437dd9e/s/3a7308fb4a58a31ef8f86e41827d0143712ecc3e4e52e68b611917039dc1fdbf/",
    "12.1": "https://editor.codeyogi.io/u/58a8f61b2c5f939e4b63d02cf437dd9e/s/cf75cd4df6450896742748a44933137bf7740a75c377f807609938170a5ac5a2/",
    "14.1": "https://editor.codeyogi.io/u/58a8f61b2c5f939e4b63d02cf437dd9e/s/e811ede5bcd9de584b8bef2a05207eff6bcacecfee00b8808e8cf755014075bb/"
}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type not in ["group", "supergroup"]:
        return

    text = update.message.text
    found = re.findall(r"\b\d+\.\d+\b", text)

    for number in found:
        if number in assignments:
            await update.message.reply_text(f"{number} Solution:\n{assignments[number]}")
            return

logging.basicConfig(level=logging.INFO)
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
app.run_polling()
