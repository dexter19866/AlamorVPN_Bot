# utils/messages.py (نسخه نهایی، کامل و حرفه‌ای)

# =============================================================================
# SECTION: پیام‌های عمومی و سیستمی
# =============================================================================
START_WELCOME = "🤖 به ربات serverusaa_bot خوش آمدید، {first_name} عزیز!\n\nاز طریق منوی زیر می‌توانید سرویس مورد نظر خود را تهیه کرده و از اینترنت بدون محدودیت لذت ببرید."
NOT_ADMIN_ACCESS = "⛔️ شما دسترسی به این بخش را ندارید."
INVALID_OPTION = "گزینه انتخاب شده نامعتبر است."
PLEASE_WAIT = "⏳ لطفاً چند لحظه صبر کنید..."
OPERATION_SUCCESS = "✅ عملیات با موفقیت انجام شد."
OPERATION_FAILED = "❌ متاسفانه در انجام عملیات خطایی رخ داد. لطفاً دوباره تلاش کنید یا با پشتیبانی تماس بگیرید."
UNDER_CONSTRUCTION = "🚧 این بخش در حال حاضر در دست ساخت و توسعه است. به زودی به ربات اضافه خواهد شد!"
INVALID_NUMBER_INPUT = "ورودی نامعتبر است. لطفاً یک عدد صحیح وارد کنید."

# =============================================================================
# SECTION: پیام‌های پنل ادمین
# =============================================================================
ADMIN_WELCOME = "👑 به پنل مدیریت serverusaa_bot خوش آمدید!\n\nاز طریق دکمه‌های زیر می‌توانید ربات را مدیریت کنید."
SERVER_MGMT_MENU_TEXT = "⚙️ گزینه‌های مدیریت سرور:"
PLAN_MGMT_MENU_TEXT = "💰 گزینه‌های مدیریت پلن:"
PAYMENT_GATEWAY_MGMT_MENU_TEXT = "💳 گزینه‌های مدیریت درگاه‌های پرداخت:"
USER_MGMT_MENU_TEXT = "👥 گزینه‌های مدیریت کاربران:"

# --- مدیریت سرور ---
ADD_SERVER_PROMPT_NAME = "لطفاً یک نام دلخواه برای سرور جدید وارد کنید (مثال: آلمان - هتزنر):"
ADD_SERVER_PROMPT_URL = "لطفاً آدرس کامل پنل X-UI را وارد کنید (مثال: http://1.2.3.4:54321):"
ADD_SERVER_PROMPT_USERNAME = "لطفاً نام کاربری پنل X-UI را وارد کنید:"
ADD_SERVER_PROMPT_PASSWORD = "لطفاً رمز عبور پنل X-UI را وارد کنید:"
ADD_SERVER_PROMPT_SUB_BASE_URL = "لطفاً آدرس پایه سابسکریپشن را وارد کنید (مثال: https://yourdomain.com:2096):"
ADD_SERVER_PROMPT_SUB_PATH_PREFIX = "لطفاً پیشوند مسیر سابسکریپشن را وارد کنید (مثال: sub):"
ADD_SERVER_TESTING = "⏳ در حال تست اتصال و ورود به پنل سرور..."
ADD_SERVER_SUCCESS = "✅ سرور **{server_name}** با موفقیت اضافه شد و آنلاین است."
ADD_SERVER_DB_ERROR = "❌ خطایی در ذخیره سرور **{server_name}** رخ داد. (احتمالاً نام سرور تکراری است)."
ADD_SERVER_LOGIN_FAILED = "❌ اتصال به پنل X-UI سرور **{server_name}** ناموفق بود. لطفاً اطلاعات وارد شده را بررسی کنید."
NO_SERVERS_FOUND = "هیچ سروری در سیستم ثبت نشده است."
LIST_SERVERS_HEADER = "📄 **لیست سرورهای ثبت شده:**\n\n"
SERVER_DETAIL_TEMPLATE = (
    "**🔸 نام:** {name} (ID: `{id}`)\n"
    "**وضعیت اتصال:** {status}\n"
    "**وضعیت فروش:** {is_active_emoji}\n"
    "**فرمت لینک:** `{sub_link}`\n"
    "-----------------------------------\n"
)
DELETE_SERVER_PROMPT = "لطفاً ID سروری که می‌خواهید حذف شود را وارد کنید:"
DELETE_SERVER_CONFIRM = "⚠️ آیا از حذف سرور **{server_name}** با شناسه `{server_id}` مطمئن هستید؟\n\n**این عمل غیرقابل بازگشت است و تمام کاربران این سرور غیرفعال خواهند شد.**"
SERVER_DELETED_SUCCESS = "✅ سرور '{server_name}' با موفقیت حذف شد."
SERVER_DELETED_ERROR = "❌ حذف سرور ناموفق بود."
SERVER_NOT_FOUND = "سروری با ID وارد شده یافت نشد."
TESTING_ALL_SERVERS = "⏳ در حال تست اتصال به تمام سرورها..."
TEST_RESULTS_HEADER = "📊 نتایج تست اتصال سرورها:\n\n"

# --- مدیریت Inbound ---
SELECT_SERVER_FOR_INBOUNDS_PROMPT = "لطفاً سروری که می‌خواهید Inboundهای آن را مدیریت کنید، انتخاب نمایید:"
FETCHING_INBOUNDS = "⏳ در حال دریافت لیست Inboundها از پنل..."
NO_INBOUNDS_FOUND_ON_PANEL = "هیچ Inboundی در پنل X-UI این سرور یافت نشد یا اتصال برقرار نشد."
SELECT_INBOUNDS_TO_ACTIVATE = " لطفاً اینباندهایی که می‌خواهید برای ساخت کانفیگ کاربران استفاده شوند را برای سرور **{server_name}** انتخاب کنید:"
INBOUND_CONFIG_SUCCESS = "✅ تنظیمات Inboundها برای سرور '{server_name}' با موفقیت ذخیره شد."
INBOUND_CONFIG_FAILED = "❌ خطایی در ذخیره تنظیمات Inboundها رخ داد."

# --- مدیریت پلن‌ها ---
ADD_PLAN_PROMPT_NAME = "لطفاً نامی برای پلن وارد کنید (مثال: ۱ ماهه ۵۰ گیگ):"
ADD_PLAN_PROMPT_TYPE = "لطفاً نوع پلن را انتخاب کنید:"
ADD_PLAN_PROMPT_VOLUME = "لطفاً حجم پلن را به گیگابایت (GB) وارد کنید (مثال: 50.5):"
ADD_PLAN_PROMPT_DURATION = "لطفاً مدت زمان پلن را به روز وارد کنید (مثال: 30):"
ADD_PLAN_PROMPT_DURATION_GB = "لطفاً مدت زمان اعتبار این پلن گیگابایتی را به **روز** وارد کنید.\n(برای اعتبار نامحدود، عدد **0** را وارد کنید)"
ADD_PLAN_PROMPT_PRICE = "لطفاً قیمت پلن را به تومان وارد کنید (مثال: 150000):"
ADD_PLAN_PROMPT_PER_GB_PRICE = "لطفاً قیمت هر گیگابایت (GB) را به تومان وارد کنید (مثال: 1800):"
ADD_PLAN_SUCCESS = "✅ پلن '{plan_name}' با موفقیت اضافه شد."
ADD_PLAN_DB_ERROR = "❌ خطایی در ذخیره پلن '{plan_name}' رخ داد (ممکن است نام تکراری باشد)."
NO_PLANS_FOUND = "هیچ پلنی در دیتابیس ثبت نشده است."
LIST_PLANS_HEADER = "📄 **لیست پلن‌های ثبت شده:**\n\n"
TOGGLE_PLAN_STATUS_PROMPT = "لطفاً ID پلنی که می‌خواهید وضعیت آن (فعال/غیرفعال) را تغییر دهید، وارد کنید:"
PLAN_NOT_FOUND = "پلنی با ID وارد شده یافت نشد."
PLAN_STATUS_TOGGLED_SUCCESS = "✅ وضعیت پلن '{plan_name}' به '{new_status}' تغییر یافت."
PLAN_STATUS_TOGGLED_ERROR = "❌ خطایی در تغییر وضعیت پلن رخ داد."

# --- مدیریت درگاه پرداخت ---
ADD_GATEWAY_PROMPT_NAME = "لطفاً نامی برای درگاه وارد کنید (مثال: کارت به کارت ملت):"
ADD_GATEWAY_PROMPT_CARD_NUMBER = "لطفاً شماره کارت را وارد کنید:"
ADD_GATEWAY_PROMPT_CARD_HOLDER_NAME = "لطفاً نام صاحب کارت را وارد کنید:"
ADD_GATEWAY_PROMPT_DESCRIPTION = "توضیحات اضافی برای درگاه را وارد کنید (اختیاری، برای انصراف کلمه `skip` را وارد کنید):"
ADD_GATEWAY_SUCCESS = "✅ درگاه '{gateway_name}' با موفقیت اضافه شد."
ADD_GATEWAY_DB_ERROR = "❌ خطایی در ذخیره درگاه '{gateway_name}' رخ داد."
LIST_GATEWAYS_HEADER = "📄 **لیست درگاه‌های پرداخت:**\n\n"
NO_GATEWAYS_FOUND = "هیچ درگاهی ثبت نشده است."
TOGGLE_GATEWAY_STATUS_PROMPT = "ID درگاهی که می‌خواهید وضعیت آن را تغییر دهید وارد کنید:"
GATEWAY_NOT_FOUND = "درگاهی با ID وارد شده یافت نشد."
GATEWAY_STATUS_TOGGLED_SUCCESS = "✅ وضعیت درگاه '{gateway_name}' به '{new_status}' تغییر یافت."
GATEWAY_STATUS_TOGGLED_ERROR = "❌ خطایی در تغییر وضعیت درگاه رخ داد."

# --- مدیریت کاربران ---
LIST_USERS_HEADER = "👥 **لیست کاربران ربات:**\n\n"
NO_USERS_FOUND = "هیچ کاربری در ربات ثبت‌نام نکرده است."

# --- نوتیفیکیشن ادمین ---
ADMIN_NEW_PAYMENT_NOTIFICATION_HEADER = "🔔 **درخواست پرداخت جدید** 🔔\n\n"
ADMIN_NEW_PAYMENT_NOTIFICATION_DETAILS = (
    "👤 **کاربر:** [{user_first_name}](tg://user?id={user_telegram_id})\n"
    "💰 **مبلغ:** `{amount:,.0f}` تومان\n"
    "🌐 **سرور:** `{server_name}`\n"
    "📦 **پلن:** `{plan_details}`\n"
    "💳 **درگاه:** `{gateway_name}`\n\n"
    "لطفاً پس از بررسی، وضعیت را مشخص کنید."
)
ADMIN_PAYMENT_CONFIRMED_DISPLAY = "✅ *این پرداخت توسط {admin_username} تأیید شد.*"
ADMIN_PAYMENT_REJECTED_DISPLAY = "❌ *این پرداخت توسط {admin_username} رد شد.*"

# =============================================================================
# SECTION: پیام‌های پنل کاربر
# =============================================================================
USER_MAIN_MENU_TEXT = "👇 لطفاً یکی از گزینه‌های زیر را انتخاب کنید:"
REQUIRED_CHANNEL_PROMPT = "🙏 برای استفاده از امکانات ربات، لطفاً ابتدا در کانال ما عضو شوید:\n{channel_link}\n\nپس از عضویت، دوباره دستور /start را بزنید."
NO_ACTIVE_SERVERS_FOR_BUY = "😔 متاسفانه در حال حاضر سرور فعالی برای خرید وجود ندارد. لطفاً بعداً دوباره تلاش کنید."
SELECT_SERVER_PROMPT = "📍 از کدام یک از سرورهای پرسرعت ما می‌خواهید استفاده کنید؟"
SELECT_PLAN_TYPE_PROMPT_USER = "📄 لطفاً نوع پلن مورد نظر خود را انتخاب نمایید:"
NO_FIXED_PLANS_AVAILABLE = "😔 در حال حاضر پلن ثابتی برای این سرور ارائه نشده است."
SELECT_FIXED_PLAN_PROMPT = "🛍️ لطفاً یکی از پلن‌های زیر را انتخاب کنید:"
ENTER_GIGABYTES_PROMPT = "لطفاً مقدار حجم مورد نیاز خود را به **گیگابایت** وارد کنید (مثلاً: 20 یا 10.5):"
GIGABYTE_PLAN_NOT_CONFIGURED = "متاسفانه پلن گیگابایتی پیکربندی نشده است."

# --- خلاصه سفارش کاربر ---
ORDER_SUMMARY_HEADER = "📝 **خلاصه سفارش شما**\n\n"
ORDER_SUMMARY_SERVER = "🌐 **سرور:** `{server_name}`\n"
ORDER_SUMMARY_PLAN = "📦 **پلن:** `{plan_name}`\n"
ORDER_SUMMARY_VOLUME = "💾 **حجم:** `{volume_gb} GB`\n"
ORDER_SUMMARY_DURATION = "⏳ **مدت زمان:** `{duration_days}`\n"
ORDER_SUMMARY_TOTAL_PRICE = "💰 **مبلغ قابل پرداخت:** `{total_price:,.0f} تومان`\n"
ORDER_SUMMARY_CONFIRM_PROMPT = "\nلطفاً اطلاعات بالا را به دقت بررسی کرده و در صورت صحت، پرداخت را تأیید کنید."
ORDER_CANCELED = "سفارش شما لغو شد."

# --- پرداخت کاربر ---
SELECT_PAYMENT_GATEWAY_PROMPT = "لطفاً روش پرداخت خود را انتخاب کنید:"
NO_ACTIVE_PAYMENT_GATEWAYS = "در حال حاضر روش پرداختی فعال نیست."
PAYMENT_GATEWAY_DETAILS = (
    "برای تکمیل خرید، لطفاً مبلغ **{amount:,.0f} تومان** را به اطلاعات زیر واریز نمایید:\n\n"
    "💳 **شماره کارت:**\n`{card_number}`\n\n"
    "👤 **صاحب کارت:**\n`{card_holder_name}`\n\n"
    "پس از واریز، **عکس کامل و واضح رسید پرداخت** را در همین صفحه ارسال کنید. سفارش شما پس از تایید به صورت خودکار فعال خواهد شد."
)
INVALID_RECEIPT_FORMAT = "فرمت نامعتبر است. لطفاً فقط **عکس رسید** پرداخت را ارسال کنید."
RECEIPT_RECEIVED_USER = "✅ رسید شما با موفقیت دریافت شد.\n\nپس از تایید توسط ادمین، سرویس شما به صورت خودکار فعال و اطلاعات آن برایتان ارسال خواهد شد. از صبر شما متشکریم!"

# --- تحویل سرویس و تست رایگان ---
SERVICE_ACTIVATION_SUCCESS_USER = "🎉 سرویس شما با موفقیت فعال شد!"
CONFIG_DELIVERY_HEADER = "در ادامه، اطلاعات سرویس شما آمده است:"
CONFIG_DELIVERY_SUB_LINK = "\n🔗 **لینک اشتراک (Subscription Link):**\n`{sub_link}`\n\n_(این لینک را کپی کرده و در اپلیکیشن خود وارد کنید تا تمام کانفیگ‌ها اضافه شوند.)_"
QR_CODE_CAPTION = "می‌توانید با اسکن کد بالا، لینک را مستقیماً به اپلیکیشن خود اضافه کنید."
GET_SINGLE_CONFIGS_BUTTON = "📄 دریافت کانفیگ‌های تکی"
NO_SINGLE_CONFIGS_AVAILABLE = "کانفیگ تکی برای این سرویس موجود نیست."
SINGLE_CONFIG_HEADER = "📄 **کانفیگ‌های تکی شما:**\n\n"
GET_FREE_TEST_SUCCESS = "✅ اکانت تست رایگان شما با موفقیت ساخته شد!\nحجم: **100 مگابایت**\nمدت زمان: **۲۴ ساعت**"
FREE_TEST_ALREADY_USED = "😔 شما قبلاً از اکانت تست رایگان خود استفاده کرده‌اید.\n\nهر کاربر فقط یک بار مجاز به دریافت اکانت تست می‌باشد."
PAYMENT_REJECTED_USER = "❌ پرداخت شما توسط مدیریت تأیید نشد. لطفاً جهت پیگیری با پشتیبانی ({support_link}) در ارتباط باشید."

# --- سرویس‌های من ---
MY_SERVICES_HEADER = "🗂️ **سرویس‌های شما**\n\nدر زیر، لیست سرویس‌هایی که تاکنون خریداری کرده‌اید آمده است. برای مشاهده جزئیات و دریافت مجدد کانفیگ، روی هر مورد کلیک کنید."
MY_SERVICES_ITEM = (
    "🔹 **سرویس ID:** `{purchase_id}`\n"
    "   **سرور:** {server_name}\n"
    "   **حجم اولیه:** {volume_gb} گیگابایت\n"
    "   **تاریخ خرید:** {purchase_date}\n"
    "   **تاریخ انقضا:** {expire_date}\n"
    "   **وضعیت:** {status}\n"
    "--------------------\n"
)
NO_SERVICES_FOUND = "شما در حال حاضر هیچ سرویس فعالی ندارید."


# --- مدیریت درگاه پرداخت ---
ADD_GATEWAY_PROMPT_TYPE = "لطفاً نوع درگاه پرداخت را انتخاب کنید:"
ADD_GATEWAY_PROMPT_MERCHANT_ID = "لطفاً مرچنت کد (Merchant ID) درگاه زرین‌پال را وارد کنید:"
